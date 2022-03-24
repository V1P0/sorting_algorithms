import random
from sorting import *
from matplotlib import pyplot

n_list = [100*i for i in range(1, 11)]
results = [[], [], []]
for k in range(3):
    results[k] = [[] for j in range(5)]
    results[k][0] = [[] for x in range(10**k)]
    results[k][1] = [[] for x in range(10**k)]
    results[k][2] = [[] for x in range(10**k)]
    results[k][3] = [[] for x in range(10**k)]
    results[k][4] = [[] for x in range(10**k)]
    for j in range(10**k):
        for i in range(10):
            n = n_list[i]
            my_list = [random.randint(0, 2*n-1) for i in range(n)]
            c, s = insertionSort(my_list[:])
            results[k][0][j].append([c, s])
            c = mergeSort(my_list[:])
            results[k][1][j].append([c, 0])
            c, s = quickSort(my_list[:], 0, len(my_list)-1)
            results[k][2][j].append([c, s])
            c, s = dualPivotQuickSort(my_list[:], 0, len(my_list) - 1)
            results[k][3][j].append([c, s])
            c, s = hybridSort(my_list[:], 0, len(my_list) - 1)
            results[k][4][j].append([c, s])
for k in range(3):
    for j in range(10**k):
        pyplot.plot(n_list, [results[k][0][j][i][0] for i in range(10)], 'r+')
        pyplot.plot(n_list, [results[k][1][j][i][0] for i in range(10)], 'bo')
        pyplot.plot(n_list, [results[k][2][j][i][0] for i in range(10)], 'g^')
        pyplot.plot(n_list, [results[k][3][j][i][0] for i in range(10)], 'c1')
        pyplot.plot(n_list, [results[k][4][j][i][0] for i in range(10)], 'md')
    pyplot.legend(['insertion', 'merge', 'quick', 'dualPivot', 'hybrid'])
    pyplot.yscale('log')
    pyplot.title(f'comparisons for {10 ** k}')
    pyplot.savefig(f'comparisons for {10**k}')
    pyplot.clf()
for k in range(3):
    for j in range(10**k):
        pyplot.plot(n_list, [results[k][0][j][i][1] for i in range(10)], 'r+')
        pyplot.plot(n_list, [results[k][1][j][i][1] for i in range(10)], 'bo')
        pyplot.plot(n_list, [results[k][2][j][i][1] for i in range(10)], 'g^')
        pyplot.plot(n_list, [results[k][3][j][i][1] for i in range(10)], 'c1')
        pyplot.plot(n_list, [results[k][4][j][i][1] for i in range(10)], 'md')
    pyplot.legend(['insertion', 'merge', 'quick', 'dualPivot', 'hybrid'])
    pyplot.yscale('log')
    pyplot.title(f'shifts for {10 ** k}')
    pyplot.savefig(f'shifts for {10**k}')
    pyplot.clf()
for k in range(3):
    for j in range(10**k):
        pyplot.plot(n_list, [results[k][0][j][i][0]//n_list[i] for i in range(10)], 'r+')
        pyplot.plot(n_list, [results[k][1][j][i][0]//n_list[i] for i in range(10)], 'bo')
        pyplot.plot(n_list, [results[k][2][j][i][0]//n_list[i] for i in range(10)], 'g^')
        pyplot.plot(n_list, [results[k][3][j][i][0]//n_list[i] for i in range(10)], 'c1')
        pyplot.plot(n_list, [results[k][4][j][i][0]//n_list[i] for i in range(10)], 'md')
    pyplot.legend(['insertion', 'merge', 'quick', 'dualPivot', 'hybrid'])
    pyplot.title(f'cn for {10 ** k}')
    pyplot.savefig(f'cn for {10**k}')
    pyplot.clf()
for k in range(3):
    for j in range(10**k):
        pyplot.plot(n_list, [results[k][0][j][i][1]//n_list[i] for i in range(10)], 'r+')
        pyplot.plot(n_list, [results[k][1][j][i][1]//n_list[i] for i in range(10)], 'bo')
        pyplot.plot(n_list, [results[k][2][j][i][1]//n_list[i] for i in range(10)], 'g^')
        pyplot.plot(n_list, [results[k][3][j][i][1]//n_list[i] for i in range(10)], 'c1')
        pyplot.plot(n_list, [results[k][4][j][i][1]//n_list[i] for i in range(10)], 'md')
    pyplot.legend(['insertion', 'merge', 'quick', 'dualPivot', 'hybrid'])
    pyplot.title(f'sn for {10 ** k}')
    pyplot.savefig(f'sn for {10**k}')
    pyplot.clf()

