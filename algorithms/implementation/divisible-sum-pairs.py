"""
https://www.hackerrank.com/challenges/divisible-sum-pairs
"""

def main():
	# initialise the inputs
	n,k = input().strip().split(' ')
	n,k = [int(n),int(k)]
	a = [int(a_temp) for a_temp in input().strip().split(' ')]

	#compute the outputs
	count = 0
	for i in range(n):
		for j in range(i+1, n):
			if (a[i] + a[j]) % k  == 0:
				count += 1
	print(count)


if __name__ == "__main__":
	main()