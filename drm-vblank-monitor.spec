Name:           drm-vblank-monitor
Version:        0.1.0
Release:        1%{?dist}
Summary:        DRM vblank monitoring tool

License:        MIT
URL:            https://github.com/SimoesCTT/drm-vblank-monitor
Source0:        %{url}/archive/v%{version}/drm-vblank-monitor-%{version}.tar.gz

BuildRequires:  cargo >= 1.70
BuildRequires:  rustc >= 1.70
BuildRequires:  libdrm-devel

%description
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
- Initial package with vendored dependencies
