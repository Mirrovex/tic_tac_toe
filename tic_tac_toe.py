import random
def wyswietl(): #wyswietlanie pola
    print(pole[0],'|',pole[1],'|',pole[2],'              ',miejsca[0],'|',miejsca[1],'|',miejsca[2]) #pierwsza linijka pola
    print('-- --- --','              ','-- --- --')
    print(pole[3],'|',pole[4],'|',pole[5],'              ',miejsca[3],'|',miejsca[4],'|',miejsca[5]) #druga linijka pola
    print('-- --- --''               ','-- --- --')
    print(pole[6],'|',pole[7],'|',pole[8],'              ',miejsca[6],'|',miejsca[7],'|',miejsca[8]) #trzecia linijka pola

def win():
    mozliwosci=[[pole[0],pole[1],pole[2]], #poziomo 1
                [pole[3],pole[4],pole[5]], #poziomo 2
                [pole[6],pole[7],pole[8]], #poziomo 4
                [pole[0],pole[3],pole[6]], #pionowo 1
                [pole[1],pole[4],pole[7]], #pionowo 2
                [pole[2],pole[5],pole[8]], #pionowo 3
                [pole[0],pole[4],pole[8]], #na skos 1
                [pole[2],pole[4],pole[6]]] #na skos 2
    for x in range (8):
        l=[]
        for y in range(3):
            if(mozliwosci[x][y]==gracze[gracz]): #jesli na tym polu jest znak przejdz dalej
                l.append(mozliwosci[x][y]) #daj graczowi 1pkt
                if(l.count(gracze[gracz])==3): #jesli gracz ma 3pkt to wygral
                    wygrany=1
                    return wygrany
            else: #jesli na tym polu nie ma znaku gracza przejdz do kolejnej mozliwosci
                break
    if(pole.count(' ')==0): #nie ma wolnych pol
        wygrany=2
        return wygrany

def wstaw(odp,znak): #wstawianie znaku
    for x in range(9):
        if(odp in miejsca): #jesli wpisane jest pole od 1-9 przejdz dalej
            if(odp==miejsca[x]):
                if(pole[x] == gracze[p1] or pole[x] == gracze[p2]): #jesli pole jest zajete wybierz nowe
                    if(gracz!='komputer'):
                        print('\n','To polejest juz zajete, wybierz inne: ')
                        wstaw(input(),znak)
                        break
                    else:
                        wstaw(random.choice(miejsca),znak)
                        break
                else: #jesli pole nie jest zajete wpisz znak
                    pole[x]=znak
                    break
        else: #jesli takie pole nie istnieje wpisz nowe
            if(gracz!='komputer'):
                print('\n','Takie pole nie istnieje, wybierz inne: ')
                wstaw(input(),znak)
                break
            else:
                wstaw(random.choice(miejsca),znak)
                break

def pc(trudnosc):
    if(trudnosc==1):
        p=random.choice(miejsca)
        wstaw(p,gracze[gracz])

gracze={}
znaki=['X','O']
p1=input('Gracz 1 wpisz swoj nick: ')
gracze[p1]=random.choice(znaki) #znak gracza 1
znaki.remove(gracze[p1])
trudnosc=0
z_kim=input('Z kim chcesz zagrac? (Wpisz "pc" = komputer, "osoba" = inny gracz): ')
while True:
    if(z_kim=='pc'):
        trudnosc=input('Wybierz poziom trudnosci: ("1" = latwy, "2" = trudny): ')
        while True:
            if(trudnosc=='1'):
                trudnosc=1
                p2='komputer'
                break
            elif(trudnosc=='2'):
                trudnosc=2
                p2='komputer'
                break
            else:
                trudnosc=input('Nie ma takiej trudnosci, wpisz ponownie: ')
    elif(z_kim=='osoba'):
        p2=input('Gracz 2 wpisz swoj nick: ')
        print('\n')
        break
    else:
        z_kim=input('Nie ma takiego trybu, wpisz ponownie: ')
    if(trudnosc>0):
        break
gracze[p2]=random.choice(znaki) #znak gracza 2
pkt1=0
pkt2=0

while True:
    kto_teraz=[p1,p2] #losowanie zaczynajacego gracza
    tura=[] #kto zacznie
    gracz1=random.choice(kto_teraz) #gracz jeden 1 to:
    tura.append(gracz1)
    kto_teraz.remove(gracz1)
    gracz2=random.choice(kto_teraz) #gracz 2 to:
    tura.append(gracz2)

    miejsca=['1','2','3','4','5','6','7','8','9'] #niezmienne pola
    pole=[' ',' ',' ',' ',' ',' ',' ',' ',' '] #zmienne pola

    wygrany=0
    print('Wpisuj liczby pol wedlug schematu: ')
    print('Powodzenia :)','\n')
    wyswietl() #wyswietlanie pola

    while (wygrany!=1): #dopoki ktos nie wygra albo nie bedzie remis
        for gracz in tura: #wybieranie ktorego gracza jest tura
            if(gracz=='komputer'):
                pc(trudnosc)
                print('Komputer: ')
            else:
                print(gracz,'wpisz gdzie wstawic',gracze[gracz],': ')
                wstaw(input(),gracze[gracz])
                print('\n')
            wyswietl()
            print('\n')
            wygrany=win() #sprawdzanie czy ktos wygral
            if(wygrany==1): #jesli ktos wygral
                print('Wygral: ',gracz,'\n')
                if(gracz==p1):
                    pkt1+=1 #dawanie pkt graczowi 1
                elif(gracz==p2):
                    pkt2+=1 #dawanie pkt graczowi 2
                break
            elif(wygrany==2): #jesli jest remis
                print('Remis','\n')
                pkt1+=1
                pkt2+=1
                wygrany=1
                break
    chcesz=input('Jesli chcesz zagrac jescze raz wpisz cokolwiek, jesli nie wpisz "end": ')
    print(' ')
    if(chcesz=='end'): #jesli nie chcesz grac dalej zakoncz gre
        break
print('Koniec gry','\n')
print('Wygrane', p1,':',pkt1) #ile razy wygral gracz 1
print('Wygrane',p2,':',pkt2) #ile razy wygral gracz 2
