import sys
from sorting import dualPivotQuickSort


n = int(sys.stdin.readline())
my_list = [int(sys.stdin.readline()) for i in range(n)]
show = n < 50
if show:
    print(my_list, '\ndualPivotQuickSort:')
comparisons, shifts = dualPivotQuickSort(my_list, 0, len(my_list) - 1, show)
if show:
    print('sorted:\n', my_list)
print(f'{comparisons=}')
print(f'{shifts=}')
other_list = my_list[:]
other_list.sort()
print(f'sorted = {my_list == other_list}')

