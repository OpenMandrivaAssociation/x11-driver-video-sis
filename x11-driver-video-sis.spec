%define _disable_ld_no_undefined 1

Summary:	X.org driver for SiS Cards
Name:		x11-driver-video-sis
Version:	0.12.0
Release:	3
Group:		System/X11
License:	MIT
Url:		https://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-sis-%{version}.tar.bz2
Patch0:		xf86-video-sis-0.12.0-compile.patch
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-sis is the X.org driver for SiS Cards.

%prep
%autosetup -n xf86-video-sis-%{version} -p1

%build
# For reasons currently unknown, X drivers tend to crash Xorg if built with clang
export CC=gcc
export CXX=g++
%configure
%make_build

%install
%make_install

%files
%{_libdir}/xorg/modules/drivers/sis_drv.so
%{_mandir}/man4/sis.*

