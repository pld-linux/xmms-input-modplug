Summary:	XMMS plugin for playing Amiga audio modules
Summary(pl):	Wtyczka dla XMMS odtwarzaj±ca modu³y muzyczne z Amigi
Name:		xmms-input-modplug
Version:	2.05
Release:	1
# uhm, code is in Public Domain, but xmms forces GPL
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/modplug-xmms/modplugxmms-%{version}.tar.gz
# Source0-md5:	2dd9b88a02978d3001b48863b8cffc5b
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
BuildRequires:	libmodplug >= 0.7
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
Wtyczka umo¿liwiaj±ca odtwarzanie modu³ów muzycznych z Amigi. Jest
ZNACZNIE lepsza od wtyczki mikmod. Nie ma problemów z odtwarzaniem
wielu modu³ów z którymi wtyczka mikmod zupe³nie sobie nie radzi.
Posiada ona równie¿ wiele zaawansowanych opcji poprawiaj±cych jako¶æ
d¼wiêku, jak choæby redukcja szumów, wzmocnienie basów czy d¼wiêk
przestrzenny.

%prep
%setup -q -n modplugxmms-%{version}

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

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
# this is standalone player - to be separated?
%attr(755,root,root) %{_bindir}/modplugplay
%attr(755,root,root) %{xmms_input_plugindir}/*.so
