message = "Życie życie jest nowelą"

output = ""
l = len(message)
for i in range(l) :
    ind = ord(message[i])
    output += str(ind)
    if l-i > 1 :
        
        output += "."


print(output)
