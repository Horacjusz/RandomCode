Str = '''
Rewolucja przemysłowa oraz jej konsekwencje okazały się katastrofą dla rodzaju ludzkiego. Znacznie zwiększyły średnią długość życia tych z nas, żyjących w krajach “rozwiniętych”, lecz zdestabilizowały społeczeństwo, uczyniły życie niespełnionym, podporządkowały ludzi nieudogodnieniom, doprowadziły do cierpienia na płaszczyźnie psychologicznej (w krajach Trzeciego Świata również i fizycznej) oraz naraziły naturalny świat na poważne szkody. Kontynuowanie rozwoju technologii pogorszy jedynie sytuację. Z pewnością podporządkuje ludzi jeszcze większym nieudogodnieniom i narazi naturalny świat na jeszcze większe szkody, prawdopodobnie doprowadzi do większego rozłamu społecznego i psychologicznego cierpienia, a nawet do zwiększenia cierpienia fizycznego w krajach “rozwiniętych”."
'''
A = list(Str)
for i in range(len(A)) :
    if A[i] == "ę" :
        A[i] = 'e'
    if A[i] == "Ę" :
        A[i] = 'E'
    elif A[i] == "ó" :
        A[i] = 'o'
    if A[i] == "Ó" :
        A[i] = 'O'
    elif A[i] == "ą" :
        A[i] = 'a'
    if A[i] == "Ą" :
        A[i] = 'A'
    elif A[i] == "ś" :
        A[i] = 's'
    if A[i] == "Ś" :
        A[i] = 'S'
    elif A[i] == "ł" :
        A[i] = 'l'
    if A[i] == "Ł" :
        A[i] = 'L'
    elif A[i] == "ż" or A[i] == 'ź' :
        A[i] = 'z'
    elif A[i] == "Ż" or A[i] == 'Ź' :
        A[i] = 'Z'
    elif A[i] == "ć" :
        A[i] = 'c'
    elif A[i] == "Ć" :
        A[i] = 'C'
    elif A[i] == "ń" :
        A[i] = 'n'
    elif A[i] == "Ń" :
        A[i] = 'N'

for i in range(len(A)) :
    if A[i] == "\n" :
        print()
    else :
        print(A[i], end = '')