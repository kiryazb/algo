from math import gcd, sqrt


def first_solution(x, y):
    count = 0
    if y % x != 0:
        return 0
    if y == x:
        return 1
    else:
        y //= x
        for i in range(1, int(sqrt(y)) + 1):
            if y % i == 0:
                j = y // i
                if gcd(i, j) == 1:
                    count += 2
    return count


x, y = list(map(int, input().split()))
print(first_solution(x ,y))