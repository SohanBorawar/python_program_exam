l1 = [2,3,4,6,'tops']
l2 = [4,5,6,8,9,'tops','pvt']
l3 = []

for i in l1:
    for j in l2:
        if i not in l2 and i not in l3: 
            l3.append(i)
        elif j not in l1 and j not in l3:
            l3.append(j)
        else:
            pass

print(l3)
        