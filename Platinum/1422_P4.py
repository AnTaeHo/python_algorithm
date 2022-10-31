from functools import cmp_to_key


def cmp(x, y):
    if str(x) + str(y) > str(y) + str(x):
        return -1
    else:
        return 1


k, n = map(int, input().split())

number = [int(input()) for _ in range(k)]
number.sort(reverse=True)
for _ in range(k, n):
    number.append(number[0])
number.sort(key=cmp_to_key(cmp))
for i in number:
    print(i, end='')
