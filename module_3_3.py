def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

value_list = [1, [2,3], True]
value_dict_ = {'a': 23, 'b': [10,20], 'c': 'привет'}
value_list_2 = ['строка', 333]

print_params()
print_params(c=[1,2,3])
print_params(b = 25)
print_params(*value_list)
print_params(**value_dict_)
print_params(*value_list_2, 42)
