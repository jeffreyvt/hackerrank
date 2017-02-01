"""
https://www.hackerrank.com/challenges/leonardo-and-prime?h_r=next-challenge&h_v=zen
"""

import math


def generate_prime(current_primes):
    current_biggest = current_primes[len(current_primes)-1]
    test = current_biggest + 2
    while True:
        prime = True
        for item in current_primes:
            if test % item == 0:
                prime = False
                break
        if prime:
            break
        else:
            test += 2
    current_primes.append(test)
    return current_primes



n = int(input())
for i in range(n):
    number = int(input())
    if number == 0:
        print(0)
    elif number == 1:
        print(0)
    elif number == 2:
        print(1)
    elif number == 3:
        print(1)
    else:
        current_prime = [2, 3]
        multi = 2
        count = 0
        if number >= multi:
            count += 1
        multi = 6
        if number >= multi:
            count += 1
        while number >= multi:
            current_prime = generate_prime(current_prime)
            multi = multi * current_prime[len(current_prime)-1]
            if number >= multi:
                count += 1
        print(count)


