Name:           drm-vblank-monitor
Version:        0.1.0
Release:        1%{?dist}
Summary:        High-performance Rust DRM VBLANK monitor and frame timing tool

License:        GPL-3.0-or-later
URL:            https://github.com/SimoesCTT/drm-vblank-monitor
Source0:        v%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  rustc

%description
A lightweight, zero-overhead diagnostic tool utilizing direct DRM ioctls 
to monitor vertical blanking intervals, frame jitter, and page-flip timings on Linux.

%prep
%autosetup -n %{name}-%{version}

%build
cargo build --release

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 target/release/drm-vblank-monitor %{buildroot}%{_bindir}/drm-vblank-monitor

%files
%{_bindir}/drm-vblank-monitor

%changelog
* Wed Nov 18 2026 Americo Simoes <amexsimoes@gmail.com> - 0.1.0-1
- Initial release v0.1.0 for Fedora Copr
