Summary:	A utility for improving the appearance of terminals
Summary(es):	Utilitario para configuraciСn avanzada de los modos de vМdeo da consola
Summary(pl):	NarzЙdzie do polepszania wygl╠du terminali
Summary(pt_BR):	UtilitАrio para configuraГЦo avanГada dos modos de vМdeo da console
Summary(ru):	Утилита для улучшения внешнего вида текстовых консолей
Summary(uk):	Утил╕та для покращення зовн╕шнього вигляду текстових консолей
Name:		SVGATextMode
Version:	1.10
Release:	12
License:	GPL
Group:		Applications/System
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/console/%{name}-%{version}-src.tar.gz
Patch0:		%{name}-conf.patch
Patch1:		%{name}-make.patch
Patch2:		%{name}-cache.patch
Patch3:		%{name}-stmmenu.patch
Patch4:		%{name}-set80.patch
Patch5:		%{name}-Makefile-gcc.patch
Patch6:		%{name}-cfgfile.y.patch
Patch7:		%{name}-GeForce.patch
Patch8:		%{name}-alpha.patch
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

%description -l es
SVGATextMode permite que el modo de la pantalla de la consola del
Linux sea controlada detalladamente. Esto permite que mАs caracteres
sean mostrados en la pantalla, mАs textos estables, menos caracteres
en la pantalla, menos textos estables, etc. En un hardware con
proyecto malo podrАs acabar con un monitor derretido. Son necesarias
fuentes extras para que funcione correctamente, pero mismo sin ellas
se pueden obtener efectos Зtiles.

%description -l pl
SVGATextMode jest narzЙdziem sЁu©╠cym do konfiguracji sprzЙtu (S)VGA,
ktСre pozwala na polepszenie wygl╠du terminali. Wykorzystuje plik
konfiguracyjny (Xconfig lub XF86Config) aby ustawiaФ wy©sze
rozdzielczo╤ci, wiЙksze fonty, wy©sze czЙstotliwo╤ci od╤wie©ania itp.

%description -l pt_BR
O SVGATextMode permite que o modo da tela do console do Linux seja
controlado detalhadamente. Isto permite que mais caracteres sejam
mostrados na tela, mais textos estАveis, menos caracteres na tela,
menos textos estАveis, etc. Em hardware com projeto ruim voce poderА
obter um monitor derretido.

Fontes extras sЦo necessАrias para que o mesmo funcione corretamente,
mas mesmo sem elas efeitos Зteis podem ser obtidos.

%description -l ru
SVGATextMode - это утилита для перепрограмирования аппаратуры (S)VGA с
целью улучшения внешнего вида текстовых консолей. SVGATextMode
использует конфигурационный файл (по умолчанию /etc/TextConfig) с
синтаксисом, похожим на конфигурационный файл X Window System (Xconfig
или XF86Config) для настройки текстовых режимов с более высоким
разрешением, большими размерами шрифтов, большей частотой обновления
экрана и т.п. Теоретически, SVGATextMode может быть использована для
программирования любого размера в текстовом режиме, но практически
результат зависит от используемой видеокарты.

%description -l uk
SVGATextMode - це утил╕та для перепрограмування апаратури (S)VGA з
метою покращення зовн╕шнього вигляду текстових консолей. SVGATextMode
використову╓ конф╕гурац╕йний файл (стандартно /etc/TextConfig) з
синтаксисом, схожим на конф╕гурац╕йний файл X Window System (Xconfig
або XF86Config) для налагодження текстових режим╕в з б╕льшою
розд╕льною здатн╕стю, б╕льшими розм╕рами шрифт╕в, б╕льшою частотою
поновлення екрану ╕ т.╕. Теоретично, SVGATextMode може бути
використана для програмування будь-якого розм╕ру у текстовому режим╕,
але практично результат залежить в╕д використано╖ в╕деокарти.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0
%patch5 -p1
%patch6 -p1
%patch7 -p1
%ifarch alpha
%patch8 -p1
ln -sf ../../asm XFREE/include
%endif

%build
%{__make} dep CC="%{__cc}"
%{__make} all CC="%{__cc}" ARCH="%{_target_cpu}" \
CFLAGS_DEFAULT="%{rpmcflags}" LDFLAGS_DEFAULT="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_sbindir},%{_mandir}/man{5,8}}

%{__make} DESTDIR=$RPM_BUILD_ROOT newinstall man-install
install STMmenu $RPM_BUILD_ROOT%{_sbindir}/stm-menu
install contrib/scripts/STM_reset $RPM_BUILD_ROOT%{_sbindir}

rm -f $RPM_BUILD_ROOT%{_mandir}/man8/{stm,clockprobe}.8
echo ".so SVGATextMode.8" > $RPM_BUILD_ROOT%{_mandir}/man8/stm.8
echo ".so grabmode.8" > $RPM_BUILD_ROOT%{_mandir}/man8/clockprobe.8

ln -sf grabmode_pixmux.gz doc/grabmode_hi_truecolor

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* README README.FIRST CREDITS HISTORY TODO
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/TextConfig
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man*/*
