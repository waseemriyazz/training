def print_star_pattern(N):
    for i in range(1, N//2 + 2):
        # spaces
        for j in range(N//2 + 1 - i):
            print(" ", end=" ")
       
        # stars
        for j in range(2*i - 1):
            print("*", end="")
        
        print()

    for i in range(N//2, 0, -1):
        # spaces
        for j in range(N//2 - i + 1):
            print(" ", end=" ")

        # stars
        for j in range(2*i - 1):
            print("*", end="")
        
        print()

# Example usage:
print_star_pattern(5)