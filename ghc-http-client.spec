#
# Conditional build:
%bcond_without	prof	# profiling library
#
%define		pkgname	http-client
Summary:	An HTTP client engine
Name:		ghc-%{pkgname}
Version:	0.7.0
Release:	1
License:	MIT
Group:		Development/Languages
#Source0Download: http://hackage.haskell.org/package/http-client
Source0:	http://hackage.haskell.org/package/%{pkgname}-%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	ad2dd8cc97e36f758f9207a5e4517a9e
URL:		http://hackage.haskell.org/package/http-client
BuildRequires:	ghc >= 6.12.3
BuildRequires:	ghc-cookie
BuildRequires:	ghc-filepath
BuildRequires:	ghc-http-types >= 0.8)
BuildRequires:	ghc-memory >= 0.7
BuildRequires:	ghc-mime-types
BuildRequires:	ghc-network >= 2.4
BuildRequires:	ghc-network-uri >= 2.6
BuildRequires:	ghc-random
BuildRequires:	ghc-safe
BuildRequires:	ghc-semigroups >= 0.16.1
BuildRequires:	ghc-streaming-commons >= 0.1.0.2
%if %{with prof}
BuildRequires:	ghc-prof
BuildRequires:	ghc-cookie-prof
BuildRequires:	ghc-filepath-prof
BuildRequires:	ghc-http-types-prof >= 0.8)
BuildRequires:	ghc-memory-prof >= 0.7
BuildRequires:	ghc-mime-types-prof
BuildRequires:	ghc-network-prof >= 2.4
BuildRequires:	ghc-network-uri-prof >= 2.6
BuildRequires:	ghc-random-prof
BuildRequires:	ghc-safe-prof
BuildRequires:	ghc-semigroups-prof >= 0.16.1
BuildRequires:	ghc-streaming-commons-prof >= 0.1.0.2
%endif
BuildRequires:	rpmbuild(macros) >= 1.608
%requires_eq	ghc
Requires(post,postun):	/usr/bin/ghc-pkg
Requires:	ghc-cookie
Requires:	ghc-filepath
Requires:	ghc-http-types >= 0.8)
Requires:	ghc-memory >= 0.7
Requires:	ghc-mime-types
Requires:	ghc-network >= 2.4
Requires:	ghc-network-uri >= 2.6
Requires:	ghc-random
Requires:	ghc-safe
Requires:	ghc-semigroups >= 0.16.1
Requires:	ghc-streaming-commons >= 0.1.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# debuginfo is not useful for ghc
%define		_enable_debug_packages	0

# don't compress haddock files
%define		_noautocompressdoc	*.haddock

%description
An HTTP client engine, intended as a base layer for more user-friendly
packages.

%package prof
Summary:	Profiling %{pkgname} library for GHC
Summary(pl.UTF-8):	Biblioteka profilująca %{pkgname} dla GHC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ghc-cookie-prof
Requires:	ghc-filepath-prof
Requires:	ghc-http-types-prof >= 0.8)
Requires:	ghc-memory-prof >= 0.7
Requires:	ghc-mime-types-prof
Requires:	ghc-network-prof >= 2.4
Requires:	ghc-network-uri-prof >= 2.6
Requires:	ghc-random-prof
Requires:	ghc-safe-prof
Requires:	ghc-semigroups-prof >= 0.16.1
Requires:	ghc-streaming-commons-prof >= 0.1.0.2

%description prof
Profiling %{pkgname} library for GHC.  Should be installed when
GHC's profiling subsystem is needed.

%description prof -l pl.UTF-8
Biblioteka profilująca %{pkgname} dla GHC. Powinna być zainstalowana
kiedy potrzebujemy systemu profilującego z GHC.

%prep
%setup -q -n %{pkgname}-%{version}

%build
runhaskell Setup.hs configure -v2 \
	%{?with_prof:--enable-library-profiling} \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libexecdir} \
	--docdir=%{_docdir}/%{name}-%{version}

runhaskell Setup.hs build
runhaskell Setup.hs haddock --executables

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/%{ghcdir}/package.conf.d

runhaskell Setup.hs copy --destdir=$RPM_BUILD_ROOT

# work around automatic haddock docs installation
%{__rm} -rf %{name}-%{version}-doc
cp -a $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} %{name}-%{version}-doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

runhaskell Setup.hs register \
	--gen-pkg-config=$RPM_BUILD_ROOT%{_libdir}/%{ghcdir}/package.conf.d/%{pkgname}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%ghc_pkg_recache

%postun
%ghc_pkg_recache

%files
%defattr(644,root,root,755)
%doc ChangeLog.md README.md %{name}-%{version}-doc/*
%{_libdir}/%{ghcdir}/package.conf.d/%{pkgname}.conf
%dir %{_libdir}/%{ghcdir}/%{pkgname}-%{version}
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/*.so
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/*.a
%exclude %{_libdir}/%{ghcdir}/%{pkgname}-%{version}/*_p.a

%dir %{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/*.hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/*.dyn_hi
%dir %{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Network
%dir %{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Network/HTTP
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Network/HTTP/*.hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Network/HTTP/*.dyn_hi
%dir %{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Network/HTTP/Client
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Network/HTTP/Client/*.hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Network/HTTP/Client/*.dyn_hi
%dir %{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Network//PublicSuffixList
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Network/PublicSuffixList/*.hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Network/PublicSuffixList/*.dyn_hi

%if %{with prof}
%files prof
%defattr(644,root,root,755)
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/*_p.a
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/*.p_hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Network/HTTP/*.p_hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Network/HTTP/Client/*.p_hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Network/PublicSuffixList/*.p_hi
%endif
