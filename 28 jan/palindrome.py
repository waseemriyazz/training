def reverse_number(number):
    reverse = 0 
    while number!=0:
        digit= number % 10
        number = number // 10
        reverse = reverse * 10 + digit
    return reverse
def pallindrome (number):
    if reverse_number(number)==number:
        return True
    return False
print(pallindrome(121),
pallindrome(10),
pallindrome(11))