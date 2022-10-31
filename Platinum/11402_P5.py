from math import factorial


def check(a, b):
    if a < b:
        return 0
    elif a == b:
        return 1
    return factorial(a) // factorial(b) // factorial(a - b)


N, K, m = map(int, input().split())
answer = 1
n_m = []
k_m = []

while N != 0 or K != 0:
    n_m.append(N % m)
    k_m.append(K % m)
    N //= m
    K //= m
for i in range(len(n_m)):
    answer = answer * check(n_m[i], k_m[i]) % m
print(answer % m)
