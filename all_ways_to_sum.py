from math import sqrt

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

def new_divisions(division, divisions=set(), prev_part=()):
    if len(division) == 1:
        return divisions

    remove = 0
    add = None
    for i in range(len(division)):
        if division[remove] < 2:
            remove = i
            continue
        if i == remove:
            continue
        if division[i] < 9:
            add = i
            break

    divisions.add(prev_part + tuple(division))
    divisions = new_divisions(division[1:], divisions, prev_part + tuple(division[:1]))

    if add is not None:
        division[remove] -= 1
        division[add] += 1
        divisions.add(prev_part + tuple(division))
        divisions = new_divisions(division[1:], divisions, prev_part + tuple(division[:1]))
        divisions = new_divisions(division, divisions, prev_part)

    return divisions

def generate_divisions(number, positions) :
    starter = [1] * positions

    summ = positions
    ind = 0
    while summ != number :
        n = min(number - summ, 8)
        summ += n
        starter[ind] += n
        ind += 1
    
    return list(new_divisions(starter, set()))


def find_sums(number) :
    n = number
    min_length = 1
    
    while n > 9 :
        n -= 9
        min_length += 1
    
    
    for i in range(min_length, number + 1) :
        divisions = generate_divisions(number, i)
        numbers = []
        
        for division in divisions :
            num = 0
            for j in range(len(division)) :
                num += division[j]*(10**(len(division) - 1 - j))
            numbers.append(num)
        numbers.sort()
        
        primes = []
        for numb in numbers :
            if (is_prime(numb)) :
                primes.append(numb)
        
        print("There are", len(primes), "prime numbers that have", i, "digits and sum up to", number)
        if len(primes) > 0 :
            print("List:")
            for j in range(len(primes) - 1) :
                print(primes[j], end = ",")
            print(primes[-1])
        print()

# print(find_sums(70))

print(len(generate_divisions(10,4)) + len(generate_divisions(10,2)) + len(generate_divisions(10,2)) + 1)