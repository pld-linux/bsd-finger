Summary:	Finger client
Summary(de):	Finger-Client
Summary(es):	Cliente finger
Summary(fr):	Client finger
Summary(pl):	Klient finger
Summary(pt_BR):	Cliente finger
Summary(ru):	ëÌÉÅÎÔ finger
Summary(tr):	Finger istemcisi
Summary(uk):	ëÌ¦¤ÎÔ finger
Group:		Networking/Utilities
Name:		bsd-finger
Version:	0.17
Release:	11
License:	BSD
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
Obsoletes:	finger
Obsoletes:	finger-client
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Finger is a simple protocol which allows users to find information
about users on other machines. This package includes a standard finger
client.

%description -l de
Finger ist ein einfaches Protokoll, das Informationen über Benutzer
auf anderen Rechnern herausfindet. Dieses Paket enthält einen
standardmäßigen Finger-Client.

%description -l es
Finger es un protocolo sencillo que permite buscar información sobre
usuarios en otras máquinas. Este paquete incluye un cliente padrón
finger.

%description -l fr
finger est un protocole simple permettant de trouver des informations
sur les utilisateurs d'autres machines. Ce paquetage contient un
client finger standard.

%description -l pl
Finger jest prostym protoko³em, który umo¿liwia wyszukiwanie
informacji o u¿ytkownikach na innym serwerze. Pakiet ten zawiera
klienta fingera.

%description -l pt_BR
Finger é um protocolo simples que permite buscar informações sobre
usuários em outras máquinas. Este pacote inclui um cliente padrão
finger.

%description -l ru
Finger - ÜÔÏ ÕÔÉÌÉÔÁ, ÐÏÚ×ÏÌÑÀÝÁÑ ÐÏÌØÚÏ×ÁÔÅÌÑÍ ÐÏÌÕÞÁÔØ ÉÎÆÏÒÍÁÃÉÀ Ï
ÐÏÌØÚÏ×ÁÔÅÌÑÈ (ÌÏÇÉÎ, ÄÏÍÁÛÎÉÊ ËÁÔÁÌÏÇ, ÉÍÑ ÐÏÌØÚÏ×ÁÔÅÌÑ, ËÁË ÄÏÌÇÏ
ÏÎÉ ÎÁÈÏÄÑÔÓÑ × ÓÉÓÔÅÍÅ É ÐÒ.) ÎÁ ÍÁÛÉÎÁÈ, ÇÄÅ ÕÓÔÁÎÏ×ÌÅÎ ÓÅÒ×ÅÒ
finger. üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÓÔÁÎÄÁÒÔÎÙÊ ËÌÉÅÎÔ finger.

%description -l tr
finger, að baðlantýsý bulunan makinalarda çalýþan kullanýcýlar
hakkýnda kýsa bilgi veren bir hizmettir. Bu pakette standart bir
finger istemcisi bulunmaktadýr.

%description -l uk
Finger - ÃÅ ÕÔÉÌ¦ÔÁ, ÝÏ ÄÏÚ×ÏÌÑ¤ ËÏÒÉÓÔÕ×ÁÞÁÍ ÏÔÒÉÍÕ×ÁÔÉ ¦ÎÆÏÒÍÁÃ¦À
ÐÒÏ ËÏÒÉÓÔÕ×ÁÞ¦× (ÌÏÇ¦Î, ÄÏÍÁÛÎ¦Ê ËÁÔÁÌÏÇ, ¦Í'Ñ ËÏÒÉÓÔÕ×ÁÞÁ, ÑË ÄÏ×ÇÏ
×ÏÎÉ ÚÎÁÈÏÄÑÔØÓÑ × ÓÉÓÔÅÍ¦ ¦ Ô.Ð.) ÎÁ ÍÁÛÉÎÁÈ, ÄÅ ×ÓÔÁÎÏ×ÌÅÎÏ ÓÅÒ×ÅÒ
finger. ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÓÔÁÎÄÁÒÔÎÉÊ ËÌ¦¤ÎÔ finger.

%package -n bsd-fingerd
Summary:	Finger server
Summary(de):	Finger-Server
Summary(es):	El servidor finger
Summary(fr):	Server finger
Summary(pl):	Serwer finger
Summary(pt_BR):	O servidor finger
Summary(ru):	äÅÍÏÎ finger
Summary(tr):	Finger sunucusu
Summary(uk):	äÅÍÏÎ finger
Group:		Networking/Daemons
Prereq:		rc-inetd >= 0.8.1
Provides:	fingerd
Obsoletes:	fingerd
Obsoletes:	efingerd
Obsoletes:	ffingerd
Obsoletes:	cfingerd
Obsoletes:	finger-server

%description -n bsd-fingerd
Finger is a simple protocol which allows users to find information
about users on other machines. This package includes a standard finger
server.

%description -n bsd-fingerd -l de
Finger ist ein einfaches Protokoll, das Informationen über Benutzer
auf anderen Rechnern herausfindet. Dieses Paket enthält einen
standardmäßigen Finger-Server.

%description -n bsd-fingerd -l es
Finger es un protocolo sencillo que permite buscar información sobre
usuarios en otras máquinas. Este paquete incluye un servidor padrón
finger.

%description -n bsd-fingerd -l fr
finger est un protocole simple permettant de trouver des informations
sur les utilisateurs d'autres machines. Ce paquetage contient un
serveur finger standard.

%description -n bsd-fingerd -l pl
Finger jest prostym protoko³em, który umo¿liwia wyszukiwanie
informacji o u¿ytkownikach na innym serwerze. Pakiet ten zawiera
serwer fingera.

%description -n bsd-fingerd -l pt_BR
Finger é um protocolo simples que permite buscar informações sobre
usuários em outras máquinas. Este pacote inclui o servidor padrão
finger.

%description -n bsd-fingerd -l ru
ðÁËÅÔ finger-server ×ËÌÀÞÁÅÔ ÓÔÁÎÄÁÒÔÎÙÊ ÓÅÒ×ÅÒ finger.

%description -n bsd-fingerd -l tr
finger, að baðlantýsý bulunan makinalarda çalýþan kullanýcýlar
hakkýnda kýsa bilgi veren bir hizmettir. Bu pakette standart bir
finger sunucusu bulunmaktadýr.

%description -n bsd-fingerd -l uk
ðÁËÅÔ finger-server ×ËÌÀÞÁ¤ ÓÔÁÎÄÁÒÔÎÉÊ ÓÅÒ×ÅÒ finger.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
CC=%{__cc} \
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
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload 1>&2
else
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet server" 1>&2
fi

%postun -n bsd-fingerd
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload
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
