

# Initialize a list
def prime(k):
    primes=[1] 
    for val in range(1, 10000): 
       for n in range(2, val): 
           if (val % n) != 0:
              pass
           else:
             primes.append(val)
             break
       if len(primes) == k:
               print('\n'.join(map(str, primes)))

def primes(k):
    if k > 0:
        print 1
    primes = []
    n = 2
    while k > 1:
        for prime in primes:
            print (n)
            if n % prime == 0:
                print( n)
                k -= 1
                break
        else:
            primes.append(n)
        n += 1
prime(12)


