def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

primes = []
num = 2
while len(primes) < 25:
    if is_prime(num):
        primes.append(num)
    num += 1

print(primes)
