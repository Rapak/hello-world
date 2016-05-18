def filt() :
    div2 = filter(lambda x: not x % 2, range(1, 10001))
    div3 = filter(lambda x: not x % 3, range(1, 10001))
    return div2 + div3
print (filt())