%define major		6
%define libname		%mklibname isofs %major
%define develname	%mklibname isofs -d

Summary: 	Library for creating ISO disc images
Name: 		libisofs
Version: 	0.6.6
Release: 	%mkrel 1
URL: 		http://libburnia-project.org/
License: 	GPLv2+
Group: 		System/Libraries
Source0: 	http://files.libburnia-project.org/releases/%{name}-%{version}.tar.gz
Buildroot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
rm -rf %{buildroot}

%makeinstall

# build documentation
doxygen doc/doxygen.conf

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libisofs.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc README AUTHORS COPYRIGHT
%{_libdir}/libisofs.so
%{_libdir}/libisofs.la
%{_libdir}/libisofs.a
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}

