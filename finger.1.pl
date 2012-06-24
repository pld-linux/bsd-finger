.\" Copyright (c) 1989, 1990 The Regents of the University of California.
.\" All rights reserved.
.\"
.\" Redistribution and use in source and binary forms, with or without
.\" modification, are permitted provided that the following conditions
.\" are met:
.\" 1. Redistributions of source code must retain the above copyright
.\"    notice, this list of conditions and the following disclaimer.
.\" 2. Redistributions in binary form must reproduce the above copyright
.\"    notice, this list of conditions and the following disclaimer in the
.\"    documentation and/or other materials provided with the distribution.
.\" 3. All advertising materials mentioning features or use of this software
.\"    must display the following acknowledgement:
.\"	This product includes software developed by the University of
.\"	California, Berkeley and its contributors.
.\" 4. Neither the name of the University nor the names of its contributors
.\"    may be used to endorse or promote products derived from this software
.\"    without specific prior written permission.
.\"
.\" THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND
.\" ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
.\" IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
.\" ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE
.\" FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
.\" DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
.\" OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
.\" HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
.\" LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
.\" OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
.\" SUCH DAMAGE.
.\"
.\"	from: @(#)finger.1	6.14 (Berkeley) 7/27/91
.\"	$Id$
.\"
.\" Translation (c) 1998 Marcin Mazurek <mazek@capella.ae.poznan.pl>
.\" {PTM/MM/0.1/08-10-1998/"finger.1 - program do sprawdzania informacji o u�ytkowniku"}
.Dd July 13, 1996
.Dt FINGER 1
.Os "Linux NetKit 0.07"
.Sh NAZWA
.Nm finger
.Nd program do sprawdzania informacji o u�ytkowniku
.Sh SK�ADNIA
.Nm finger
.Op Fl lmsp
.Op Ar u�ytkownik ...
.Op Ar u�ytkownik@host ...
.Sh OPIS
.Nm finger
wy�wietla informacj� o u�ytkownikach danego systemu.
.Pp
Dozwolone opcje to:
.Bl -tag -width flag
.It Fl s
.Nm Finger
podaje nazw� u�ytkownika (login name), imi� i nazwisko, nazw� terminala
i mo�liwo�� pisania do niego
 (``*'' po nazwie terminala oznacza �e prawo pisania do niego jest
zabronione), czas "bezczynno�ci", czas zalogowania si�, adres i telefon biura.
.Pp
Czas logowania wy�wietlany jest w nast�puj�cym formacie: miesi�c, dzie�,
godzina i minuty.Je�li czas ten jest wi�kszy ni� sze�� miesi�cy
wy�wietlany jest rok a nie czas co do godziny i minuty.
.Pp
Nieznane urz�dzenia jak i nie daj�ce si� okre�li� czasy zalogowania si� i bezczynno�ci
pokazywane s� jako gwiazdki.
.Pp
.It Fl l
Po podaniu tej opcji finger wy�wietla pe�n� informacj�, pokazan� w kilku
liniach, okre�lon� przez opcj�
.Fl s
plus dodatkowo katalog domowy u�ytkownika, telefon domowy, pow�oka logowania si�,
informacj� o jego poczcie, i zawarto�� plik�w
.Dq Pa .plan
,
.Dq Pa .project
i
.Dq Pa .forward
z katalogu domowego u�ytkownika.
.Pp
Numery telefon�w podane jako jedenastocyfrowe liczby s� wy�wietlane w
formacie ``+N-NNN-NNN-NNNN''.
Numery podane jako dziesi�cio- lub siedmiocyfrowe liczby s� wy�wietlane jako
jego odpowiedni pod�a�cuch.
Numery podane jako liczby pi�ciocyfrowe s� wy�wietlane w formacie ``xN-NNNN''.
Numery podane jako liczby czterocyfrowe s� wy�wietlane w formacie ``xNNNN''.
.Pp
Je�li prawo pisania do urz�dzenia jest wy��czone, wtedy tekst ``(messages off)''
jest do��czany do lini zawieraj�cej nazw� urz�dzenia.
Przy podanej opcji
.Fl l
informacja o terminalu zalogowanego u�ytkownika jest podana dla ka�dego
u�ytkownika i powt�rzona w zale�no�ci od liczby logowa� si�.
.Pp
Informacja o braku poczty zasygnalizowana jest tekstem ``No Mail.'',
Je�li u�ytkownik sprawdzi� swoj� poczt� zanim przysz�a nowa wy�wietlany jest
tekst ``Mail last read DDD MMM ## HH:MM YYYY (TZ)''
, lub ``New mail received ...'',
``  Unread since ...'' je�li u�ytkownik ma now� poczt�.
.Pp
.It Fl p
Wy��cza w opcji
.Fl l
programu
.Nm finger
wy�wietlanie zawarto�ci plik�w
.Dq Pa .plan
i
.Dq Pa .project
.
.It Fl m
Wy��cza wyszukiwanie nazw u�ytkownik�w.
Nazwa u�ytkownika podawana jako argument programu finger jest zazwyczaj
nazw� u�ytkownika w systemie; jednak�e, finger wyszukuje tego ci�gu tak�e w
prawdziwej nazwie u�ytkownika, chyba �e zostanie podana opcja 
.Fl m
.
Nie istnieje rozr�nienie na du�e i ma�e litery w nazwach wyszukiwanych przez
.Nm finger
.
.El
.Pp
Je�li nie ma podanych �adnych opcji,
.Nm finger
standardowo wy�wietla informacj� w stylu opcji
.Fl l
je�li nazwa u�ytkownika lub systemu zosta�a podana, 
format informacji odpowiada opcji
.Fl s
.
Je�li kt�ra� z informacji nie jest dost�pna, niekt�rych z p�l mo�e brakowa�.
.Pp
Je�li nie zosta�y podane �adne argumenty,
.Nm finger
wypisze informacj� dla ka�dego u�ytkownika zalogowanego w danej chwili w
systemie.
.Pp
.Nm Finger
mo�e by� wykorzystany do wyszukiwania u�ytkownik�w na odleg�ym systemie.
Zamiast pojedynczej nazwy u�ytkownika
.Ar u�ytkownik
podajemy
.Dq Li u�ytkownik@host ,
lub
.Dq Li @host ,
gdzie informacja w pierwszym przypadku standardowo wy�wietlana jest w formacie 
opcji 
.Fl l
, a w drugim w formacie opcji
.Fl s
.
Opcja
.Fl l
jest jedyn� opcj� jaka mo�e by� przekazana odleg�emu systemowi.
.Sh ZOBACZ TAK�E
.Xr chfn 1 ,
.Xr passwd 1 ,
.Xr w 1 ,
.Xr who 1
.Sh HISTORY
Komenda
.Nm finger
pokaza�a si� po raz pierwszy w BSD 3.0 
