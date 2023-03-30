VÁLTOZÓK KIÍRÓ UTASÍTÁS PYTHONBAN

def kiiras():
    print("Az én nevem: Katalin")


VÁLTOZÓK HASZNÁLATA, ADATTÍPUSOK
def kiiras_nev():
    nev = "Katalin"     # szöveges típus - str
    kor = 53.5          # szám típus - float
    magassag = 173      # szám - int
    ferfi = False       # logikai - bool
    print(f"Az én nevem: {nev} \n {kor} éves vagyok.")
    print(f"\t Magasságom: {magassag}")
    print(f"\t Férfi vagyok? : {ferfi}")


MŰVELETEK SZÖVEGEKKEL

def muveletek_szovegekkel():
    szoveg="Az élet szép!"
    szoveg2="Főleg, ha programozunk!"
    szam = 2
    szov= szoveg + szoveg2
    print (szov)
    ujszov= szov + str(szam) +" - ban."
    print(ujszov)
    print(szoveg[0:7])
    print(szoveg.upper())
    print(szoveg.title())
    szam1 = "2"       #szövegként tárolt szám
    szam2 = 3         # számként tárolt szám
    #print(szam1 + szam2)        # hiba, mert két különböző típussal akarunk műveletet végrehajtani
    print(szam1 + str(szam2))   # szövegként fűzzük össze,  eredmény: "23"
    print(int(szam1) + szam2)   # számként adjuk össze,     eredmény: 5

def muveletekszovegekkel2():
    szoveg = "gipsz jakab"
    print(f"A szöveg hossza: {len(szoveg)}")
    print(f"Az első 'a' betű helye: {(szoveg.index('a'))}")
    keresztnev_elsobetu_helye = szoveg.index(" ")
    vezeteknev = szoveg[0:keresztnev_elsobetu_helye].title()
    keresztnev = szoveg[keresztnev_elsobetu_helye+1:len(szoveg)].title()
    monogram1 = vezeteknev[0:1].upper()
    monogram2 = keresztnev[0:1].upper()
    print(vezeteknev)
    print(keresztnev)
    print(monogram1 + monogram2)


MŰVELETEK SZÁMOKKAL

import math
def muveletek_szamokkal():
    a = 12              #int
    b = 24              #int
    osszeg = a + b      #eredmény int
    kulonbség = a-b     #eredmény int
    hanyados = a / b    #eredmény float
    szorzat = a * b     #eredmény int
    hatvany = a ** 2    #eredmeny int
    gyok = a ** 0.5     #eredmény float
    gyok = math.sqrt(a) #eredmény float

    a = 12.456
    egeszresz = a // 1  # hányszor van meg benne egész számszor az osztó - int
    maradek = a % 1     # az adott számmal osztva mennyi a maradék - float
    parose = a % 2      # Ha a kettővel való osztási maradék 0, akkor ps, különben ptlan a szám
    print(f"{a} szám egészrésze: {egeszresz}, a tört rész 2 tizedesre kerekítve: {maradek:.2f}")
    print(f"{a} szám kettővel való osztási maradéka 3 tizedesre kerekítve: {parose:.3f}")
    print(f"{13 } szám kettővel való osztási maradéka: {13 % 2}")


ADATBEKÉRÉS

def adatbekeres():
    nev = input("Add meg a neved!")
    kor = input("Add meg a korod!")
    kor = int(kor) / 2
    print(f"A neved: {nev} \n {kor} éves vagy.")


ELÁGAZÁSOK

def egyszeru_elagazas():
    #adott egy szám, döntsük el róla, hogy páros, vagy páratlan?
    # Milyen számokkal tesztelnéd a programod?
    szam = 12
    # tesztesetek
    # szam -----  várt eredmény
    #   12     |       12 páros
    #  -12     |      -12 páros
    #   13     |       13 páratlan
    #  -13     |      -13 páratlan
    if szam % 2 == 0:
        print(f"{szam} páros.")
    else:
        print(f"{szam} páratlan.")
    	#kérjünk be egy nevet és az illető nemét!
#Írjuk ki, hogy az adott nevű ember milyen nemű!
    nev = input("A neved:")
    neme = input("A nemed (f/n):")
    if neme == "f":
        print(f"{nev} férfi.")
    else:
        print(f"{nev} nő.")

