Name:           drm-vblank-monitor
Version:        0.1.0
Release:        1%{?dist}
Summary:        Real-time DRM VBLANK monitor and frame timing tool written in Rust

License:        GPL-3.0-or-later
URL:            https://github.com/SimoesCTT/drm-vblank-monitor
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  rust-toolset
BuildRequires:  cargo

%description
A high-performance, zero-overhead diagnostic tool utilizing direct DRM ioctls 
to monitor vertical blanking intervals, frame jitter, and page-flip timings on Linux.

%prep
%autosetup

%build
%cargo_build

%install
%cargo_install

%files
%{_bindir}/drm-vblank-monitor

%changelog
* Wed Nov 18 2026 Americo Simoes <amexsimoes@gmail.com> - 0.1.0-1
- Initial package release for Fedora Copr
