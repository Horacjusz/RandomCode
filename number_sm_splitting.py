T = [[[1]]]

def split(number) :
    global T
    l = len(T)
    if number <= l :
        return T[number-1]
    for i in range(l+1,number+1) :
        T.append([[i]])
        for j in range(i-2,-1,-1) :
            for k in T[j] :
                T[i-1].append(k+[i-j-1])
    
    return T[number - 1]


t = split(5)
for _ in t :
    print(_)

#for i in range(25) :
#    split(i+1)
#    print(i+1,"done")
    