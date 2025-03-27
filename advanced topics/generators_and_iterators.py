def prime_generator(limit=50):
    for num in range(2, limit + 1):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            yield num

primes = list(prime_generator())
print(primes)


def even_numbers():
    num = 2
    while True:
        yield num
        num += 2

evens = even_numbers()
print(next(evens))  # Output: 2
print(next(evens))  # Output: 4
