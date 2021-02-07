%define major 6
%define libname %mklibname isofs %{major}
%define devname %mklibname isofs -d
%define beta rc1

Summary:	Library for creating ISO disc images
Name:		libisofs
Version:	1.5.4
Release:	%{?beta:0.%{beta}.}2
License:	GPLv2+
Group:		System/Libraries
Url:		http://libburnia-project.org/wiki/Libisofs
Source0:	https://dev.lovelyhq.com/libburnia/libisofs/archive/release-%{version}%{?beta:.%{beta}}.tar.gz
# From https://www.gnu.org/software/xorriso/ 's internal copy of libisofs
Patch0:		xorriso-1.5.4-1.5.4.pl02.patch
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
%autosetup -p1 -n %{name}
%configure

%build
%make_build

%install
%make_install

# build documentation
doxygen doc/doxygen.conf

%files -n %{libname}
%{_libdir}/libisofs.so.%{major}*

%files -n %{devname}
%doc README AUTHORS COPYRIGHT
%{_libdir}/libisofs.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}