def tobbszoros_elagazas_paritas():
    # adott egy szám, döntsük el róla, hogy pozitív, vagy negatív!
    # Milyen számokkal tesztelnéd a programod?
    # tesztesetek
    # szam -----  várt eredmény
    #   12     |       12 pozitív
    #  -13     |      -13 negatív
    #    0     |        A szám a nulla
    #   12.3   |       12.3 pozitív
    #  -13.45  |      -13.45 negatív

    szam = -12
    if szam > 0:
        print(f"{szam} pozitív.")
    elif szam==0:
        print(f"A szám  a  nulla.")
    else:
        print(f"{szam} negatív.")

def tobbszoros_elagazas_osztalyzat():
    """: A program olvasson be a konzolról egy egész számot!
    Ha a szám 0 és 100 közötti, akkor legyen a beolvasott szám egy százalékérték!
    A program írja ki a konzolra a százalékban megadott értékelést szövegesen
        0%–59%-ig elégtelen,
        60%–69%-ig elégséges,
        70%–79%-ig közepes,
        80%–89%-ig jó,
        90%–100%-ig jeles)!
    Ha a szám nem 0 és 100 közötti, akkor a program írja ki a konzolra, hogy „Hiba: érvénytelen százalék!”!
    """
    szam = int(input("Adj meg egy 0 ész 100 közötti számot! "))
    if szam <= 59 and szam >= 0:
        print(f"{szam} % - elégtelen")
    elif szam <= 69:
        print(f"{szam} % - elégséges")
    elif szam <= 79:
        print(f"{szam} % - közepes")
    elif szam <= 89:
        print(f"{szam} % - jó")
    elif szam <= 100:
        print(f"{szam} % - jeles")
    else:
        print(f"Hiba: érvénytelen százalék!")

def feltetelek_and():
    """13.  Adj meg három egész számot egy-egy változóba, melyek egy sorozat első három elemét jelentik.
    Írd ki a „növekvő” szót, ha a három szám növekvő sorrendben áll, és a „csökkenő” szót, ha csökkenőben!"""
    szam1 = 34
    szam2 = 45
    szam3 = 56
    # Milyen számokkal tesztelnéd a programod?
    # tesztesetek
    # szam1,szam2,szam3 -----  várt eredmény
    #  34,45,56      |      Növekvő sorrendv
    #  65,54,43      |      Csökkenő sorrend
    #  34,23,56      |      Rendezetlen sorozat
    if szam1 < szam2 and szam2 < szam3:
        print( f"{szam1}, {szam2}, {szam3} növekvő sorozat")
    elif szam3 < szam2 and szam2 < szam1:
        print(f"{szam1}, {szam2}, {szam3} csökkenő sorozat")
    else:
        print(f"{szam1}, {szam2}, {szam3} rendezetlen sorozat")

def feltetelek_or():
    """Kérj be egy egész számot, és írd ki, hogy osztható-e 3-mal vagy öttel!"""
    szam = int(input("Adj meg egy 0 ész 100 közötti számot! "))
    # Milyen számokkal tesztelnéd a programod?
    # tesztesetek
    # szam         -----  várt eredmény
    #  3             |      osztható 3-mal, vagy 5-tel
    #  5             |      osztható 3-mal, vagy 5-tel
    #  6             |      nem osztható sem 3-mal, sem 5-tel
    #  15            |      osztható 3-mal, vagy 5-tel
    if szam % 3 == 0 or  szam % 5 == 0:
        print( f"{szam}, osztható 3-mal, vagy 5-tel")
    else:
        print(f"{szam}, nem osztható sem 3-mal, sem 5-tel")

