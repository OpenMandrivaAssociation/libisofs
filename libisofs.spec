%define name    libisofs
%define version 0.2.4
%define rel 	1

%define major 	4
%define libname %mklibname isofs %major
%define develname %mklibname isofs -d

Summary: 	Library for creating ISO disc images
Name: 		%name
Version: 	%version
Release: 	%mkrel %rel
Url: 		http://libburnia.pykix.org/
License: 	GPL
Group: 		System/Libraries
Source: 	http://libburnia-download.pykix.org/releases/%{name}-%{version}.tar.gz
Buildroot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: libburn-devel

%description
Libisofs is a library that handles creating ISO disc image files. It
is intended to work together with libburn to write these images to
discs.

%package -n	%{libname}
Group:		System/Libraries
Summary:	Library for creating ISO disc images

%description -n %{libname}
Libisofs is a library that handles creating ISO disc image files. It
is intended to work together with libburn to write these images to
discs.

%package -n %{develname}
Group:          Development/C
Summary:        Header files for development with %name
Provides:       %{name}-devel = %{version}
Requires:       %{libname} = %{version}

%description -n %{develname}
This package includes the header files for the %{name} package.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

# build documentation
doxygen doc/doxygen.conf

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{libname}
%defattr(-,root,root)
%doc README AUTHORS COPYING COPYRIGHT
%_libdir/libisofs.so.*

%files -n %{develname}
%defattr(-,root,root)
%_libdir/libisofs.so
%_libdir/libisofs.la
%_libdir/libisofs.a
%_libdir/pkgconfig/*.pc
%_includedir/%name/

