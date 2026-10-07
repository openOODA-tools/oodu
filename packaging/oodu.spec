Name:           oodu
Version:        0.1.0
Release:        1%{?dist}
Summary:        Fast parallel disk space estimator tracking inode counts and directory tree weights.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oodu
Source0:        oodu-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oodu is a sovereign, capability-bounded DISK USAGE written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oodu
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oodu-uninstall

%files
/usr/bin/oodu
/usr/bin/oodu-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
