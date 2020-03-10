import os                                               #importuje biblioteke do przegladania plikow w folderach

def o(x):                                               #funkcja, ktora bedzie nam zwracala najkrotszy czas
    with open(x, "r") as plik:                          #przygotowanie pliku tekstowego do odczytu
        if plik.readable():                             #sprawdzenie, czy plik jest poprawny
            TT = []                                     #lista przechowujaca w kazdej komorce wartosci kolejno [r, p pi]
            TT.append([0, 0])                           #inicjujemy pierwsza wartosc p i r jako 0
            n = int(plik.readline())                    #zczytujemy z pliku ilosc zadan
            C = [0 for i in range(n+1)]                 #inicjalizacja listy C jako wektor zerowy 15 elementowy ze wzgledu na ulatwienie dalszych operacji
            for i in range(1, n+1):                     #petla jadaca od pierwszej danej z pliku do ostatniej dlatego n+1 bo 1 element to 0 0
                TT.append(plik.readline().split())      #zapelniamy liste TT wartosciami z pliku split pozwala nam na rozdzielenie danych na osobne listy
                TT[i][0] = int(TT[i][0])                #domyslnie czytanie i przypisywanie odbywa sie dla zmiennych string
                TT[i][1] = int(TT[i][1])                #wiec zmieniamy ich typ na int
                TT[i].append(i)                         #dodanie ostatniej wartosci czyli pi
            TT.sort()                                   #sortujemy wzgledem wartosci ri poniewaz jest jako pierwsza i algorytm bierze tylko ja pod uwage
            for i in range(1, n+1):                     #obliczamy Cmax ze wzoru, poniewaz mamy juz posortowane wartosci ostatnia wartosc czyli C[n+1] da nam pozadany wynik
                C[i]=max(TT[i][0], C[i-1]) + TT[i][1]   #TT[i][0] - r(i), TT[i][1] - p(i), TT[i][2] - pi(i)
    return (C[len(C)-1])                                #zwraca ostatnia wartosc listy C czyli Cmax

lista = os.listdir("data")                              #wczytuje liste plikow
for i in range(0, len(lista)):                          #dodaje do nazwy kazdego pliku przedrostek okreslajacy polozenie w folderze
    lista[i] = 'data/'+lista[i]
data = int(input("podaj nr pliku danych ")) - 1
print(o(lista[data]))