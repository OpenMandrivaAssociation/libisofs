%define major	6
%define libname	%mklibname isofs %{major}
%define devname	%mklibname isofs -d

Summary:	Library for creating ISO disc images
Name:		libisofs
Version:	1.3.0
Release:	3
License:	GPLv2+
Group:		System/Libraries
Url:		http://libburnia-project.org/wiki/Libisofs
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

%package -n %{devname}
Summary:	Header files for development with %{name}
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
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

%files -n %{devname}
%doc README AUTHORS COPYRIGHT
%{_libdir}/libisofs.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}

