file = open(r"C:\Users\pawel\Desktop\Pliki\Coding\VS_Code\Python\matura_2022\liczby.txt")
data = file.read().split("\n")
count = 0
first = ""
for number in data:
    str_ = str(number)
    if len(str_) > 0 and (str_[0] == str_[-1]) :
        if count == 0 :
            first = str_
        count += 1
print(count,first)