def egymasbaagyazott():
    """"
    Egy házaspárnak két gyereke van.
    A gyerek lehet édesgyerek, vagy mostoha, lány, vagy fiú. A program írja ki a négyféle lehetőséget a változók alapján:
     tipus : e - édes , m - mostoha
     nem : f - fiú, l - lány
    """
    tipus = "e"
    nem = "f"
    #tesztesetek
    #     tipus |  nem  |  várt eredmény
    #       e   |   f   |   Saját fiúgyermek.
    #       e   |   l   |   Saját leánygyermek.
    #       m   |   f   |   A házastárs fia.
    #       m   |   l   |   A házastárs lánya.
    #    bármi  |   f   |   A házastárs fia.
    #    bármi  |   l   |   A házastárs lánya.
    #       e   | bármi |   Saját leánygyermek.
    #       m   | bármi |   A házastárs lánya.
    
    if ( nem == "f"):
        if( tipus == "e"):
            print(" Saját fiúgyermek.")
        else:
            print(" A házastárs fia.")
    else:
        if (tipus == "e"):
            print(" Saját leánygyermek.")
        else:
            print(" A házastárs lánya.")


KOMPLEX FELADAT ELÁGAZÁSOKKAL

def pizza():
    """Készíts Pizza rendelő alkalmazást:
    A program kérje be, hogy sajtos, gombás, vagy sonkás pizzát kér-e?
    Kérje be a pizza méretét:
        kicsi   - az ára az ár 90%-a
        normál  - az ára az ár 100%-a
        nagy    – az ára az ár 110%-a

    Kérje be, hogy feltét kell-e?

    1.  Normál sajtos pizza alapára 1000 Ft
    2.  Normál gombás pizza alapára 1100Ft
    3.  Normál sonkás pizza alapára 1200 Ft

    Az extra feltét plusz 50 Ft-ba kerül. """

    """GONDOLD ÁT A TEZSTESETEKET! """
    # A változók kezdőértékének megadása - inicializálás *********************
    sajtos_alap_ar = 1000
    gombas_alap_ar = 1100
    sonkas_alap_ar = 1200
    # Adatok bekérése ********************************************************
    tipus = input("Válasszon pizzát 1 - sajtos / 2 - gombás / 3 - sonkás: ")

    meret = input("A pizza mérete (k)icsi/(n)normál/(o)óriás k/n/o: ")
    meret = meret[0:1].lower()
    feltet_kelle =  input("Kér extra feltétet? i/n: ")
    feltet_kelle = feltet_kelle[0:1].lower()

    szoveg= "A rendelt pizza: "
    ar = 0
    if tipus == "1":
        ar = sajtos_alap_ar
        szoveg += "sajtos pizza."
    elif tipus == "2":
        ar = gombas_alap_ar
        szoveg += "gombás pizza."
    elif tipus == "3":
        ar = sonkas_alap_ar
        szoveg += "sonkás pizza."
    else:
        ar = sonkas_alap_ar
        szoveg += "hibásan adta meg, ezért a legfinomabbat kapja!"

    if meret == "k":
        ar *= 0.9
        szoveg += " Kicsi méretben, "
    elif meret =="o":
        ar *= 1.1
        szoveg += "Óriás méretben, "
    else:
        szoveg += "Normál méretben, "

    if feltet_kelle == "i":
        ar += 50
        szoveg += "extra feltéttel."

    print(szoveg + " Fizetendő: " + str(ar) + " Ft." )


BONTSUK METÓDUSOKRA!

def pizza2():
    """Készíts Pizza rendelő alkalmazást:
    A program kérje be, hogy sajtos, gombás, vagy sonkás pizzát kér-e?
    Kérje be a pizza méretét:
        kicsi   - az ára az ár 90%-a
        normál  - az ára az ár 100%-a
        nagy    – az ára az ár 110%-a

    Kérje be, hogy feltét kell-e?

    1.  Normál sajtos pizza alapára 1000 Ft
    2.  Normál gombás pizza alapára 1100Ft
    3.  Normál sonkás pizza alapára 1200 Ft

    Az extra feltét plusz 50 Ft-ba kerül. """

    # Adatok bekérése ********************************************************
    tipus = beker("Válasszon pizzát 1 - sajtos / 2 - gombás / 3 - sonkás: ")
    meret = beker("A pizza mérete (k)icsi/(n)normál/(o)óriás k/n/o: ")
    feltet_kelle = beker("Kér extra feltétet? i/n: ")

    # Ár számítása ********************************************************
    ar = tipus_ar(tipus)
    ar = meret_ar(meret, ar) + feltet_ar(feltet_kelle)
    # Kiírandó szöveg kialakítása ********************************************************
    minta("=", 100)
    szoveg = "A rendelt pizza: " + tipus_szoveg(tipus) + meret_szoveg(meret) + feltet_szoveg(feltet_kelle)
    print(szoveg + "fizetendő: " + str(ar))
    minta("=", 100)

