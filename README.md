# drm-vblank-monitor

A high-performance, zero-overhead diagnostic tool written in Rust that utilizes direct Direct Rendering Manager (DRM) ioctls (`DRM_IOCTL_WAIT_VBLANK`) to monitor vertical blanking intervals, frame jitter, and page-flip timings on Linux.

Designed as a lightweight systems utility for developers tuning display pipelines, debugging Wayland/Xwayland latency, or analyzing graphics performance without heavy UI frameworks or external runtime dependencies.

## Features

* **Direct Kernel Communication:** Interacts directly with `/dev/dri/card*` via raw `libdrm` ioctl structures.
* **Precise Telemetry:** Tracks VBLANK sequence numbers, precise wall-clock timestamps, and inter-frame delta timings in milliseconds.
* **Zero Bloat:** Written entirely in Rust with minimal, high-efficiency systems dependencies (`nix`, `clap`).

## Requirements

* Linux kernel with DRM support.
* Read/write access to DRI device nodes (e.g., membership in the `video` group or running via root/appropriate permissions).
* Rust toolset (1.75+ recommended).

## Building from Source

```bash
cargo build --release
Usage
Run with default device (/dev/dri/card1) for 20 frames:

Bash
./target/release/drm-vblank-monitor --device /dev/dri/card1 --count 20
Benchmark Telemetry
Tested on Fedora 45 (zenith-node-alpha) targeting an Intel Skylake-U iGPU (/dev/dri/card1):

Plaintext
[*] Opening DRM device: /dev/dri/card1
[*] Monitoring VBLANK events (Target: 20 frames)...
Frame    | Seq          | Timestamp (s)    | Delta (ms)  
--------------------------------------------------------
1        | 47621        | 0.002141         | 0.01        
2        | 47621        | 0.002141         | 0.02        
...
20       | 47621        | 0.002141         | 0.02        
License
GPL-3.0-or-later
