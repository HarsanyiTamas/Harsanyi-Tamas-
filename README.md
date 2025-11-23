# Harsanyi-Tamas- Z94OYV
A felhasználó megadja elöszőr a nevét. Miután kész csak akkor folytathatja ha elmúlt 18 éves. A végső ablakban pedig addig játszhat black jack-et amíg kedve tartja. Mindig a gép ellen játszik a felhasználó. A játékos neve egy txt fájlban érhető el.
A használt modulok:  tkinter as tk
                    import tkinter.messagebox as messagebox(azért kell mert így vizsgálom meg, hogy elmúlt e 18 éves a játékos)
                    import HT_pakli (itt történik a játék érdemi része. a main ennek az osztálynak a fügvényeit hívja meg.)
                    import random (A random kártyához szükséges.)

Fügvények:  def torol (letörli az eredményeket a felhasználó számára és visszaállítja az új játékhoz szükséges adatokat nullára.)
            def huzas (A játékos húz egy lapot a pakliból.)
            def gombhuzas(Ellenőrzi, hogy sikerült e a játékosnak 21-et húzni és nyernie vagy annál többet és vesztett)
            def osztojon(Ha a játékos nem akar többet húzni de még nem nyert akkor átadja a játékot a gépnek aki végig játsza a black jack szabályai szerint)
            def eletkor(A messagebox segítségével ellenőrzi, hogy elmúlt-e 18 éves a játékos) 
            def mentes(Kiírja a fájlba a játékos nevét.)
            def (bezárja a második ablakot)
            def beolvas_nev(Ellenőrzi, hogy megfelelő e az adat a mezőkben)
            def reset(Mindent letisztít egy új játékhoz)
            def osztokor(Meghívja az osztojon függvényt és értesíti a jatékost az eredményről)
            def HT_huzas(Meghívja a huzas függvényt és értesít az eredményről)

Használt osztály: HT_pakliakcio
