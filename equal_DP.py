T = int(input())
problems = []
for i in range(T):
    N = int(input())
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    problems.append([N, a])

for i in range(T):
    N = problems[i][0]
    a = problems[i][1][::]
    a.sort()
    count = 0
    while True:

        diff = a[N-1] - a[0]
        # print(diff)
        if diff >= 5:
            for i in range(N-1):
                a[i] += 5
            a.sort()
            count += 1
        elif diff >= 2:
            for i in range(N-1):
                a[i] += 2
            a.sort()
            count += 1
        elif diff >= 1:
            for i in range(N-1):
                a[i] += 1
            a.sort()
            count += 1
        else:
            break
    print(count)
