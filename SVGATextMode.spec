Summary:	A utility for improving the appearance of text consoles.
Name:		SVGATextMode
Version:	1.10
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/console/%{name}-%{version}-src.tar.gz
Patch0:		%{name}-conf.patch
Patch1:		%{name}-make.patch
Patch2:		%{name}-cache.patch
Patch3:		%{name}-stmmenu.patch
BuildRequires:	bison
Requires:	console-tools
Requires:	dialog
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86} alpha

%description
SVGATextMode is a utility for reprogramming (S)VGA hardware, which can
improve the appearance of text consoles. You should install
SVGATextMode if you want to alter the appearance of your text
consoles. The utility uses a configuration file (Xconfig or
XF86Config) to set up textmodes with higher resolution, larger fonts,
higher display refresh rates, etc.

Although SVGATextMode can be used to program any text mode size, your
results will depend on your VGA card.

%description -l pl
SVGATextMode jest narzêdziem s³u¿±cym konfiguracji sprzêtu (S)VGA,
które pozwala na polepszenie wygl±du konsoli tekstowej. To narzêdzie
wykorzystuje plik konfiguracyjny by ustawiaæ wy¿sze rozdzielczo¶ci,
wiêksze fonty, wy¿sze czêstotliwo¶ci od¶wie¿ania itp.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__make} dep
%{__make} all \
	CFLAGS_DEFAULT="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g}" \
	LDFLAGS_DEFAULT="%{!?debug:-s}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man{5,8}}

%{__make} DESTDIR=$RPM_BUILD_ROOT newinstall man-install
install STMmenu $RPM_BUILD_ROOT%{_sbindir}/stm-menu

rm -f $RPM_BUILD_ROOT%{_mandir}/man8/stm.8
echo ".so SVGATextMode.8" > $RPM_BUILD_ROOT%{_mandir}/man8/stm.8

gzip -9nf doc/* README README.FIRST CREDITS COPYING HISTORY TODO

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/TextConfig
%attr(755,root,root) %{_sbindir}/*
%attr(644,root,root) %{_mandir}/man*/*
