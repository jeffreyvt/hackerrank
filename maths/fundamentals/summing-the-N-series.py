"""
https://www.hackerrank.com/challenges/summing-the-n-series
"""

def main():
	mod_val = 10**9 + 7
	T = int(input())
	ns = []
	for _ in range(T):
		ns.append(int(input()))
	for item in ns:
		print(item**2%mod_val)



if __name__ == "__main__":
	main()
