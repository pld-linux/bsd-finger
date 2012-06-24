Summary:        Finger client 
Summary(de):    Finger-Client
Summary(fr):    Client finger
Summary(pl):    Klient finger
Summary(tr):    Finger istemcisi
Group:          Networking/Utilities
Group(pl):	Sieciowe/Narz�dzia
Name:		bsd-finger
Version:	0.16
Release:	2
Copyright:	BSD
Source:		ftp://sunsite.unc.edu/pub/Linux/system/network/finger/%{name}-%{version}.tar.gz
Source1:	finger.1.pl
Source2:	fingerd.inetd
Patch0:		bsd-finger-DESTDIR.patch
Patch1:		bsd-finger-exact.patch
Patch2:		bsd-finger-pts.patch
Patch3:		http://www.misiek.eu.org/ipv6/bsd-finger-ipv6.patch.gz
Obsoletes:	finger
Obsoletes:	finger-client
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Finger is a simple protocol which allows users to find information about
users on other machines. This package includes a standard finger client. 

%description -l de
Finger ist ein einfaches Protokoll, das Informationen �ber Benutzer auf
anderen Rechnern herausfindet. Dieses Paket enth�lt einen standardm��igen
Finger-Client. 

%description -l fr
finger est un protocole simple permettant de trouver des informations sur
les utilisateurs d'autres machines. Ce paquetage contient un client finger
standard.

%description -l pl
Finger jest prostym protoko�em, kt�ry umo�liwia wyszukiwanie informacji
o u�ytkownikach na innym serwerze. Pakiet ten zawiera klienta fingera.

%description -l tr
finger, a� ba�lant�s� bulunan makinalarda �al��an kullan�c�lar hakk�nda k�sa
bilgi veren bir hizmettir. Bu pakette standart bir finger istemcisi 
bulunmaktad�r.

%package -n bsd-fingerd
Summary:	Finger server
Summary(de):	Finger-Server 
Summary(fr):	Server finger
Summary(pl):	Serwer finger
Summary(tr):	Finger sunucusu
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Prereq:		rc-inetd >= 0.8.1
Provides:	fingerd
Obsoletes:	fingerd
Obsoletes:	ffingerd
Obsoletes:	cfingerd
Obsoletes:	finger-server

%description -n bsd-fingerd
Finger is a simple protocol which allows users to find information about
users on other machines. This package includes a standard finger server. 

%description -n bsd-fingerd -l de
Finger ist ein einfaches Protokoll, das Informationen �ber Benutzer 
auf anderen Rechnern herausfindet. Dieses Paket enth�lt einen 
standardm��igen Finger-Server.

%description -n bsd-fingerd -l fr
finger est un protocole simple permettant de trouver des informations sur
les utilisateurs d'autres machines. Ce paquetage contient un serveur finger
standard.

%description -n bsd-fingerd -l pl
Finger jest prostym protoko�em, kt�ry umo�liwia wyszukiwanie informacji
o u�ytkownikach na innym serwerze. Pakiet ten zawiera serwer fingera. 

%description -n bsd-fingerd -l tr
finger, a� ba�lant�s� bulunan makinalarda �al��an kullan�c�lar hakk�nda 
k�sa bilgi veren bir hizmettir. Bu pakette standart bir finger sunucusu 
bulunmaktad�r.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
# Need update.
#%patch2 -p1

%build
./configure \
	--installroot=$RPM_BUILD_ROOT \
	--prefix=%{_prefix}

make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/{man{1,8},pl/man1}} \
	$RPM_BUILD_ROOT/etc/sysconfig/rc-inetd

make MANDIR=%{_mandir} install

mv -f $RPM_BUILD_ROOT%{_sbindir}/in.fingerd \
	$RPM_BUILD_ROOT%{_sbindir}/fingerd
mv -f $RPM_BUILD_ROOT%{_mandir}/man8/in.fingerd.8 \
	 $RPM_BUILD_ROOT%{_mandir}/man8/fingerd.8 

install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/pl/man1/finger.1
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/fingerd

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/{man?/*,pl/man1/*} \
	README BUGS

%post -n bsd-fingerd
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload 1>&2
else
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet sever" 1>&2
fi

%postun -n bsd-fingerd
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files -n bsd-fingerd
%defattr(644,root,root,755)
%doc {README,BUGS}.gz
%attr(755,root,root) %{_sbindir}/*
%attr(640,root,root) /etc/sysconfig/rc-inetd/fingerd
%{_mandir}/man8/*

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/pl/man1/*
