'''
1.1 Feladat
Készíts egy programot, amely megkérdezi a felhasználótól, hogy jó napja van-e! A válasz kétféle lehet: igen vagy nem. A választól függően írjon ki üzenetet a gép!
'''

szoveg = input('Milyen napja volt? ')
if szoveg == "Jó":
    print("Akkor további szép napot! ")
if szoveg == "Rossz":
    print("Remélem jobb lesz.")
else:
    szoveg = input('Milyen napja volt? ')