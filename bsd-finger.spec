Summary:	Finger client and server
Summary(de):	Finger-Client und Server 
Summary(fr):	Client et server finger
Summary(pl):	Klient i serwer finger
Summary(tr):	Finger istemcisi ve sunucusu
Name:		finger
Version:	0.10
Release:	2d
Copyright:	BSD
Group:		Networking
URL:		ftp://sunsite.unc.edu/pub/Linux/system/network/finger
Source:		bsd-%{name}-%{version}.tar.gz
Patch:		bsd-%{name}-%{version}-misc.patch
Patch1:		bsd-%{name}-%{version}-security.patch
Patch2:		bsd-%{name}-%{version}-nobr.patch
Patch3:		bsd-%{name}-%{version}-typo.patch
Requires:	inetd
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Finger is a simple protocol which allows users to find information about
users on other machines. This package includes a standard finger client
and server. The server runs from /etc/inetd.conf, which must be modified
to disable finger requests.

%description -l de
Finger ist ein einfaches Protokoll, das Informationen über Benutzer auf anderen
Rechnern herausfindet. Dieses Paket enthält einen standardmäßigen Finger-Client
und -Server. Der Server läuft in /etc/inetd.conf, für das Finger-Anforderungen
deaktiviert werden müssen.

%description -l fr
finger est un protocole simple permettant de trouver des informations sur
les utilisateurs d'autres machines. Ce paquetage contient un client finger
standard et un serveur. Le serveur est lancé à partir de /etc/inetd.conf,
qui doit être modifié pour désactiver les requêtes finger.

%description -l pl
Finger jest prostym protoko³em który umo¿liwia wyszukiwanie iformacji
o u¿ytkownikach na innym serwerze. Pakiet ten zawiera klienta i serwer 
fingera. 

%description -l tr
finger, að baðlantýsý bulunan makinalarda çalýþan kullanýcýlar hakkýnda kýsa
bilgi veren bir hizmettir. Bu pakette standart bir finger sunucusu ve
istemcisi bulunmaktadýr. Sunucu öntanýmlý olarak çalýþýr durumdadýr,
çalýþmasýný istemiyorsanýz /etc/inetd.conf içerisinde ilgili satýrlarda
deðiþiklik yapmanýz gerekecektir.

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
install -d $RPM_BUILD_ROOT/usr/{bin,man/man1,man/man8,sbin}

make INSTALLROOT=$RPM_BUILD_ROOT install
mv -f $RPM_BUILD_ROOT/usr/sbin/in.fingerd $RPM_BUILD_ROOT/usr/sbin/fingerd
mv -f $RPM_BUILD_ROOT/usr/man/man8/in.fingerd.8 \
	$RPM_BUILD_ROOT/usr/man/man8/fingerd.8 

bzip2 -9 $RPM_BUILD_ROOT/usr/man/man[18]/* README BUGS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.bz2 BUGS.bz2

%attr(755,root,root) /usr/bin/*
%attr(755,root,root) /usr/sbin/*
%attr(644,root, man) /usr/man/man[18]/*

%changelog
* Sun Nov 08 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.10-1d]
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
