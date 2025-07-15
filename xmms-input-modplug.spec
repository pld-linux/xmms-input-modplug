Summary:	XMMS plugin for playing Amiga audio modules
Summary(pl.UTF-8):	Wtyczka wejściowa dla XMMS-a odtwarzająca moduły muzyczne z Amigi
Name:		xmms-input-modplug
Version:	2.05
Release:	4
# uhm, code is in Public Domain, but xmms forces GPL
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/modplug-xmms/modplugxmms-%{version}.tar.gz
# Source0-md5:	2dd9b88a02978d3001b48863b8cffc5b
Patch0:		%{name}-aclocal.patch
Patch1:		%{name}-build.patch
URL:		http://modplug-xmms.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libmodplug-devel >= 0.7
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.0.0
Requires:	libmodplug >= 0.7
Obsoletes:	xmms-input-mikmod
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugin for playing Amiga audio modules. It is MUCH better than mikmod
plugin. It has no problems playing many modules which are beyond
abilities of mikmod plugin. It also has many advanced options
increasing sound quality, such as noise reductions, bass boost and
surround sound.

%description -l pl.UTF-8
Wtyczka umożliwiająca odtwarzanie modułów muzycznych z Amigi. Jest
ZNACZNIE lepsza od wtyczki mikmod. Nie ma problemów z odtwarzaniem
wielu modułów z którymi wtyczka mikmod zupełnie sobie nie radzi.
Posiada ona również wiele zaawansowanych opcji poprawiających jakość
dźwięku, jak choćby redukcja szumów, wzmocnienie basów czy dźwięk
przestrzenny.

%prep
%setup -q -n modplugxmms-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{xmms_input_plugindir}/*.la

# newer version in modplugtools
%{__rm} $RPM_BUILD_ROOT%{_bindir}/modplugplay

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{xmms_input_plugindir}/*.so
