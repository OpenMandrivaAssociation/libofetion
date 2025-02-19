Summary: Fetion protocol library powered by ofetion project
Name: libofetion
Version: 2.2.0
Release: 2
Group: Networking/Instant messaging
License: GPLv2+
URL: https://code.google.com/p/ofetion/
Source0: http://ofetion.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: openssl-devel
BuildRequires: sqlite3-devel
BuildRequires: libxml2-devel
BuildRequires: cmake
Conflicts: openfetion < 2.1.0

%description
OpenFetion is a IM client based on GTK+2.0, using CHINA MOBILE's Fetion
Protocol Version 4.

%files
%defattr(-,root,root)
%{_datadir}/libofetion1

#---------------------------------------------------------------
%define major 1
%define libname %mklibname ofetion %major

%package -n %libname
Summary: Fetion protocol library powered by ofetion project
Group: Networking/Instant messaging
Requires: %name = %{version}

%description -n %libname
OpenFetion is a IM client based on GTK+2.0, using CHINA MOBILE's Fetion
Protocol Version 4.

%files -n %libname
%defattr(-,root,root)
%{_libdir}/libofetion.so.%{major}
%{_libdir}/libofetion.so.%{major}.*

#---------------------------------------------------------------
%define develname %mklibname -d ofetion

%package -n %develname
Summary: Fetion protocol library powered by ofetion project
Group: Development/C
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}-%{release}

%description -n %develname
OpenFetion is a IM client based on GTK+2.0, using CHINA MOBILE's Fetion
Protocol Version 4.

%files -n %develname
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/libofetion.so
%{_libdir}/libofetion.a
%{_libdir}/pkgconfig/*.pc

#---------------------------------------------------------------

%prep
%setup -qn %name-%version

%build
%cmake
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%clean
rm -rf $RPM_BUILD_ROOT


%changelog
* Sat May 14 2011 Funda Wang <fwang@mandriva.org> 2.2.0-1mdv2011.0
+ Revision: 674434
- new version 2.2.0

* Sun Dec 26 2010 Funda Wang <fwang@mandriva.org> 2.1.0-1mdv2011.0
+ Revision: 625215
- import libofetion

