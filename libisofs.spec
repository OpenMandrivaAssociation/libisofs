%define major 6
%define libname %mklibname isofs %{major}
%define develname %mklibname isofs -d

Summary:	Library for creating ISO disc images
Name:		libisofs
Version:	1.2.4
Release:	1
License:	GPLv2+
Group:		System/Libraries
URL:		http://libburnia-project.org/wiki/Libisofs
Source0:	http://files.libburnia-project.org/releases/%{name}-%{version}.tar.gz
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	pkgconfig(libburn-1)

%description
Libisofs is a library that handles creating ISO disc image files. It
is intended to work together with libburn to write these images to
discs.

%package -n %{libname}
Summary:	Library for creating ISO disc images
Group:		System/Libraries

%description -n %{libname}
Libisofs is a library that handles creating ISO disc image files. It
is intended to work together with libburn to write these images to
discs.

%package -n %{develname}
Summary:	Header files for development with %{name}
Group:		Development/C
Provides:	libisofs-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
This package includes the header files for the %{name} package.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

# build documentation
doxygen doc/doxygen.conf

%files -n %{libname}
%{_libdir}/libisofs.so.%{major}*

%files -n %{develname}
%doc README AUTHORS COPYRIGHT
%{_libdir}/libisofs.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}


%changelog
* Mon Jul 30 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.4-1
+ Revision: 811450
- version update  1.2.4

* Sat Apr 07 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.2-1
+ Revision: 789782
- update to new version 1.2.2

* Thu Feb 02 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.0-2
+ Revision: 770656
- removed BuildRoot

* Thu Feb 02 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.0-1
+ Revision: 770649
- version update 1.2.0 file added
- version update 1.2.0

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.6-1
+ Revision: 703678
- update to new version 1.1.6

* Mon Aug 29 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.4-1
+ Revision: 697346
- update to new version 1.1.4

* Sat Nov 06 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.38-1mdv2011.0
+ Revision: 594168
- update to new version 0.6.38

* Sat Sep 18 2010 Funda Wang <fwang@mandriva.org> 0.6.36-1mdv2011.0
+ Revision: 579315
- new versiion 0.6.36

* Sun Jul 11 2010 Emmanuel Andry <eandry@mandriva.org> 0.6.34-1mdv2011.0
+ Revision: 550715
- New version 0.6.34

* Sat Feb 20 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.28-1mdv2010.1
+ Revision: 508795
- update to new version 0.6.28

* Sun Jan 24 2010 Frederik Himpe <fhimpe@mandriva.org> 0.6.26-1mdv2010.1
+ Revision: 495522
- update to new version 0.6.26

* Sat Nov 07 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.24-1mdv2010.1
+ Revision: 462513
- update to new version 0.6.24

* Wed Sep 02 2009 Frederik Himpe <fhimpe@mandriva.org> 0.6.22-1mdv2010.0
+ Revision: 425462
- update to new version 0.6.22

* Mon Jul 27 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.20-2mdv2010.0
+ Revision: 401039
- rebuild
- update to new version 0.6.20

* Wed Mar 11 2009 Frederik Himpe <fhimpe@mandriva.org> 0.6.16-1mdv2009.1
+ Revision: 353958
- update to new version 0.6.16

* Sun Mar 01 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.14-1mdv2009.1
+ Revision: 346343
- update to new version 0.6.14

* Fri Nov 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.12-1mdv2009.1
+ Revision: 307475
- update to new version 0.6.12
- fix urls
- spec file clean

* Tue Oct 14 2008 Funda Wang <fwang@mandriva.org> 0.6.10-1mdv2009.1
+ Revision: 293510
- new version 0.6.10

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.6.6-2mdv2009.0
+ Revision: 267820
- rebuild early 2009.0 package (before pixel changes)

* Thu Jun 12 2008 Adam Williamson <awilliamson@mandriva.org> 0.6.6-1mdv2009.0
+ Revision: 218277
- new release 0.6.6

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue May 13 2008 Adam Williamson <awilliamson@mandriva.org> 0.6.4-2mdv2009.0
+ Revision: 206730
- rebuild with newer libburn

* Tue May 13 2008 Adam Williamson <awilliamson@mandriva.org> 0.6.4-1mdv2009.0
+ Revision: 206524
- new release 0.6.4

* Thu Apr 17 2008 Adam Williamson <awilliamson@mandriva.org> 0.6.2.1-1mdv2009.0
+ Revision: 195307
- clean spec
- new release 0.6.2.1

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.2.8-1mdv2008.1
+ Revision: 140924
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Aug 26 2007 Adam Williamson <awilliamson@mandriva.org> 0.2.8-1mdv2008.0
+ Revision: 71456
- don't package COPYING, not needed
- protect against major change in file list
- use Fedora license policy
- new major 5
- new release 0.2.8 (now supported by brasero)
- add note about not updating to newer versions

* Tue Jul 31 2007 Adam Williamson <awilliamson@mandriva.org> 0.2.5-1mdv2008.0
+ Revision: 57149
- new release 0.2.5

* Tue Jul 03 2007 Adam Williamson <awilliamson@mandriva.org> 0.2.4-1mdv2008.0
+ Revision: 47402
- buildrequires libburn
- Import libisofs