def minta(jel, db):
    print(jel * db)

def beker(szoveg):
    minta("*", 100)
    sz = input(szoveg)
    return sz[0:1].lower()

def tipus_ar(tipus):
    # A változók kezdőértékének megadása - inicializálás *********************
    sajtos_alap_ar = 1000
    gombas_alap_ar = 1100
    sonkas_alap_ar = 1200
    ar = 0
    if tipus == "1":
        ar = sajtos_alap_ar
    elif tipus == "2":
        ar = gombas_alap_ar
    elif tipus == "3":
        ar = sonkas_alap_ar
    else:
        ar = sonkas_alap_ar
    return ar

def tipus_szoveg(tipus):
    szoveg = ""
    if tipus == "1":
        szoveg += "sajtos pizza."
    elif tipus == "2":
        szoveg += "gombás pizza."
    elif tipus == "3":
        szoveg += "sonkás pizza."
    else:
        szoveg += "hibásan adta meg, ezért a legfinomabbat kapja!"
    return szoveg

def meret_ar(meret, ar):
    if meret == "k":
        ar *= 0.9
    elif meret == "o":
        ar *= 1.1
    return ar

def meret_szoveg(meret):
    szoveg = ""
    if meret == "k":
        szoveg += " Kicsi méretben,  "
    elif meret == "o":
        szoveg += " Óriás méretben, "
    else:
        szoveg += " Normál méretben, "

    return szoveg

def feltet_szoveg(feltet_kelle):
    szoveg = ""
    if feltet_kelle == "i":
        szoveg += "extra feltéttel. "
    return szoveg

def feltet_ar(feltet_kelle):
    pluszar = 0
    if feltet_kelle == "i":
        pluszar = 50
    return pluszar


CIKLUSOK
CIKLUSOK - WHILE CIKLUS - SZÁMLÁLÓS CIKLUS

def szamlalos():
    print("Írjuk ki a páros számokat 0 és 30 között! [0,30)")
    i = 0 # kell egy ciklusváltozó
    while i < 30: # eddig fut a ciklus
        print(i)
        i += 2 # a ciklusváltozó értékét meg kell változtatni

    print("Írjuk ki a számokat 30-tól 0-ig visszafelé! [30,0)")
    i = 30  # kell egy ciklusváltozó
    while i > 0:  # eddig fut a ciklus
        print(i)
        i -= 1  # a ciklusváltozó értékét meg kell változtatni


ELÖLTESZTELŐS CIKLUS - WHILE - ELLENŐRZÖTT ADATBEKÉRÉS

def ellenorzott_adatbekeres():
    # Kérjük be a felhasználótól az életkorát. Hibás érték esetén kérjük újra!
    #Az életkor 1 és 100 év között lehet.
    #Nem számlálós ciklus, ezért nem kell ciklusváltozó
    # Figyelni kell arra, hogy biztos kilépjünk a ciklusból helyes adat esetén.
    # A while feltételébe írt érték igaz, akkor végrehajtja a ciklusmag utasításait
    # Ha a feltétel hamis, akkor a ciklus után folytatja a program a futását.
    kor = int(input("Kérem adja meg a korát! [0,100]"))
    # while (kor < 1) or ( kor > 100):
    while not (kor >= 1  and  kor <= 100):
        kor = int(input("Nem jó adat, kérem adja meg újra! [0,100]"))
    # ciklus vége - akkor jutunk ide, ha a feltétel hamis lesz
    print(f"Az Ön kora: {kor} év!")

def adatbekeres():
    # Kérjük be a felhasználótól szavakat, addig, amíg a @ jelet nem üti le!
    #Nem számlálós ciklus, ezért nem kell ciklusváltozó
    # Figyelni kell arra, hogy biztos kilépjünk a ciklusból a megfelelő  adat esetén.
    # A while feltételébe írt érték igaz, akkor végrehajtja a ciklusmag utasításait
    # Ha a feltétel hamis, akkor a ciklus után folytatja a program a futását.
    szavak = (input("Kérem a szavakat! @-cal kilép..."))

    while not (szavak == "@"):
        print(szavak)
        szavak = (input("Kérem a szavakat! @-cal kilép..."))
    # ciklus vége - akkor jutunk ide, ha a feltétel hamis lesz


