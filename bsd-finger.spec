Summary:	Finger server
Summary(de):	Finger-Server 
Summary(fr):	Server finger
Summary(pl):	Serwer finger
Summary(tr):	Finger sunucusu
Name:		finger
Version:	0.10
Release:	3
Copyright:	BSD
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Source:		ftp://sunsite.unc.edu/pub/Linux/system/network/finger/bsd-%{name}-%{version}.tar.gz
Source1:	finger.1.pl
Patch0:		bsd-finger-misc.patch
Patch1:		bsd-finger-security.patch
Patch2:		bsd-finger-nobr.patch
Patch3:		bsd-finger-typo.patch
Requires:	inetd
Provides:	fingerd
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Finger is a simple protocol which allows users to find information about
users on other machines. This package includes a standard finger server. 
The server runs from /etc/inetd.conf, which must be modified to disable 
finger requests.

%description -l de
Finger ist ein einfaches Protokoll, das Informationen über Benutzer 
auf anderen Rechnern herausfindet. Dieses Paket enthält einen 
standardmäßigen Finger-Server. Der Server läuft in /etc/inetd.conf, 
für das Finger-Anforderungen deaktiviert werden müssen.

%description -l fr
finger est un protocole simple permettant de trouver des informations sur
les utilisateurs d'autres machines. Ce paquetage contient un serveur finger
standard. Le serveur est lancé à partir de /etc/inetd.conf,
qui doit être modifié pour désactiver les requêtes finger.

%description -l pl
Finger jest prostym protoko³em, który umo¿liwia wyszukiwanie informacji
o u¿ytkownikach na innym serwerze. Pakiet ten zawiera serwer fingera. 

%description -l tr
finger, að baðlantýsý bulunan makinalarda çalýþan kullanýcýlar hakkýnda 
kýsa bilgi veren bir hizmettir. Bu pakette standart bir finger sunucusu 
bulunmaktadýr. Sunucu öntanýmlý olarak çalýþýr durumdadýr, çalýþmasýný 
istemiyorsanýz /etc/inetd.conf içerisinde ilgili satýrlarda deðiþiklik 
yapmanýz gerekecektir.

%package -n finger-client
Summary:        Finger client 
Summary(de):    Finger-Client
Summary(fr):    Client finger
Summary(pl):    Klient finger
Summary(tr):    Finger istemcisi
Group:          Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia

%description -n finger-client
Finger is a simple protocol which allows users to find information about
users on other machines. This package includes a standard finger client. 

%description -n finger-client -l de
Finger ist ein einfaches Protokoll, das Informationen über Benutzer auf
anderen Rechnern herausfindet. Dieses Paket enthält einen standardmäßigen
Finger-Client. 

%description -n finger-client -l fr
finger est un protocole simple permettant de trouver des informations sur
les utilisateurs d'autres machines. Ce paquetage contient un client finger
standard.

%description -n finger-client -l pl
Finger jest prostym protoko³em, który umo¿liwia wyszukiwanie informacji
o u¿ytkownikach na innym serwerze. Pakiet ten zawiera klienta fingera.

%description -n finger-client -l tr
finger, að baðlantýsý bulunan makinalarda çalýþan kullanýcýlar hakkýnda kýsa
bilgi veren bir hizmettir. Bu pakette standart bir finger istemcisi 
bulunmaktadýr.

%prep
%setup -q -n bsd-finger-0.10
%patch0 -p1 
%patch1 -p1 
%patch2 -p1 
%patch3 -p1 

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,sbin,share/man/{man1,man8,pl/man1}}

make INSTALLROOT=$RPM_BUILD_ROOT MANDIR=%{_mandir} install

mv -f $RPM_BUILD_ROOT%{_sbindir}/in.fingerd $RPM_BUILD_ROOT/usr/sbin/fingerd
mv -f $RPM_BUILD_ROOT%{_mandir}/man8/in.fingerd.8 \
	$RPM_BUILD_ROOT%{_mandir}/man8/fingerd.8 

install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/pl/man1/finger.1

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/{man1,man8,pl/man1}/* \
	README BUGS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,BUGS}.gz
%attr(755,root,root) %{_sbindir}/*

%{_mandir}/man8/*

%files -n finger-client
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%{_mandir}/man1/*
%{_mandir}/pl/man1/*

%changelog
* Thu May 13 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [0.10-3]
- added Group(pl),
- added finger-client subpackage,
- minor changes in %install,
- added pl translation of finger(1),
- package is now FHS 2.0 compliant.

* Thu Apr 15 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [0.10-2]
- gzipping documentation (instead bzipping)
- removed man group from man pages

* Sun Nov 08 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.10-1]
- build for PLD Tornado,
- major changes.

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- fix error message typo.

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Sep 22 1997 Erik Troan <ewt@redhat.com>
- added check for getpwnam() failure
