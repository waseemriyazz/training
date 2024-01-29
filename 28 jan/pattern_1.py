def print_pattern(N):
    for i in range(1, N+1):
        # spaces
        for j in range(N-i):
            print(" ", end="")    
       
        #numbers
        
        for j in range(i):
           
           print(i+j, end="")

        for j in range(i-1):
            print(i+j, end="")

        print()
            
    
# Example usage:
print_pattern(5)