PROGRAMOZÁSI TÉTELEK - SZÁMOKON 

def megszamlalas():
    # Egy sorozatban adott tulajdonságú elemek száma
    # Számoljuk meg, hány 7-tel osztható szám van [0, 100] intervallumban!
    i = 0 # ciklusváltozó
    db = 0 # gyűjtőváltozó
    while i <= 100:
        if ( i % 7 == 0):
            db += 1 # gyűjtőváltozó értékét változtatom
        # elágazás vége
        i += 1 # ciklusváltozó értékét növelem
    # ciklus vége
    print(f"[0, 100] intervallumban {db } db 7-tel osztható szám van!")

def osszegzes():
    # Egy sorozatban adott tulajdonságú elemek számát, átlagát szorzatát, stb.. határozzuk meg
    # Mekkora a számok összege a [0, 100] intervallumban!
    i = 0 # ciklusváltozó
    ossz = 0 # gyűjtóváltozó
    while i <= 100:
        ossz += i # gyűjtőváltozó értékét változtatom a ciklusváltozó értékével
        i += 1 # ciklusváltozó értékét növelem
    # ciklus vége
    print(f"[0, 100] intervallumban  a számok összege: {ossz } ")

import random
def maximumkivalasztas():
    # Egy sorozatban a legnagyobb/legkisebb értékű elemet, vagy annak helyét határozzuk meg
    # Generáljunk 10 db véletlen számot a [1,90] intervallumban. Mekkora volt a legnagyobb szám?
    # Hányadik lépésben generáltuk a legnagyobb számot?
    i = 1 # ciklusváltozó
    max_ertek = 0 # gyűjtóváltozó
    max_hely = 0
    while i <= 10:
        vel = int(random.random() * 89) + 1
        print(vel)
        if (vel >max_ertek):
           max_ertek = vel
           max_hely = i
        #elágazás vége
        i += 1 # ciklusváltozó értékét növelem
    # ciklus vége
    print(f"[1, 90] intervallumban  a generált legnagyobb szám: {max_ertek }, a helye: {max_hely}")

def eldontes():
    # Van- e a sorozatban adott tulajdonságú elem?
    # Generáljunk 5 db véletlen számot a [1,90] intervallumban. Van-e köztük páros?
    # Pontosabban: Most addig generáljuk a számokat, amíg párost nem kapunk, d legfeljebb öt számot generáljunk!
    i = 1 # ciklusváltozó
    vel = int(random.random() * 89) + 1
    while i <= 5 and vel % 2 == 1: #fontos, hogy először a ciklusváltozót vizsgáljuk és csak utána a paritást
        print(vel)
        vel = int(random.random() * 89) + 1
        i += 1 # ciklusváltozó értékét növelem
    # ciklus vége
    if ( i<5 ):
        print(f"Van páros szám, az { i}. helyen.")
    else:
        print("Nincs páros szám!")


EGYMÁSBA ÁGYAZOTT CIKLUSOK

def szorzotabla():
    #Írjuk ki a szorzótáblát a képernyőre!
    i = 1  # külső ciklusváltozó
    while i <= 10:
        j = 1 # belső  ciklusváltozó
        sor = "" # Itt fogom tárolni egy sor számait!
        while j <= 10:
            sor += f"{i*j:>4}"
            j += 1 # belső ciklusváltozó növelése
        # belső ciklus vége
        print(sor)
        i += 1 # külső ciklusváltpzó növelése
    #külső ciklus vége


LISTÁK

# LISTÁK BEJÁRÁSA

