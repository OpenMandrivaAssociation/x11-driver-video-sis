%define _disable_ld_no_undefined 1

Summary:	X.org driver for SiS Cards
Name:		x11-driver-video-sis
Version:	0.10.7
Release:	18
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-sis-%{version}.tar.bz2
Patch0:		remove_mibstore_h.patch
Patch1:		0001-Fix-compilation-with-Werror-format-security.patch
Patch2:		0001-Replace-xf86UnMapVidMem-with-pci_device_unmap_range.diff
# archlinux
Patch3:		u_Fixed-build-with-INPUT_API-19.patch
Patch4:		0001-Disable-UploadToScreen-and-DownloadFromScreen.patch
Patch5:		U_sis-fix-build-against-latest-xserver.patch
Patch6:		U_sis-more-build-fixes-against-master-X-server.patch
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

