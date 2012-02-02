%define major 6
%define libname %mklibname isofs %{major}
%define develname %mklibname isofs -d

Summary:	Library for creating ISO disc images
Name:		libisofs
Version:	1.2.0
Release:	1
License:	GPLv2+
Group:		System/Libraries
URL:		http://libburnia-project.org/wiki/Libisofs
Source0:	http://files.libburnia-project.org/releases/%{name}-%{version}.tar.gz
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	libburn-devel >= 1.1.4
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
This package includes the header files for the %{name} package.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

rm -f %{buildroot}/%{_libdir}/{*.la,*.a}

# build documentation
doxygen doc/doxygen.conf


%files -n %{libname}
%{_libdir}/libisofs.so.%{major}*

%files -n %{develname}
%doc README AUTHORS COPYRIGHT
%{_libdir}/libisofs.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}
