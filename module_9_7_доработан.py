def is_prime(func):
    def wrapper(*args):
        x = func(*args)
        i = 2
        while i * i <= x and x % i != 0:
            i += 1
        if i * i > x:
            print(f'Простое')
        else:
            print(f'Сложное')
        return x
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
