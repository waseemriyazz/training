# function to check if number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
# calling is_prime on each number in range
def print_primes_in_range(N):
    for i in range(2, N+1):
        if is_prime(i):
            print(i)

# Example usage:
print_primes_in_range(11)