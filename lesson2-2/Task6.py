def d():
    n = range (1,101)
    for k in n:
            if not k % 2:
                v = {k: k*k}
                for k, v in v.iteritems():
                    print k, v

print(d())