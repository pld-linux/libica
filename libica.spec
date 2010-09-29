Summary:	Interface library to the ICA device driver
Summary(pl.UTF-8):	Biblioteka interfejsu do sterownika urządzenia ICA
Name:		libica
Version:	1.3.9.1
Release:	1
License:	CPL v0.5
Group:		Libraries
Source0:	http://downloads.sourceforge.net/opencryptoki/%{name}-%{version}.tar.bz2
# Source0-md5:	fa82b4cb4549c3d3f567fb89b18fbeff
Patch0:		%{name}-headers.patch
Patch1:		%{name}-fixes.patch
URL:		http://opencryptoki.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9.5
BuildRequires:	libtool
%ifarch s390 s390x
BuildRequires:	openssl-devel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Interface library routines used by IBM modules to interface to the IBM
eServer Cryptographic Accelerator (ICA).

%description -l pl.UTF-8
Biblioteka interfejsu używana przez moduły IBM-a do współpracy z
akceleratorem kryptograficznym IBM eServer Cryptographic Accelerator
(ICA).

%package devel
Summary:	Header files for ICA library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ICA
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%ifarch s390 s390x
Requires:	openssl-devel
%endif

%description devel
Header files for ICA library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ICA.

%package static
Summary:	Static ICA library
Summary(pl.UTF-8):	Statyczna biblioteka ICA
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ICA library.

%description static -l pl.UTF-8
Statyczna biblioteka ICA.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	CPPFLAGS=-I$(pwd)/include
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_bindir}/icainfo
%attr(755,root,root) %{_libdir}/libica-*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libica.so
%{_libdir}/libica.la
%{_includedir}/ica_api.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libica.a
