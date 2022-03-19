# **Implementacja gry w statki**
<br>
<div style="text-align: right"><b>Przemysław Pawlik</b></div>

## **1. Wstęp**
Program wykonany jako projekt zaliczeniowy z przedmiotu Język Python na który uczęszczałem w roku akademiskim 21/22.

----------
<br>

## **2. Opis programu**
Program jest komputerową implementacją zasad klasycznej gry „w Statki” przeznaczoną dla jednego gracza. 
<br>
<br>
Użytkownik podejmuje działania mierząc się z przeciwnikiem komputerowym. W gestii gracza spoczywa rozstawienie swoich okrętów na planszy i podejmowanie działań zmierzających do zatopienia jednostek przeciwnika poprzez poprawne wskazanie współrzędnych wrogiego okrętu.
<br>
<br>
Ostrzał przeprowadzany jest naprzemiennie, z zastrzeżeniem, że strona, która dokonała celnego ostrzału kontynuuje go, bez oddawania ruchu przeciwnikowi, do czasu pierwszego chybienia. Ostrzał i rozstawienie okrętów przeciwnika komputerowego jest generowane komputerowo, stąd położenie wrogich graczowi okrętów zmienia się.
Celem jest wyeliminowanie wszystkich jednostek przeciwnika, wyeliminowanie jednostki polega na wskazaniu wszystkich pól pod którymi kryje się okręt. 
<br>
<br>
Okręty prezentowane są przez pionowe lub poziome odcinki zajmujące od 1 do 4 pól na planszy, odcinki te nie mogą się przecinać lub na siebie nachodzić. Gra prowadzona jest na dwóch kwadratowych planszach liczących po 100 pól. Każde pole na planszy może zostać opisane za pomocą współrzędnych składających się z 10 liter alfabetu łacińskiego (A-J) i liczb (1-10). Literami określane jest położenie względem osi pionowej, liczbami względem osi poziomej.

----------
<br>

## **3. Sposób uruchomienia**
Aby uruchomić program należy wywołać komendę:<br>
`python Ships.py`<br>
a następnie postępować zgodnie z instrukacjami programu.

----------
<br>

## **4. Literatura**
https://pl.wikipedia.org/wiki/Okręty<br>
https://pl.wikipedia.org/wiki/Okręt<br>

----------
<br>

## **5. Wymagania**
**Python** - testowane na wersji **3.9.7**<br>
**System Linux** - działa bez problemu<br>
**System Windows** - działa uruchamiane na **WSL**, w **Pycharm** i **Windows Terminal Preview**<br>

----------
<br>