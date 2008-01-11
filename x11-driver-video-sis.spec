%define debug_package	%{nil}

Name: x11-driver-video-sis
Version: 0.9.4
Release: %mkrel 2
Summary: The X.org driver for SiS Cards
Group: System/X11
URL: http://xorg.freedesktop.org
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-sis  xorg/drivers/xf86-video-sis
# cd xorg/drivers/xf86-video/sis
# git-archive --format=tar --prefix=xf86-video-sis-0.9.4/ xf86-video-sis-0.9.4 | bzip2 -9 > xf86-video-sis-0.9.4.tar.bz2
########################################################################
Source0: xf86-video-sis-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xf86-video-sis-0.9.4..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################
BuildRequires: x11-util-macros		>= 1.1.5-4mdk
#BuildRequires: gcc			>= 4.2.2
#BuildRequires: glibc-devel		>= 2.7
BuildRequires: libdrm-devel		>= 2.3.0
BuildRequires: libpixman-1-devel	>= 0.9.6
BuildRequires: x11-proto-devel		>= 7.3
BuildRequires: libmesagl-devel		>= 7.0.2
BuildRequires: x11-server-devel		>= 1.4

BuildRequires: GL-devel
Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for SiS Cards

%prep
%setup -q -n xf86-video-sis-%{version}

%patch1 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/xorg/modules/drivers/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/sis_drv.so
%{_mandir}/man4/sis.*
