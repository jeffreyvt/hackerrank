"""
sample input:
4 3
1 2 3

sample output:
4


Sample Input #02
10 4
2 5 3 6

Sample Output #02
5

sample input:
75 27
25 10 11 29 49 31 33 39 12 36 40 22 21 16 37 8 18 4 27 17 26 32 6 38 2 30 34
"""


def coin_search(amount, coins):
    m = len(coins)
    T = [[0 for x in range(amount + 1)] for y in range(m)]

    for i in range(m):
        T[i][0] = 1
    for j in range(1, amount + 1):
        if j%coins[0] == 0:
            T[0][j] = 1
    # print(T)

    for i in range(1, m):
        for j in range(1, amount + 1):
            # print("index  ",i,j)
            # print(T)
            # print("coinvalue =",coins[i])
            if j - coins[i] < 0:
                T[i][j] = T[i-1][j]
            # elif coins[i] - j == 0:
            #     T[i][j] = T[i-1][j] + 1
            else:
                # print(T[i-1][j], T[i][j-coins[i]])
                T[i][j] = T[i-1][j] + T[i][j-coins[i]]
            # print(T)

    return T[m-1][amount]



[amount, m] = input().split(" ")
amount = int(amount)
m = int(m)

coins = [int(a_temp) for a_temp in input().strip().split(' ')]
coins.sort()
# print(coins)
if 0 != amount:
    # count = 0

    print(coin_search(amount, coins))
elif 0 not in coins:
    print(0)
else:
    print(1)
