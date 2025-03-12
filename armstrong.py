from math import sqrt

def is_prime(n) :
    if ( (n == 2) or (n == 3) ) :
        return True
    elif ( (n == 1) or (n == 0) or ((n % 2) == 0) or ((n % 3) == 0) ) :
        return False
    else :
        for i in range(5,int(sqrt(n))) :
            if (((n % i) == 0) or ((n % (i + 2)) == 0)) :
                return False
        return True

def square_sum(num) :
    n = num
    sum = 0
    leng = len(str(num))
    while n != 0 :
        check = n % 10
        sum += check**leng
        n = (n - check) // 10
    return sum


def armstrong_prime():
    number = 0
    test = 0
    while (len(str(number))) < 61 :
        if test == 7 :
            break
        if square_sum(number) == number :
            print(number, end = '; ')
            if is_prime(number) :
                test += 1
                print('PRIME', end = '; ')
            print()
        number += 1

armstrong_prime()