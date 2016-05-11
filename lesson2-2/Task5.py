def sum13(str):
    s = 0
    for i in str:
        if i == 13:
            break
        if i > 13:
            break
        s = s + i
    return s

print ( sum13([1,3,3,1,13,2,1,4,1]) )