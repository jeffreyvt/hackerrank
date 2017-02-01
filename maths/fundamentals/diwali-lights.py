"""
https://www.hackerrank.com/challenges/diwali-lights

Ran into a bit of trouble computing this one,
The naive approach is to calculate the nCr, however, 
as you dive deeper into the computation, there is a 
recurrence relationship between the outputs:
F(n) = 2 * F(n-1) + 1

The main() implements the naive approach,
The main2() implements the recurrence relationship to
compute the outputs.
"""


import math

def ncr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


def main():
	T = int(input())
	N = []
	for i in range(T):
		N.append(int(input()))
	for item in N:
		ans = 0
		for i in range(1, item+1):
			ans += ncr(item, i)
		print(int(ans) % 100000)


def main2():
	T = int(input())
	N = []
	for i in range(T):
		N.append(int(input()))

	for item in N:
		print(recursive(item) % 100000)


def recursive(num):
	ans = 1
	for i in range(num-1):
		ans = ans*2 + 1
	return(ans)

if __name__ == "__main__":
	main2()