n = int(input("Enter the value of N "))
q = int(input("Enter the value of Q "))
if q==1:
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    print(sum)
if q==2:
    pro = 1 
    for i in range ( 1 , n+1):
        pro = pro * i 
    print(pro)
