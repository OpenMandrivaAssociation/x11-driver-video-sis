Name: x11-driver-video-sis
Version: 0.10.7
Release: 1
Summary: X.org driver for SiS Cards
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-sis-%{version}.tar.bz2
Patch1: 0001-Fix-compilation-with-Werror-format-security.patch
 
BuildRequires: libdrm-devel >= 2.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.12
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: pkgconfig(gl)

Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

Conflicts: xorg-x11-server < 7.0

%description
x11-driver-video-sis is the X.org driver for SiS Cards.

%prep
%setup -qn xf86-video-sis-%{version}
%apply_patches

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%{_libdir}/xorg/modules/drivers/sis_drv.so
%{_mandir}/man4/sis.*

