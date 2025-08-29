def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]

# Precompute primes up to ~2,000,000 (enough for n <= 100000)
primes = sieve(2000000)

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(primes[n - 1])   # because list is 0-indexed
