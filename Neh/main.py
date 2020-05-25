import numpy

def ReadFile(FileName):
    data = []
    with open('data\\NEH' + str(FileName) + '.DAT') as file:
        #n, m = [int(x) for x in next(file).split()]
        n, m = file.readline().split()
        print(n, m)
        for i in file:
            if not i.isspace():
                data.append([int(x) for x in i.split()])
    return data, n, m

#j-zadanie k-maszyna
#n-zadania m-maszyny
def Cmax(data, n, m):
    C = numpy.zeros((int(n+1), int(m+1)))
    for j in range(1, n+1):
        for k in range(1, m+1):
            C[j][k] = max(C[j-1][k], C[j][k-1]) + data[j-1][k-1]
    return C

def sum(data, n, m):
    sumP = 0
    for i in range(m):
        sumP += data[n][i]
    return sumP

def sumList(data, n, m):
    sumlist=[]
    for i in range(n):
        sumlist.append(i)
    return sorted(sumlist, key=lambda x: sum(data, x, m), reverse=True)

def inserter(sequence, index, value):
    new_sequence = sequence[:]
    new_sequence.insert(index, value)
    return new_sequence

def Neh(data, n, m):
    CTab = Cmax(data, n, m)
    PTab = sumList(data, n, m)
    current_sequence = [PTab[0]]
    current_sequence.append(PTab[0])
    for i in range(1, n):
        cm = float("inf")
        for j in range(0, i + 1):
            temp_sequence = inserter(current_sequence, j, PTab[i])
            temp_cmax = Cmax(data, len(temp_sequence), m)[len(temp_sequence)-1][m]
            if cm > temp_cmax:
                best_sequence = temp_sequence
                cm = temp_cmax
            current_sequence = best_sequence
    return  current_sequence

def read_wyniki(nb):
    with open('data\\wyniki' + str(nb) + '.DAT') as f:
        return int(f.readline())

if __name__ == '__main__':
    result_tab = []
    data, n, m = ReadFile(1)
    C = Cmax(data, int(n), int(m))
    print(Neh(data, int(n), int(m)))
    print('wynikiWITI: ')
    print(data)
