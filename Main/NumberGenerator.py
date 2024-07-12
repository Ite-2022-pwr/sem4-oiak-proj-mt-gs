import random

# losowanie liczb maksymalnie do 1.000
def GenerateNumbers():
    n = random.randint(1, 10000)
    while n % 2 == 0:  # warunek: n jest liczba nieparzysta
        n = random.randint(1, 10000)
    e = random.randint(0, 10000)
    a = random.randint(0, n - 1)  # warunek: 0 <= a <= n-1
    return a, e, n