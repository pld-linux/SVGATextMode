Summary:	A utility for improving the appearance of text consoles.
Name:		SVGATextMode
Version:	1.9
Release:	2
Copyright:	GPL
Group:		Applications/System
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/console/%{name}-%{version}-src.tar.gz 
Source1:	%{name}.init
Patch0:		SVGATextMode-src-conf.patch
Patch1:		SVGATextMode-src-agp.patch
Patch2:		SVGATextMode-src-make.patch
Prereq:		/sbin/chkconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86} alpha

%description
SVGATextMode is a utility for reprogramming (S)VGA hardware,
which can improve the appearance of text consoles.
You should install SVGATextMode if you want to alter the
appearance of your text consoles. The utility uses a 
configuration file (Xconfig or XF86Config) to set up 
textmodes with higher resolution, larger fonts, higher 
display refresh rates, etc.

Although SVGATextMode can be used to program any text
mode size, your results will depend on your VGA card.

%description -l pl
SVGATextMode jest narzêdziem s³u¿±cym konfiguracji sprzêtu
(S)VGA, które pozwala na polepszenie wygl±du konsoli tekstowej.
To narzêdzie wykorzystuje plik konfiguracyjny by ustawiaæ
wy¿sze rozdzielczo¶ci, wiêksze fonty, wy¿sze czêstotliwo¶ci
od¶wierzania itp.

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1 -b .conf
%patch1 -p1 -b .agp
%patch2 -p1 -b .make

%build
make dep
make all

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/rc.d/init.d
install -d $RPM_BUILD_ROOT%{_sbindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man{5,8}

make	DESTDIR=$RPM_BUILD_ROOT newinstall man-install
install -m 0755 STMmenu $RPM_BUILD_ROOT%{_sbindir}/stm-menu
install	%{SOURCE1}	$RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}

rm	   $RPM_BUILD_ROOT%{_mandir}/man8/stm.8
echo ".so SVGATextMode.8" > $RPM_BUILD_ROOT%{_mandir}/man8/stm.8
strip	   $RPM_BUILD_ROOT%{_sbindir}/* || :
gzip -9nf  $RPM_BUILD_ROOT%{_mandir}/man*/* doc/* README
gzip -9nf  README.FIRST CREDITS COPYING HISTORY TODO

%clean 
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add %{name} 2>/dev/null

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del %{name} 2>/dev/null
fi

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) /etc/TextConfig
%doc {README,README.FIRST,CREDITS,COPYING,HISTORY,TODO}.gz
%doc doc/*
%attr(755,root,root) %{_sbindir}/*
%attr(644,root,root) %{_mandir}/man*/*
%attr(754,root,root) /etc/rc.d/init.d/%{name}
