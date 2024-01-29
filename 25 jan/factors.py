def print_factors(num):
    factors = []
    for i in range(2, num):
        if num % i == 0:
            factors.append(i)
    if len(factors) == 0:
        print(-1)
    else:
        print(' '.join(map(str, factors)))


number = 8
print_factors(number)
