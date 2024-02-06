# 7.Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following: D 100 W 200

# D means deposit while W means withdrawal. Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100 Then, the output should be: 500

def get_balance(transaction_string):
    b = transaction_string.split(" ")
    ans = 0
    for i in range (0 , len(b)):
        if b[i]=="D":
            ans = ans + int(b[i+1])
        if b[i]=="W":
            ans = ans - int(b[i+1])

    return ans
print(get_balance("D 300 D 300 W 200 D 100"))


    