Summary:	XMMS plugin for playing Amiga audio modules
Summary(pl):	Wtyczka dla XMMS odtwarzaj�ca modu�y muzyczne z Amigi
Name:		xmms-input-modplug
Version:	2.04
Release:	2
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/modplug-xmms/modplugxmms-%{version}.tar.gz
# Source0-md5:	fe3671391dc65703357db9ad147744ef
URL:		http://modplug-xmms.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
Requires:	xmms
Obsoletes:	xmms-input-mikmod
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugin for playing Amiga audio modules. It is MUCH better than mikmod
plugin. It has no problems playing many modules which are beyond
abilities of mikmod plugin. It also has many advanced options
increasing sound quality, such as noise reductions, bass boost and
surround sound.

%description -l pl
Wtyczka umo�liwiaj�ca odtwarzanie modu��w muzycznych z Amigi. Jest
ZNACZNIE lepsza od wtyczki mikmod. Nie ma problem�w z odtwarzaniem
wielu modu��w z kt�rymi wtyczka mikmod zupe�nie sobie nie radzi.
Posiada ona r�wnie� wiele zaawansowanych opcji poprawiaj�cych jako��
d�wi�ku, jak cho�by redukcja szum�w, wzmocnienie bas�w czy d�wi�k
przestrzenny.

%prep
%setup -q -n modplugxmms-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README TODO ChangeLog AUTHORS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{xmms_input_plugindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_libdir}/lib*.la
%{_includedir}/modplug.h
