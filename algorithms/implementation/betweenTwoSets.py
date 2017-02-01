#!/bin/python3

import sys

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(b_temp) for b_temp in input().strip().split(' ')]

a.sort()
b.sort()
count = 0
for i in range(a[n - 1], b[0]+1):
    flag = True
    for item in a:
        if i % item != 0:
            flag = False
            break
    if flag:
        for item in b:
            if item % i != 0:
                flag = False
                break
    if flag:
        count += 1
print(count)
