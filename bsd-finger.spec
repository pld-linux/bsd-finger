Summary:	Finger client
Summary(de.UTF-8):	Finger-Client
Summary(es.UTF-8):	Cliente finger
Summary(fr.UTF-8):	Client finger
Summary(pl.UTF-8):	Klient finger
Summary(pt_BR.UTF-8):	Cliente finger
Summary(ru.UTF-8):	Клиент finger
Summary(tr.UTF-8):	Finger istemcisi
Summary(uk.UTF-8):	Клієнт finger
Name:		bsd-finger
Version:	0.17
Release:	15
License:	BSD
Group:		Networking/Utilities
Source0:	ftp://ftp.linux.org.uk/pub/linux/Networking/netkit/%{name}-%{version}.tar.gz
# Source0-md5:	52bf281aac8814bf56cdc92f7661ee75
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	404d52f992378fbc9b2378b8f21f3727
Source2:	fingerd.inetd
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-exact.patch
# http://www.t17.ds.pwr.wroc.pl/~misiek/ipv6/
Patch2:		%{name}-0.16-20000912.patch.gz
Patch3:		%{name}-time.patch
Patch4:		%{name}-gecos.patch
Patch5:		%{name}-rfc742.patch
Patch6:		%{name}-typo.patch
Patch7:		%{name}-wide-char-support5.patch
Patch8:		%{name}-iconv.patch
BuildRequires:	rpmbuild(macros) >= 1.268
Obsoletes:	finger
Obsoletes:	finger-client
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Finger is a simple protocol which allows users to find information
about users on other machines. This package includes a standard finger
client.

%description -l de.UTF-8
Finger ist ein einfaches Protokoll, das Informationen über Benutzer
auf anderen Rechnern herausfindet. Dieses Paket enthält einen
standardmäßigen Finger-Client.

%description -l es.UTF-8
Finger es un protocolo sencillo que permite buscar información sobre
usuarios en otras máquinas. Este paquete incluye un cliente padrón
finger.

%description -l fr.UTF-8
finger est un protocole simple permettant de trouver des informations
sur les utilisateurs d'autres machines. Ce paquetage contient un
client finger standard.

%description -l pl.UTF-8
Finger jest prostym protokołem, który umożliwia wyszukiwanie
informacji o użytkownikach na innym serwerze. Pakiet ten zawiera
klienta fingera.

%description -l pt_BR.UTF-8
Finger é um protocolo simples que permite buscar informações sobre
usuários em outras máquinas. Este pacote inclui um cliente padrão
finger.

%description -l ru.UTF-8
Finger - это утилита, позволяющая пользователям получать информацию о
пользователях (логин, домашний каталог, имя пользователя, как долго
они находятся в системе и пр.) на машинах, где установлен сервер
finger. Этот пакет содержит стандартный клиент finger.

%description -l tr.UTF-8
finger, ağ bağlantısı bulunan makinalarda çalışan kullanıcılar
hakkında kısa bilgi veren bir hizmettir. Bu pakette standart bir
finger istemcisi bulunmaktadır.

%description -l uk.UTF-8
Finger - це утиліта, що дозволяє користувачам отримувати інформацію
про користувачів (логін, домашній каталог, ім'я користувача, як довго
вони знаходяться в системі і т.п.) на машинах, де встановлено сервер
finger. Цей пакет містить стандартний клієнт finger.

%package -n bsd-fingerd
Summary:	Finger server
Summary(de.UTF-8):	Finger-Server
Summary(es.UTF-8):	El servidor finger
Summary(fr.UTF-8):	Server finger
Summary(pl.UTF-8):	Serwer finger
Summary(pt_BR.UTF-8):	O servidor finger
Summary(ru.UTF-8):	Демон finger
Summary(tr.UTF-8):	Finger sunucusu
Summary(uk.UTF-8):	Демон finger
Group:		Networking/Daemons
Requires:	rc-inetd >= 0.8.1
Provides:	fingerd
Obsoletes:	cfingerd
Obsoletes:	efingerd
Obsoletes:	ffingerd
Obsoletes:	finger-server
Obsoletes:	fingerd

%description -n bsd-fingerd
Finger is a simple protocol which allows users to find information
about users on other machines. This package includes a standard finger
server.

%description -n bsd-fingerd -l de.UTF-8
Finger ist ein einfaches Protokoll, das Informationen über Benutzer
auf anderen Rechnern herausfindet. Dieses Paket enthält einen
standardmäßigen Finger-Server.

%description -n bsd-fingerd -l es.UTF-8
Finger es un protocolo sencillo que permite buscar información sobre
usuarios en otras máquinas. Este paquete incluye un servidor padrón
finger.

%description -n bsd-fingerd -l fr.UTF-8
finger est un protocole simple permettant de trouver des informations
sur les utilisateurs d'autres machines. Ce paquetage contient un
serveur finger standard.

%description -n bsd-fingerd -l pl.UTF-8
Finger jest prostym protokołem, który umożliwia wyszukiwanie
informacji o użytkownikach na innym serwerze. Pakiet ten zawiera
serwer fingera.

%description -n bsd-fingerd -l pt_BR.UTF-8
Finger é um protocolo simples que permite buscar informações sobre
usuários em outras máquinas. Este pacote inclui o servidor padrão
finger.

%description -n bsd-fingerd -l ru.UTF-8
Пакет finger-server включает стандартный сервер finger.

%description -n bsd-fingerd -l tr.UTF-8
finger, ağ bağlantısı bulunan makinalarda çalışan kullanıcılar
hakkında kısa bilgi veren bir hizmettir. Bu pakette standart bir
finger sunucusu bulunmaktadır.

%description -n bsd-fingerd -l uk.UTF-8
Пакет finger-server включає стандартний сервер finger.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
CC="%{__cc}" \
./configure \
	--installroot=$RPM_BUILD_ROOT \
	--prefix=%{_prefix}

%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/{man{1,8},pl/man1}} \
	$RPM_BUILD_ROOT/etc/sysconfig/rc-inetd

%{__make} MANDIR=%{_mandir} install

mv -f $RPM_BUILD_ROOT%{_sbindir}/in.fingerd \
	$RPM_BUILD_ROOT%{_sbindir}/fingerd
mv -f $RPM_BUILD_ROOT%{_mandir}/man8/in.fingerd.8 \
	$RPM_BUILD_ROOT%{_mandir}/man8/fingerd.8

install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/fingerd

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n bsd-fingerd
%service -q rc-inetd reload

%postun -n bsd-fingerd
if [ "$1" = 0 ]; then
	%service -q rc-inetd reload
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(fi) %{_mandir}/fi/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(pl) %{_mandir}/pl/man1/*

%files -n bsd-fingerd
%defattr(644,root,root,755)
%doc README BUGS
%attr(755,root,root) %{_sbindir}/*
%attr(640,root,root) /etc/sysconfig/rc-inetd/fingerd
%{_mandir}/man8/*
