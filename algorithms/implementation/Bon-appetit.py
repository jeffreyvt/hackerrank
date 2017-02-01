"""
https://www.hackerrank.com/challenges/bon-appetit?h_r=next-challenge&h_v=zen
"""


def main():
	n, k = [int(x) for x in input().split(" ")]
	c = [int(x) for x in input().split(" ")]
	b = int(input())

	total = sum(c)
	total_needs_paid = (total - c[k])//2
	if total_needs_paid == b:
		print("Bon Appetit")
	else:
		print(b - total_needs_paid)



if __name__ == "__main__":
	main()