import random
def listabejaras():
    # lista azonos típusú elemek halmaza, melyek adott sorrendben vannak
    # lista megadása:
    lista_nev = ["Éva", "Géza"]
    lista_szam = [1, 4, 3, 6]
    #Hivatkozás a lista elemeire az indexükkel lehet.
    # A számozás 0-tól kezdődik:
    print(lista_nev[1]) #Géza
    print(lista_szam[0]) #1
    #a lista hossza a benne lévő elemek száma
    print(len(lista_nev)) # 2, mert két elem van benne
    #lista elemeinek megváltoztatása:
    lista_nev[0] = "Juli"
    # listaelemek hozzáadása
    lista_nev.append("Elemér")

def lottoszamok():
    #generáljunk 5 lottószámot! [1,90]
    lotto_lista = [] # kezdetben üres a lista, itt fogom tárolni a lottószámokat
    i = 1 #ciklusváltozó
    while i <= 5:
        vel = int(random.random()*89)+1
        lotto_lista.append(vel) # véletlen szám hozzáadása a listához
        # lotto_lista.append(int(random.random()*89)+1)
        i += 1
    #ciklus vége


PROGRAMOZÁSI TÉTELEK LISTÁKON

def megszamlalas():
    # Adott egy lista, hány páros szám van benne?
    lista = [ 12, 32, 45, 21, 34]
    i = 0  # ciklusváltozó
    db = 0  # gyűjtőváltozó
    while i < len(lista):
        if (lista[i] % 2 == 0):
            db += 1
        i += 1
    # ciklus vége
    print(f"A lista = [ 12, 32, 45, 21, 34] listában  {db} db páros szám van!")

def osszegzes():
    # Egy listában adott tulajdonságú elemek számát, átlagát szorzatát, stb.. határozzuk meg
    # Mekkora a számok összege a listában?
    lista = [12, 32, 45, 21, 34]
    i = 0 # ciklusváltozó
    ossz = 0 # gyűjtóváltozó
    while i < len(lista):
        ossz += lista[i] # gyűjtőváltozó értékét változtatom a ciklusváltozó értékével
        i += 1 # ciklusváltozó értékét növelem
    # ciklus vége
    print(f"lista = [12, 32, 45, 21, 34] számok összege: {ossz } ")

def maximumkivalasztas():
    # Egy sorozatban a legnagyobb/legkisebb értékű elemet, vagy annak helyét határozzuk meg
    # Hol van a legnagyobb szám, és mennyi az értéke?
    lista = [12, 32, 45, 21, 34]
    i = 0 # ciklusváltozó
    max_ertek = 0 # gyűjtóváltozó
    max_hely = 0
    while i < len(lista):
        if (lista[i] >max_ertek):
           max_ertek = lista[i]
           max_hely = i
        #elágazás vége
        i += 1 # ciklusváltozó értékét növelem
    # ciklus vége
    print(f" lista = [12, 32, 45, 21, 34] legnagyobb száma: {max_ertek }, a helye: {max_hely}")

def eldontes():
    # Adott egy lista, döntsük el, hogy van-e benne páros szám!
    lista = [12, 32, 45, 21, 34]
    i = 0  # ciklusváltozó
    while i < len(lista) and lista[i] % 2 == 1:  # fontos, hogy először a ciklusváltozót vizsgáljuk és csak utána a paritást
        i += 1  # ciklusváltozó értékét növelem
    # ciklus vége
    if (i < len(lista)):
        print(f"Van páros szám, az {i}. helyen.")
    else:
        print("Nincs páros szám!")

def nyert_e_lotto():
    # Adott 5 lottószám!
    lotto = [12, 32, 45, 21, 34]
    # Kérjünk be a felhasználótól egy tippet és
    # döntsük el, hogy benne van-e a lottószámok között?
    tipp = int(input("Kérek egy számot 1 és 90 között! "))
    i = 0  # ciklusváltozó
    while i < len(lotto) and lotto[i] != tipp:  # fontos, hogy először a ciklusváltozót vizsgáljuk és csak utána a paritást
        i += 1  # ciklusváltozó értékét növelem
    # ciklus vége
    if (i < len(lotto)):
        print(f"Nyert, az {i}. helyen.")
    else:
        print("Nem nyert!")


EGYMÁSBA ÁGYAZOTT CIKLUSSAL KÉT LISTA

