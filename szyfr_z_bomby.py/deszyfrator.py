message = "379.121.99.105.101.32.380.121.99.105.101.32.106.101.115.116.32.110.111.119.101.108.261"

output = ""

table = message.split(".")
for i in table :
    output += chr(int(i))

print(output)