Name: x11-driver-video-sis
Version: 0.10.3
Release: %mkrel 1
Summary: X.org driver for SiS Cards
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-sis-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
 
BuildRequires: libdrm-devel >= 2.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: GL-devel

Conflicts: xorg-x11-server < 7.0

Patch1: 0001-Fix-compilation-with-Werror-format-security.patch
%description
x11-driver-video-sis is the X.org driver for SiS Cards.

%prep
%setup -q -n xf86-video-sis-%{version}
%patch1 -p1 -b .format-security

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/sis_drv.la
%{_libdir}/xorg/modules/drivers/sis_drv.so
%{_mandir}/man4/sis.*
