def p(str):
    s = str.lower()
    r = s.replace(" ", "")
    t = r.replace(',', '')
    f = t.replace(':', '')
    z = f.replace('.', '')
    o = z.replace('!', '')
    l = o.replace('\'', '')
    v = l.replace('(', '')
    k = v.replace(')', '')
    m = k.replace('?', '')
    y = m.replace(';', '')
    c = y.replace('\"', '')
    return c == c[::-1]

print (p(' Are we not pure? \"No sir!\" Panama\'s moody Noriega brags. \"It is garbage!\" '
         'Irony dooms a man; a prisoner up to new era. '))