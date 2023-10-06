l = [32,34,67,54,87,98,45]
total = 0
length = 0
for i in l:
    total = total + i
    length = length + 1
average = total//length
print("Total :",total)
print("Average :",average)
for i in l:
    if i > average:
        print(i)

