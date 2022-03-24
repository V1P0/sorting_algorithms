import sys
from sorting import mergeSort

n = int(sys.stdin.readline())
my_list = [int(sys.stdin.readline()) for i in range(n)]
show = n < 50
if show:
    print(my_list, '\nMergeSort:')
comparisons = mergeSort(my_list, show)
if show:
    print('sorted:\n', my_list)
print(f'{comparisons=}')
other_list = my_list[:]
other_list.sort()
print(f'sorted = {my_list == other_list}')
