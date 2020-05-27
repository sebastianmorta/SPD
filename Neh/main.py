import numpy

def ReadFile(FileName):
    data = []
    with open('data\\NEH' + str(FileName) + '.DAT') as file:
        n, m = file.readline().split()
        for i in file:
            if not i.isspace():
                data.append([int(x) for x in i.split()])
    return data, int(n), int(m)

#j-zadanie k-maszyna
#n-zadania m-maszyny
def Cmax(data, n, m):
    C = numpy.zeros((int(n+1), int(m+1)))
    for j in range(1, n+1):
        for k in range(1, m+1):
            C[j][k] = max(C[j-1][k], C[j][k-1]) + data[j-1][k-1]
    return C

def SumSortP(data, n, m):
    permutation = []
    result = []
    for i in range(n):
        permutation.append(i)
    temp = sorted(permutation, key=lambda x: Psum(data, x, m), reverse=True)
    for i in temp:
        result.append(data[i])
    return result

def Psum(data, n, m):
    sumP = 0
    for i in range(m):
        sumP += data[n][i]
    return sumP

def Neh(data, n, m):
    SortedList = SumSortP(data, n, m)
    CurrentTask = SortedList[0]
    sequence = [CurrentTask]
    best_sequence = []
    for i in range(1, n): # dla każdego zadania
        BestCmax = float("inf") # bardzo duża liczba
        for j in range(i+1): # dla każdej pozycji w permutacji
            temp_sequence = sequence[:]
            temp_sequence.insert(j, SortedList[i])
            n = len(temp_sequence)
            CurrentCmax = Cmax(temp_sequence, n, m)[n][m]
            if CurrentCmax < BestCmax:
                best_sequence = temp_sequence
                BestCmax = CurrentCmax
        sequence = best_sequence
    return int(BestCmax)


def read_wyniki(nb):
    with open('data\\wyniki' + str(nb) + '.DAT') as f:
        return int(f.readline())

if __name__ == '__main__':

    wyniki_tab = []
    result_tab = []
    for file in range(1, 10):
        data, n, m = ReadFile(file)
        result = Neh(data, n, m)
        result_tab.append(result)
        wyniki_tab.append(read_wyniki(file))
    print('wyniki obliczone: ')
    print(result_tab)
    print('wyniki ze strony: ')
    print(wyniki_tab)