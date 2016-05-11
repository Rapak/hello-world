def boolen(a,b,c):
    if a is True:
        if b is True:
            if c is True:
                print 'a - true, b - true, c - true ', 'expr =', (a or not b) and (c or not a)
    if a is False:
        if b is True:
            if c is True:
                print 'a - false, b - true, c - true ', 'expr =', (a or not b) and (c or not a)
    if a is True:
        if b is False:
            if c is True:
                print 'a - true, b - false, c - true ', 'expr =', (a or not b) and (c or not a)
    if a is True:
        if b is True:
            if c is False:
                print 'a - true, b - true, c - false ', 'expr =', (a or not b) and (c or not a)
    if a is False:
        if b is False:
            if c is False:
                print 'a - false, b - false, c - false ', 'expr =', (a or not b) and (c or not a)
    if a is False:
        if b is True:
            if c is False:
                print 'a - false, b - false, c - false ', 'expr =', (a or not b) and (c or not a)

boolen(a = False, b = True, c = False )