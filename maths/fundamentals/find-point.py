n = int(input())

for i in range(n):
    points = [int(a_temp) for a_temp in input().strip().split(' ')]
    p = points[:2]
    q = points[2:]
    pq = [q[0] - p[0], q[1] - p[1]]
    print(str(p[0] + pq[0] * 2) + " " + str(p[1] + pq[1] * 2))
