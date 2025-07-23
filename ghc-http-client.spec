#
# Conditional build:
%bcond_without	prof	# profiling library
#
%define		pkgname	http-client
Summary:	An HTTP client engine
Summary(pl.UTF-8):	Silnik klienta HTTP
Name:		ghc-%{pkgname}
Version:	0.7.0
Release:	2
License:	MIT
Group:		Development/Languages
#Source0Download: http://hackage.haskell.org/package/http-client
Source0:	http://hackage.haskell.org/package/%{pkgname}-%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	ad2dd8cc97e36f758f9207a5e4517a9e
URL:		http://hackage.haskell.org/package/http-client
BuildRequires:	ghc >= 8.2.1
BuildRequires:	ghc-array
BuildRequires:	ghc-base >= 4.10
BuildRequires:	ghc-base < 5
BuildRequires:	ghc-blaze-builder >= 0.3
BuildRequires:	ghc-bytestring >= 0.10
BuildRequires:	ghc-case-insensitive >= 1.0
BuildRequires:	ghc-containers >= 0.5
BuildRequires:	ghc-cookie
BuildRequires:	ghc-deepseq >= 1.3
BuildRequires:	ghc-deepseq < 1.5
BuildRequires:	ghc-exceptions >= 0.4
BuildRequires:	ghc-filepath
BuildRequires:	ghc-ghc-prim
BuildRequires:	ghc-http-types >= 0.8
BuildRequires:	ghc-memory >= 0.7
BuildRequires:	ghc-mime-types
BuildRequires:	ghc-network >= 2.6
BuildRequires:	ghc-network-uri >= 2.6
BuildRequires:	ghc-random
BuildRequires:	ghc-safe
BuildRequires:	ghc-stm >= 2.3
BuildRequires:	ghc-streaming-commons >= 0.1.0.2
BuildRequires:	ghc-streaming-commons < 0.3
BuildRequires:	ghc-text >= 0.11
BuildRequires:	ghc-time >= 1.2
BuildRequires:	ghc-transformers
%if %{with prof}
BuildRequires:	ghc-prof >= 8.2.1
BuildRequires:	ghc-array-prof
BuildRequires:	ghc-base-prof >= 4.10
BuildRequires:	ghc-blaze-builder-prof >= 0.3
BuildRequires:	ghc-bytestring-prof >= 0.10
BuildRequires:	ghc-case-insensitive-prof >= 1.0
BuildRequires:	ghc-containers-prof >= 0.5
BuildRequires:	ghc-cookie-prof
BuildRequires:	ghc-deepseq-prof >= 1.3
BuildRequires:	ghc-exceptions-prof >= 0.4
BuildRequires:	ghc-filepath-prof
BuildRequires:	ghc-ghc-prim-prof
BuildRequires:	ghc-http-types-prof >= 0.8
BuildRequires:	ghc-memory-prof >= 0.7
BuildRequires:	ghc-mime-types-prof
BuildRequires:	ghc-network-prof >= 2.6
BuildRequires:	ghc-network-uri-prof >= 2.6
BuildRequires:	ghc-random-prof
BuildRequires:	ghc-safe-prof
BuildRequires:	ghc-stm-prof >= 2.3
BuildRequires:	ghc-streaming-commons-prof >= 0.1.0.2
BuildRequires:	ghc-text-prof >= 0.11
BuildRequires:	ghc-time-prof >= 1.2
BuildRequires:	ghc-transformers-prof
%endif
BuildRequires:	rpmbuild(macros) >= 1.608
%requires_eq	ghc
Requires(post,postun):	/usr/bin/ghc-pkg
Requires:	ghc-array
Requires:	ghc-base >= 4.10
Requires:	ghc-blaze-builder >= 0.3
Requires:	ghc-bytestring >= 0.10
Requires:	ghc-case-insensitive >= 1.0
Requires:	ghc-containers >= 0.5
Requires:	ghc-cookie
Requires:	ghc-deepseq >= 1.3
Requires:	ghc-exceptions >= 0.4
Requires:	ghc-filepath
Requires:	ghc-ghc-prim
Requires:	ghc-http-types >= 0.8
Requires:	ghc-memory >= 0.7
Requires:	ghc-mime-types
Requires:	ghc-network >= 2.6
Requires:	ghc-network-uri >= 2.6
Requires:	ghc-random
Requires:	ghc-safe
Requires:	ghc-stm >= 2.3
Requires:	ghc-streaming-commons >= 0.1.0.2
Requires:	ghc-text >= 0.11
Requires:	ghc-time >= 1.2
Requires:	ghc-transformers
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# debuginfo is not useful for ghc
%define		_enable_debug_packages	0

# don't compress haddock files
%define		_noautocompressdoc	*.haddock

%description
An HTTP client engine, intended as a base layer for more user-friendly
packages.

%description -l pl.UTF-8
Silnik klienta HTTP, pomyślany jako warstwa bazowa dla pakietów
bardziej przyjaznych dla użytkownika.

%package prof
Summary:	Profiling %{pkgname} library for GHC
Summary(pl.UTF-8):	Biblioteka profilująca %{pkgname} dla GHC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ghc-array-prof
Requires:	ghc-base-prof >= 4.10
Requires:	ghc-blaze-builder-prof >= 0.3
Requires:	ghc-bytestring-prof >= 0.10
Requires:	ghc-case-insensitive-prof >= 1.0
Requires:	ghc-containers-prof >= 0.5
Requires:	ghc-cookie-prof
Requires:	ghc-deepseq-prof >= 1.3
Requires:	ghc-exceptions-prof >= 0.4
Requires:	ghc-filepath-prof
Requires:	ghc-ghc-prim-prof
Requires:	ghc-http-types-prof >= 0.8
Requires:	ghc-memory-prof >= 0.7
Requires:	ghc-mime-types-prof
Requires:	ghc-network-prof >= 2.6
Requires:	ghc-network-uri-prof >= 2.6
Requires:	ghc-random-prof
Requires:	ghc-safe-prof
Requires:	ghc-stm-prof >= 2.3
Requires:	ghc-streaming-commons-prof >= 0.1.0.2
Requires:	ghc-text-prof >= 0.11
Requires:	ghc-time-prof >= 1.2
Requires:	ghc-transformers-prof

%description prof
Profiling %{pkgname} library for GHC. Should be installed when GHC's
profiling subsystem is needed.

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
%attr(755,root,root) %{_libdir}/%{ghcdir}/%{pkgname}-%{version}/*.so
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
