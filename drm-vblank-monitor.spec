Name:           drm-vblank-monitor
Version:        0.1.0
Release:        1%{?dist}
<<<<<<< HEAD
Summary:        DRM vblank monitoring tool
=======
Summary:        High-performance Rust DRM VBLANK monitor and frame timing tool
>>>>>>> 23898d3275beb8f79103065ea7d976e2068d942a

License:        MIT
URL:            https://github.com/SimoesCTT/drm-vblank-monitor
<<<<<<< HEAD
Source0:        %{url}/archive/v%{version}/drm-vblank-monitor-%{version}.tar.gz
=======
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
>>>>>>> 23898d3275beb8f79103065ea7d976e2068d942a

BuildRequires:  cargo >= 1.70
BuildRequires:  rustc >= 1.70
BuildRequires:  libdrm-devel

%description
<<<<<<< HEAD
DRM vblank monitoring tool for Linux systems.

%prep
%autosetup -n drm-vblank-monitor-%{version} -p1

# Setup cargo config for vendored dependencies
mkdir -p .cargo
cat > .cargo/config.toml << 'CONFIG'
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
CONFIG
=======
A lightweight, zero-overhead diagnostic tool utilizing direct DRM ioctls 
to monitor vertical blanking intervals, frame jitter, and page-flip timings on Linux.

%prep
%autosetup -n %{name}-%{version}
>>>>>>> 23898d3275beb8f79103065ea7d976e2068d942a

%build
cargo build --release --offline

%install
install -d %{buildroot}%{_bindir}
install -m 0755 target/release/drm-vblank-monitor %{buildroot}%{_bindir}/drm-vblank-monitor

%files
%{_bindir}/drm-vblank-monitor
%license LICENSE
%doc README.md

%changelog
* Wed Nov 18 2026 Americo Simoes <amexsimoes@gmail.com> - 0.1.0-1
<<<<<<< HEAD
- Initial package with vendored dependencies
=======
- Initial release v0.1.0 for Fedora Copr
>>>>>>> 23898d3275beb8f79103065ea7d976e2068d942a
