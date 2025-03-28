#function to yiels prime numbers up to 50
def prime_generator(limit=50):
    for num in range(2, limit + 1):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            yield num

primes = list(prime_generator())
print(primes)


#function to create a generator that produces an infinite sequence of even numbers
def even_numbers():
    num = 2
    while True:
        yield num
        num += 2

evens = even_numbers()
print(next(evens))  # Output: 2
print(next(evens))  # Output: 4

#
class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.a, self.b = 0, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return self.a

fib = Fibonacci(10)
print(list(fib))  # First 10 Fibonacci numbers

