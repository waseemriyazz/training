def decimal_to_binary(N):
    binary = ""
    while N > 0:
        remainder = N % 2
        binary = str(remainder) + binary
        N = N // 2
    print(binary)


decimal_to_binary(12)