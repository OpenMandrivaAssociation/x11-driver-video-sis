%define _disable_ld_no_undefined 1

Summary:	X.org driver for SiS Cards
Name:		x11-driver-video-sis
Version:	0.10.7
Release:	9
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-sis-%{version}.tar.bz2
Patch0:		remove_mibstore_h.patch
Patch1:		0001-Fix-compilation-with-Werror-format-security.patch
Patch2:		0001-Replace-xf86UnMapVidMem-with-pci_device_unmap_range.diff
# archlinux
Patch3:		Xi.patch

BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-sis is the X.org driver for SiS Cards.

%prep
%setup -qn xf86-video-sis-%{version}
%apply_patches

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/drivers/sis_drv.so
%{_mandir}/man4/sis.*

