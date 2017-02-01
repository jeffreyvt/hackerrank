"""
https://www.hackerrank.com/challenges/handshake?h_r=next-challenge&h_v=zen
"""


n = int(input())

for i in range(n):
    ppl = int(input())
    sum = 0
    for j in range(1,ppl):
        sum += j
    print(sum)