def hanytalalat_lotto():
    # Adott 5 lottószám!
    lotto = [12, 32, 45, 21, 34]
    # Kérjünk be a felhasználótól 5 tippet és
    # Hány találata lett a lottón?
    ## Tippek bekérése
    tipp = [] # itt tárolom a felhasználó tippjeit
    i = 0  # ciklusváltozó
    while i < 5:
        tipp.append(int(input(f"Kérem az {i+1}. számot 1 és 90 között! ")))
        i += 1  # ciklusváltozó értékét növelem
    # ciklus vége
    print(tipp)
    i = 0  # külső ciklusváltozó
    talalat_db = 0 # a találatok száma gyűjtőváltozoó
    while i < len(lotto):
        j = 0  # belső ciklusváltozó
        while j < len(tipp):
            if (tipp[j] == lotto [i]):
                talalat_db += 1
                print(tipp[j])
            #elágazás vége
            j += 1 # belső ciklusváltozó értékét növelem
        i += 1  # külső ciklusváltozó értékét növelem
    # ciklus vége
    print(f"A találatok száma: {talalat_db}")


SZÖVEGKEZELÉS  -  PROGRAMOZÁSI TÉTELEK

def abetuk_szama():
    # A szövegek karakterekből álló listák. Az egyes betűkre az indexükkel tudunk hivatkozni.
    # Adott egy szöveg. Hány 'a' betű van a szövegben?
    szoveg = " Indul a kutya és a tyúk aludni!"
    i = 0
    a_db = 0
    while i < len(szoveg):
        if (szoveg[i] == 'a'):
            a_db += 1
        #elágazás vége
    #ciklus vége
    print(f"A {szoveg} - ben {a_db} 'a' betű van")

def megszamlalas_szoveg():
    # Adott egy lista, hány a betűvel kezdődő szó van benne?
    lista = ["alma", "béka" , "Anna", "nyak"]
    i = 0  # ciklusváltozó
    db = 0  # gyűjtőváltozó
    while i < len(lista):
        if (lista[i][0] == "a"):
            db += 1
        i += 1
    # ciklus vége
    print(f"A {lista} listában  {db} db a betűs szó van!")

def osszegzes_szoveg():
    # Egy listában adott tulajdonságú elemek számát, átlagát szorzatát, stb.. határozzuk meg
    # Mekkora a szavak összhossza?
    lista = ["alma", "béka", "Anna", "nyak"]
    i = 0 # ciklusváltozó
    ossz = 0 # gyűjtóváltozó
    while i < len(lista):
        ossz += len(lista[i]) # gyűjtőváltozó értékét változtatom a ciklusváltozó értékével
        i += 1 # ciklusváltozó értékét növelem
    # ciklus vége
    print(f"A {lista} lista összhossza:   {ossz} ")

def maximumkivalasztas_szoveg():
    # Egy sorozatban a legnagyobb/legkisebb értékű elemet, vagy annak helyét határozzuk meg
    # Mekkora a leghosszabb szöveg hossza?
    lista = ["alma-ata", "béka", "Anna", "nyak"]
    i = 0 # ciklusváltozó
    max_ertek = 0 # gyűjtóváltozó
    max_hely = 0
    while i < len(lista):
        if (len(lista[i]) >max_ertek):
           max_ertek = len(lista[i])
           max_hely = i
        #elágazás vége
        i += 1 # ciklusváltozó értékét növelem
    # ciklus vége
    print(f" {lista} leghosszabb szava: {lista[max_hely]}, hossza:  {max_ertek }, a helye: {max_hely}")


KOMPLEX FELADAT CIKLUSOKKAL

Az elágazásos fejezet végén specifikált pizzarendelő alkalmazást alakítsuk át úgy, hogy a felhasználótól addig kérje be a rendelésket, amíg a @ jelet nem ütjük le!
Tároljuk a felvett rendeléseket megfelelő listákba!  pizzanev, pizzameret, pizzaextra
A rendelések felvétele után készítsünk statisztikát!
1.	Melyik típusú (név alapján)  pizzából hány darab fogyott? 
2.	Melyik pizzából fogyott a legtöbb? 
3.	Mekkora volt a bevétel? 
4.	Hányszor kértek extra feltétet? 
5.	A kicsi, nagy , vagy a közepes pizzából rendeltek-e többet? 
6.	… ami még eszetekbe jut. 











