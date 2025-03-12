from math import sqrt

file = open(r"C:\Users\pawel\Desktop\Pliki\Coding\VS_Code\Python\matura_2022\liczby.txt")
data = file.read().split("\n")
for i in range(len(data)) :
    _ = data[i]
    if len(_) > 0 :
        data[i] = int(data[i])
    else :
        data.pop()
data.sort()

def is_prime(n) :
    if ( (n == 2) or (n == 3) ) :
        return True
    elif ( (n == 1) or (n == 0) or ((n % 2) == 0) or ((n % 3) == 0) ) :
        return False
    else :
        i = 5
        while i <= sqrt(n) :
            if (((n % i) == 0) or ((n % (i + 2)) == 0)) :
                return False
            i += 6
        return True

primes = [2,3]

def prim(number) :
    global primes
    if number > primes[-1] :
        for i in range(primes[-1] + 1,number+1) :
            if is_prime(i) :
                primes.append(i)
                
def factor(number) :
    n = number
    global primes
    prim(n)
    factors = []
    dif_factors = []
    
    length = len(primes)
    i = length - 1
    while i > -1 :
        if n % primes[i] == 0 :
            n = n // primes[i]
            factors.append(primes[i])
            if len(dif_factors) > 0 and dif_factors[-1] != primes[i] :
                dif_factors.append(primes[i])
            if len(dif_factors) == 0 :
                dif_factors.append(primes[i])
            i += 1
            
        i -= 1
    return (number,len(factors),len(dif_factors))

numbers = []
for i in data :
    numbers.append(factor(i))

max_factors = max(numbers,key = lambda x: x[1])
max_dif_factors = max(numbers,key = lambda x: x[2])

print(max_factors[0],max_factors[1],max_dif_factors[0],max_dif_factors[2])