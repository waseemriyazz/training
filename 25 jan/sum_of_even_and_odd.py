def sum_of_even_and_odd_digits(n):
    even_sum = 0
    odd_sum = 0

    for digit in str(n):
        digit = int(digit)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    print(f"{even_sum} {odd_sum}")


num = 132456
sum_of_even_and_odd_digits(num)
