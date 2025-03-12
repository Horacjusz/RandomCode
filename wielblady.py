from itertools import permutations

N = 5

def camels(n) :
    if n == 0 :
        return None
    if n == 1 :
        return 0
    set_of_camels = []
    for i in range(1,n+1):
        set_of_camels += [i]

    num = 0

    perms = permutations(set_of_camels)

    for i in perms:
        listed = list(i)
        status = True
        for i in range(n - 1):
            if listed[i] + 1 == listed[i + 1] or listed[0] == 1 :
                status = False
                break
            
        if status :
            num += 1
            #print(listed)
    return num

for i in range(100) :
    print(camels(i))