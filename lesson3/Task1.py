def compreh() :
    s2 = [i for i in range(1,10001) if not i % 2]
    s3 = [i for i in range(1,10001) if not i % 3]
    return s2 + s3;

print (compreh())