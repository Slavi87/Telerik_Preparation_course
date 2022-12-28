#  1
# n = int(input())
# prime_list = []
# not_prime_list = []
# for i in range(2, n + 1):
#     if i not in prime_list:
#         not_prime_list.append(i)
#         for j in range(i * i, n + 1, i):
#             prime_list.append(j)
# print(max(prime_list))

# 2
# n = int(input())
# primes = [p for p in range(2, n + 1)]
# for p in primes:
#     if p > n / p:
#         break
#     for i in range(p * p, n + 1, p):
#         if i in primes:
#             primes.remove(i)
# print(max(primes))

# 3
import math
n = int(input())
primes = set(range(2, n + 1))
for p in range(2, math.ceil(n**0.5) + 1):
    for i in range(2, n + 1):
        if i % p == 0 and i != p:
            primes.discard(i)
print(max(primes))