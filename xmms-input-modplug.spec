Summary:	XMMS plugin for playing Amiga audio modules
Summary(pl):	Wtyczka dla XMMS odtwarzaj�ca modu�y muzyczne z Amigi
Name:		xmms-input-modplug
Version:	1.5a
Release:	2
License:	GPL
Group:		Development/Libraries
URL:		http://modplug-xmms.sourceforge.net/
Source0:	http://download.sourceforge.net/modplug-xmms/modplugxmms-%{version}.tar.gz
Requires:	xmms
Obsoletes:	xmms-input-mikmod
BuildRequires:	libstdc++-devel
BuildRequires:	xmms-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Plugin for playing Amiga audio modules. It is MUCH better than mikmod
plugin. It has no problems playing many modules wich are beyond
abilities of mikmod plugin. It also has many advanced options
incrasing sound quality, such as noise reductions, bass bust and
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

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip README TODO ChangeLog AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Input/*
%doc *.gz
