import random
import sys

n = int(sys.argv[1])
rand_list = [random.randint(0, 2*n-1) for i in range(n)]
rand_list.sort(reverse=True)
print(n)
for i in rand_list:
    print(i)
