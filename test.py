# Dynamic Programming Python implementation of Coin Change problem
def count(S, m, n):
    # We need n+1 rows as the table is consturcted in bottom up
    # manner using the base case 0 value case (n = 0)
    table = [[0 for x in range(m)] for x in range(n + 1)]
    print(table)
    # Fill the enteries for 0 value case (n = 0)
    for i in range(m):
        table[0][i] = 1
    print(table)
    # Fill rest of the table enteries in bottom up manner
    for i in range(1, n + 1):
        for j in range(m):
            print(table)
            # Count of solutions including S[j]
            x = table[i - S[j]][j] if i - S[j] >= 0 else 0

            # Count of solutions excluding S[j]
            y = table[i][j - 1] if j >= 1 else 0

            # total count
            table[i][j] = x + y
    print(table)
    print(n, m-1)
    return table[n][m - 1]


# Driver program to test above function
arr = [1,2,3]
m = len(arr)
n = 4
print(count(arr, m, n))

# This code is contributed by Bhavya Jain