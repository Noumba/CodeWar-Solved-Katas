import math
def prime_factors(n):
    primes = []
    prime_format = ""
    while n%2 == 0:
        primes.append(2)
        n = n/2
        for i in range(3, int(math.sqrt(n)+1),2):
            while(n%i == 0):
                primes.append(i)
                n=n/i
        if n>2:
            primes.append(n)
    counts = {prime:primes.count(prime) for prime in primes}
    for key in counts:
        if counts[key]> 1:
            
            prime_format = prime_format + "({}**{})".format(key,counts[key])
        else:
            prime_format = prime_format + "({})".format(key)
    return (prime_format)