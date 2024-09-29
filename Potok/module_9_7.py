def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        for i in (2, int(result)):
            if result % i == 0:
                print(f"Простое")
            else:
                print(f"Составное")
            return result
    return wrapper
@is_prime
def sum_three(*args):
    result = sum(args)
    return result


result = sum_three(2, 3, 6)
print(result)