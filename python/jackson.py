import os
lista = os.listdir("data")
for i in range(0, len(lista)):
    lista[i] = 'data/'+lista[i]
print(lista)

TT = []
TT.append([0,0])
def o(x):
    with open(x, "r") as plik:
        if plik.readable():
            n = int(plik.readline())
            C = [0 for i in range(n+1)]
            for i in range(1, n+1):
                TT.append(plik.readline().split())
                TT[i][0] = int(TT[i][0])
                TT[i][1] = int(TT[i][1])
                TT[i].append(i)
            TT.sort()
            for i in range(1, n+1):
                C[i]=max(TT[i][0], C[i-1]) + TT[i][1]

    return (C[len(C)-1])
x = int(input("podaj nr pliku danych")) - 1

print(o(lista[x]))
