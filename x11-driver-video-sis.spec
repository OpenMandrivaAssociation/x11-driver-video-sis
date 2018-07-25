%define _disable_ld_no_undefined 1

Summary:	X.org driver for SiS Cards
Name:		x11-driver-video-sis
Version:	0.10.8.20161117
Release:	3
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-sis-%{version}.tar.bz2
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
[ -e autogen.sh ] && ./autogen.sh

%build
# For reasons currently unknown, X drivers tend to crash Xorg if built with clang
export CC=gcc
export CXX=g++
%configure
%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/drivers/sis_drv.so
%{_mandir}/man4/sis.*

