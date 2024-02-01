# Case 1: All the characters in the string are ‘a’. This will give us only 1 possible string.
# Case 2: One character ‘b’ and remaining ‘a’. Using permutations and combinations we can say the number of possible strings will be (N! / (N-1)!) i.e. N.
# Case 3: One character ‘b’, One character ‘c’ and remaining ‘a’. Using permutations and combinations we can say the number of possible strings will be (N! / (N-2)!) i.e. N*(N-1).
# Case 4: One character ‘b’, Two characters ‘c’ and remaining ‘a’. Number of possible strings will be (N! / (2! * (N-3)!)) i.e. N*(N-1)*(N-2)/2.
# Case 5: One character ‘c’ and remaining ‘a’. Similar to case 2. So, we can say the number of possible strings will be N.
# Case 6: Two characters ‘c’ and remaining ‘a’. Number of possible strings will be (N! / (2! * (N-2)!)) i.e. N*(N-1)/2.
# Adding all the above cases we get the formula: 1 + 2*N + N*(N*N - 1)/2.
n = int(input("Enter the length of string : "))
ans = 1 + 2*n + n*(n*n - 1)/2
print(ans)