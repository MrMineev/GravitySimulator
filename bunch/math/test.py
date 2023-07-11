import math

n = 6

ans = 1

def fact(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

#print(fact(3))

final = 0

for i in range(1, 2 ** n + 1):
    ans = n
    sum = 0
    for j in range(1, i + 1):
        multi = math.pi * ((fact(j - 1) + 1) / j)
        ret = math.cos(multi) ** 2
        res = math.floor(ret)

        sum += res
    ans = n / sum
    ans = ans ** (1 / n)

    new = math.floor(ans)

    final += new

print(1 + final)
