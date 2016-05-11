
def fst_lst_chr(str) :
    fst_ten_letters = str[:10]
    lst_ten_letters = str[-10:]
    for i in fst_ten_letters:
        print i
    for r in lst_ten_letters:
        print r
    return str;

fst_lst_chr('Natalia is a very very very happy girl')

