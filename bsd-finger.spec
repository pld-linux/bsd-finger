Summary:	Finger server
Summary(de):	Finger-Server 
Summary(fr):	Server finger
Summary(pl):	Serwer finger
Summary(tr):	Finger sunucusu
Name:		finger
Version:	0.10
Release:	26
Copyright:	BSD
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Source:		ftp://sunsite.unc.edu/pub/Linux/system/network/finger/bsd-%{name}-%{version}.tar.gz
Source1:	finger.1.pl
Source2:	fingerd.inetd
Patch0:		bsd-finger-misc.patch
Patch1:		bsd-finger-security.patch
Patch2:		bsd-finger-nobr.patch
Patch3:		bsd-finger-ipv6.patch
Patch4:		bsd-finger-maint.patch
Patch5:		bsd-finger-timeout.patch
Patch6:		bsd-finger-pts.patch
Patch7:		bsd-finger-exact.patch
Prereq:		rc-inetd
Provides:	fingerd
Obsoletes:	fingerd
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Finger is a simple protocol which allows users to find information about
users on other machines. This package includes a standard finger server. 

%description -l de
Finger ist ein einfaches Protokoll, das Informationen �ber Benutzer 
auf anderen Rechnern herausfindet. Dieses Paket enth�lt einen 
standardm��igen Finger-Server.

%description -l fr
finger est un protocole simple permettant de trouver des informations sur
les utilisateurs d'autres machines. Ce paquetage contient un serveur finger
standard.

%description -l pl
Finger jest prostym protoko�em, kt�ry umo�liwia wyszukiwanie informacji
o u�ytkownikach na innym serwerze. Pakiet ten zawiera serwer fingera. 

%description -l tr
finger, a� ba�lant�s� bulunan makinalarda �al��an kullan�c�lar hakk�nda 
k�sa bilgi veren bir hizmettir. Bu pakette standart bir finger sunucusu 
bulunmaktad�r.

%package -n finger-client
Summary:        Finger client 
Summary(de):    Finger-Client
Summary(fr):    Client finger
Summary(pl):    Klient finger
Summary(tr):    Finger istemcisi
Group:          Networking/Utilities
Group(pl):	Sieciowe/Narz�dzia

%description -n finger-client
Finger is a simple protocol which allows users to find information about
users on other machines. This package includes a standard finger client. 

%description -n finger-client -l de
Finger ist ein einfaches Protokoll, das Informationen �ber Benutzer auf
anderen Rechnern herausfindet. Dieses Paket enth�lt einen standardm��igen
Finger-Client. 

%description -n finger-client -l fr
finger est un protocole simple permettant de trouver des informations sur
les utilisateurs d'autres machines. Ce paquetage contient un client finger
standard.

%description -n finger-client -l pl
Finger jest prostym protoko�em, kt�ry umo�liwia wyszukiwanie informacji
o u�ytkownikach na innym serwerze. Pakiet ten zawiera klienta fingera.

%description -n finger-client -l tr
finger, a� ba�lant�s� bulunan makinalarda �al��an kullan�c�lar hakk�nda k�sa
bilgi veren bir hizmettir. Bu pakette standart bir finger istemcisi 
bulunmaktad�r.

%prep
%setup -q -n bsd-%{name}-%{version}
%patch0 -p1 
%patch1 -p1 
%patch2 -p1 
%patch3 -p1 
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/{man{1,8},pl/man1}} \
	$RPM_BUILD_ROOT/etc/sysconfig/rc-inetd

make INSTALLROOT=$RPM_BUILD_ROOT MANDIR=%{_mandir} install

mv -f $RPM_BUILD_ROOT%{_sbindir}/in.fingerd $RPM_BUILD_ROOT/usr/sbin/fingerd
mv -f $RPM_BUILD_ROOT%{_mandir}/man8/in.fingerd.8 \
	$RPM_BUILD_ROOT%{_mandir}/man8/fingerd.8 

install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/pl/man1/finger.1
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/fingerd

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/{man?/*,pl/man1/*} \
	README BUGS

%post 
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd restart 1>&2
else
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet sever" 1>&2
fi

%postun
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd restart
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,BUGS}.gz
%attr(755,root,root) %{_sbindir}/*
%attr(640,root,root) /etc/sysconfig/rc-inetd/fingerd

%{_mandir}/man8/*

%files -n finger-client
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%{_mandir}/man1/*
%{_mandir}/pl/man1/*
