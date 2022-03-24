import sys
import math
import random


def isSorted(arr: list):
    for i in range(len(arr) - 1):
        if not arr[i] <= arr[i + 1]:
            return False
    return True


def bogoSort(arr: list) -> int:
    s = 0
    while not isSorted(arr):
        random.shuffle(arr)
        s += 1
    return s


n = int(sys.stdin.readline())
my_list = [int(sys.stdin.readline()) for i in range(n)]
if n > 15:
    print('are you drunk?')
    sys.exit(0)
print(my_list)
print(f'expected shuffles {math.factorial(n)}')
shuffles = bogoSort(my_list)
print(my_list)
print(f'{shuffles=}')
print(f'expected - actual = {math.factorial(n) - shuffles}')
