def dubl(str):
    for i in str:
        if str.count(i) <=1:
            print i

dubl(['1','2','3','4','4','6','2'])