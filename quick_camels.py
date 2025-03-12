#NIE ODPALAĆ TEGO KODU!!!!!!!!!!

import sys
sys.set_int_max_str_digits(2**20)

def a(n, tab) :
    if tab[n] is not None :
        return tab[n]

    tab[n] = (n-1)*a(n-1, tab) + (n-1)*a(n-2, tab)

    return tab[n]

#DO NOT RUN THIS CODE!!!!!!!!!!!!!!!

N = 99999999

tab = [None for i in range(N)]
tab[1] = 0
tab[2] = 1

#НЕ ЗАПУСКАЙТЕ ЭТОТ КОД!!!!!!!!!!

with open('./fortunne_wielblady.txt','w') as f :

    for i in range(3, N) :
        f.write(f'{i}: {a(i, tab)} \n \n')

#不要运行此代码!!!!!!!!!!