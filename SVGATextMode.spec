Summary:	A utility for improving the appearance of terminals
Summary(pl):	Narzêdzie do polepszania wygl±du terminali
Name:		SVGATextMode
Version:	1.10
Release:	5
License:	GPL
Group:		Applications/System
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/console/%{name}-%{version}-src.tar.gz
Patch0:		%{name}-conf.patch
Patch1:		%{name}-make.patch
Patch2:		%{name}-cache.patch
Patch3:		%{name}-stmmenu.patch
Patch4:		%{name}-set80.patch
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	util-linux
Requires:	dialog
Requires:	kbd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86} alpha

%description
SVGATextMode is a utility for reprogramming (S)VGA hardware, which can
improve the appearance of terminals. You should install SVGATextMode
if you want to alter the appearance of your terminal. The utility uses
a configuration file (Xconfig or XF86Config) to set up textmodes with
higher resolution, larger fonts, higher display refresh rates, etc.

Although SVGATextMode can be used to program any text mode size, your
results will depend on your VGA card.

%description -l pl
SVGATextMode jest narzêdziem s³u¿±cym do konfiguracji sprzêtu (S)VGA,
które pozwala na polepszenie wygl±du terminali. Wykorzystuje plik
konfiguracyjny (Xconfig lub XF86Config) aby ustawiaæ wy¿sze
rozdzielczo¶ci, wiêksze fonty, wy¿sze czêstotliwo¶ci od¶wie¿ania itp.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__make} dep
%{__make} all CFLAGS_DEFAULT="%{rpmcflags}" LDFLAGS_DEFAULT="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_sbindir},%{_mandir}/man{5,8}}

%{__make} DESTDIR=$RPM_BUILD_ROOT newinstall man-install
install STMmenu $RPM_BUILD_ROOT%{_sbindir}/stm-menu
install contrib/scripts/STM_reset $RPM_BUILD_ROOT%{_sbindir}

rm -f $RPM_BUILD_ROOT%{_mandir}/man8/{stm,clockprobe}.8
echo ".so man8/SVGATextMode.8" > $RPM_BUILD_ROOT%{_mandir}/man8/stm.8
echo ".so man8/grabmode.8" > $RPM_BUILD_ROOT%{_mandir}/man8/clockprobe.8

gzip -9nf doc/* README README.FIRST CREDITS HISTORY TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/TextConfig
%attr(755,root,root) %{_sbindir}/*
%attr(644,root,root) %{_mandir}/man*/*
