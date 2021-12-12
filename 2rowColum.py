n = 0
r = [0, 1, 2, 3]
c = [0, 1, 2, 3, 4]
i = 0
d = 0
while (i<=3):
    while n<=4:
        n=n+1
        d[r][c] = r*c
    i = i+1
print(d)
