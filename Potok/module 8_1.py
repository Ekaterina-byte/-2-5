def add_everything_up(a,b):

    try:
        a == str
        b==int, float
        c=a+b
    except TypeError:
        print(a,b, sep='')
    else:
        print(round(c,3))





add_everything_up(123.456, 'строка')
add_everything_up('яблоко', 4215)
add_everything_up(123.456, 7)
