import math
def is_prime(n):
    if n > 1:
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(n) + 1), 2):
            if n % current == 0: 
                return False
        return True
    return False

def manipulate_generator(g,n):
    if is_prime(n+1):
            next(g)
            manipulate_generator(g, n+1)
         


def positive_integers_generator():
    n = 1
    while True:
        x = yield n
        if x is not None:
            n = x
        else:
            n += 1

k = int(raw_input())
g = positive_integers_generator()
for _ in range(k):
    n = next(g)
    print n 
    manipulate_generator(g, n)
