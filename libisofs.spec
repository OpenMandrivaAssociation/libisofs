%define name    libisofs
# We ship only one app which
# actually uses libisofs - brasero. Brasero 0.6.0 does not work with
# libisofs versions beyond 0.2.8. Do NOT update this package past
# 0.2.8 unless you are 100% sure a version of Brasero which works
# with the newer version of this package is available, and you are
# also going to update Brasero. -AdamW 2007/08
%define version 0.2.8
%define rel 	1

%define major 	5
%define libname %mklibname isofs %major
%define develname %mklibname isofs -d

Summary: 	Library for creating ISO disc images
Name: 		%name
Version: 	%version
Release: 	%mkrel %rel
Url: 		http://libburnia.pykix.org/
License: 	GPLv2+
Group: 		System/Libraries
Source: 	http://libburnia-download.pykix.org/releases/%{name}-%{version}.tar.gz
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	libburn-devel

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
%doc README AUTHORS COPYRIGHT
%_libdir/libisofs.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%_libdir/libisofs.so
%_libdir/libisofs.la
%_libdir/libisofs.a
%_libdir/pkgconfig/*.pc
%_includedir/%name/

