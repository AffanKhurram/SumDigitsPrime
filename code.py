# prints primes up to but not including max
max = 1000

def sumdigits(n):
    if len(str(n)) == 1:
        return n
    sum = 0
    for i in str(n):
        sum += int(i)
    if len(str(sum)) >= 2:
        return sumdigits(sum)
    else:
        return sum

def prime(n):
    for i in range(2, int(n**0.5)):
        if n%i == 0:
            return False
    return True


for i in range(11, max, 2):
    if (prime(i)):
        print(i, sumdigits(i))
