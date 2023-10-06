l = [23,55,67,78,6,34,65,43]
larg = 0
for i in l:
    if i>larg:
        larg = i
    else:
        pass
small = larg
for i in l:
    if i<small:
        small = i
    else:
        pass

print("largest :",larg)
print("smallest :",small)