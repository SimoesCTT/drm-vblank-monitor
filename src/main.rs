use clap::Parser;
use std::fs::File;
use std::os::unix::io::AsRawFd;
use std::time::Instant;

#[derive(Parser, Debug)]
#[command(author, version, about, long_about = None)]
struct Args {
    #[arg(short, long, default_value = "/dev/dri/card0")]
    device: String,

    #[arg(short, long, default_value_t = 100)]
    count: usize,
}

const DRM_IOCTL_BASE: u8 = 'd' as u8;

#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct DrmVblankReply {
    pub sequence: u32,
    pub t_sec: u32,
    pub t_usec: u32,
}

#[repr(C)]
#[derive(Copy, Clone)]
pub union DrmVblankUnion {
    pub request: u32,
    pub reply: DrmVblankReply,
}

// Manual Debug implementation for the union
impl std::fmt::Debug for DrmVblankUnion {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.debug_struct("DrmVblankUnion").finish()
    }
}

#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct DrmVblank {
    pub type_: u32,
    pub flags: u32,
    pub union_: DrmVblankUnion,
}

nix::ioctl_readwrite!(drm_wait_vblank, DRM_IOCTL_BASE, 0x3a, DrmVblank);

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let args = Args::parse();

    println!("[*] Opening DRM device: {}", args.device);
    let file = File::open(&args.device)?;
    let fd = file.as_raw_fd();

    println!("[*] Monitoring VBLANK events (Target: {} frames)...", args.count);
    println!("{:<8} | {:<12} | {:<16} | {:<12}", "Frame", "Seq", "Timestamp (s)", "Delta (ms)");
    println!("{}", "-".repeat(56));

    let mut last_instant = Instant::now();

    for i in 0..args.count {
        let mut vbl = DrmVblank {
            type_: 1, // 1 = relative sequence
            flags: 0,
            union_: DrmVblankUnion { request: 1 }, // wait for 1 vblank ahead
        };

        let start_wait = Instant::now();
        unsafe {
            if let Err(e) = drm_wait_vblank(fd, &mut vbl) {
                eprintln!("[-] DRM ioctl DRM_IOCTL_WAIT_VBLANK failed: {}", e);
                break;
            }
        }

        let _elapsed = start_wait.elapsed();
        let reply = unsafe { vbl.union_.reply };
        let timestamp_sec = reply.t_sec as f64 + (reply.t_usec as f64 / 1_000_000.0);
        let delta_ms = last_instant.elapsed().as_secs_f64() * 1000.0;
        last_instant = Instant::now();

        println!(
            "{:<8} | {:<12} | {:<16.6} | {:<12.2}",
            i + 1,
            reply.sequence,
            timestamp_sec,
            delta_ms
        );
    }

    Ok(())
}
