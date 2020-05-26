import numpy
import sys

def ReadFile(FileName):
    data = []
    with open('data\\NEH' + str(FileName) + '.DAT') as file:
        #n, m = [int(x) for x in next(file).split()]
        n, m = file.readline().split()
        #print(n, m)
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

def sorted_by_p(data, n, m):
    permutation = []
    result = []
    for i in range(n):
        permutation.append(i)
    temp = sorted(permutation, key=lambda x: sum(data, x, m), reverse=True)
    for i in temp:
        result.append(data[i])
    return result

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
    print('newsewfa', new_sequence,index,value)
    new_sequence.insert(index, value)
    return new_sequence

def neh(data, n, m):
    tasks_lst = sorted_by_p(data, n, m)
    current_task = tasks_lst[0]
    sequence = [current_task]
    best_sequence = []
    for i in range(1, n): # dla każdego zadania
        best_c_max = float("inf") # bardzo duża liczba
        for j in range(0, i+1): # dla każdej pozycji w permutacji
            temp_sequence = list.copy(sequence)
            temp_sequence.insert(j, tasks_lst[i])
            n = len(temp_sequence)
            c_max_seq = Cmax(temp_sequence, n, m)[n][m]
            if c_max_seq < best_c_max:
                best_sequence = temp_sequence
                best_c_max = c_max_seq
        sequence = best_sequence
    return int(best_c_max)

def Neh(data, n, m):
    #CTab = Cmax(data, n, m)
    PTab = sumList(data, n, m)
    current_sequence = []
    current_sequence.append(PTab[0])
    for i in range(1, n):
        cm = float("inf")
        temp = current_sequence
        for j in range(0, i + 1):
            temp_sequence = inserter(temp, j, PTab[i])#sekwencja,
            temp_cmax = Cmax(data, len(temp_sequence), m)[len(temp_sequence)-1][m]
            if cm > temp_cmax:
                best_sequence = temp_sequence
                cm = temp_cmax
            current_sequence = best_sequence
            print("i -", i, "| j -", j, "| temp seq-", temp_sequence, '| curr seq', current_sequence, "| best -", best_sequence, "| tempcmax -", temp_cmax)
    return  current_sequence,

def read_wyniki(nb):
    with open('data\\wyniki' + str(nb) + '.DAT') as f:
        return int(f.readline())

if __name__ == '__main__':
    lst = []

    for i in range(1, 10):
        tasks, n, m = ReadFile(i)

        print(str(i) + " - " + str(neh(tasks, n, m)) + " - " + str(read_wyniki(i)))