"""#int_list = [6,20,15,9]

def *function ():

def function_min (args):

    min_number = min(int_list)
    max_number = max(int_list)
    len_number = len(int_list)
    sum_numbers = sum(int_list)
    sorted_numbers = sorted(int_list)
    return min_number

def function_max (args):

    min_number = min(int_list)
    max_number = max(int_list)
    len_number = len(int_list)
    sum_numbers = sum(int_list)
    sorted_numbers = sorted(int_list)
    return max_number"""

def apply_all_func (int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))