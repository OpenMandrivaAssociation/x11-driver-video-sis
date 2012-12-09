Name: x11-driver-video-sis
Version: 0.10.7
Release: 2
Summary: X.org driver for SiS Cards
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-sis-%{version}.tar.bz2
Patch1: 0001-Fix-compilation-with-Werror-format-security.patch
Patch2:	0001-Replace-xf86UnMapVidMem-with-pci_device_unmap_range.diff
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



%changelog
* Mon Jul 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.10.7-1
+ Revision: 810691
- version update 0.10.7

* Fri Jul 06 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.10.6-1
+ Revision: 808304
- version update 0.10.6

* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.10.4-2
+ Revision: 787270
- Rebuild for x11-server 1.12

* Sun Mar 25 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.10.4-1
+ Revision: 786718
- version update 0/10/4

* Sat Dec 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.10.3-7
+ Revision: 748466
- rebuild cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.10.3-6
+ Revision: 703744
- rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.10.3-5
+ Revision: 683545
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 0.10.3-4
+ Revision: 671177
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 0.10.3-3mdv2011.0
+ Revision: 595713
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 0.10.3-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Tue Jul 20 2010 Thierry Vignaud <tv@mandriva.org> 0.10.3-1mdv2011.0
+ Revision: 555161
- new release

* Tue Nov 10 2009 Thierry Vignaud <tv@mandriva.org> 0.10.2-2mdv2010.1
+ Revision: 464341
- rebuild for new xserver

* Mon Aug 03 2009 Thierry Vignaud <tv@mandriva.org> 0.10.2-1mdv2010.0
+ Revision: 407718
- fix build
- new release

* Tue Dec 30 2008 Colin Guthrie <cguthrie@mandriva.org> 0.10.1-2mdv2009.1
+ Revision: 321381
- Rebuild for new xserver

* Tue Dec 23 2008 Ander Conselvan de Oliveira <ander@mandriva.com> 0.10.1-1mdv2009.1
+ Revision: 317952
- Fix compilation with -Werror=format-security
- New version 0.10.1

* Sat Nov 29 2008 Adam Williamson <awilliamson@mandriva.org> 0.10.0-3mdv2009.1
+ Revision: 308148
- rebuild for new X server

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)
    - improved description
    - add missing dot at end of description
    - improved summary

* Tue Apr 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.10.0-1mdv2009.0
+ Revision: 194153
- Update to version 0.10.0.

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.9.4-4mdv2008.1
+ Revision: 166110
- Revert to use upstream tarball and remove local patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 0.9.4-3mdv2008.1
+ Revision: 156620
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.9.4-2mdv2008.1
+ Revision: 154794
- Updated BuildRequires and resubmit package.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Properly use existing tag xf86-video-sis-0.9.4 to generate tarball.
  There was no changes from this tag to the point mandriva branch was created,
  so, only spec changes were generated.
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 19 2007 Thierry Vignaud <tv@mandriva.org> 0.9.4-1mdv2008.1
+ Revision: 110426
- new release

* Tue Oct 16 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 0.9.3-2mdv2008.1
+ Revision: 99046
- minor spec cleanup
- build against new xserver (1.4)

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages

