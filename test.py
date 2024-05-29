def div(n,m):
    count = 0
    num = 1
    while count < 5:
        if num % n == 0 and num % m == 0:
            print(num)
            count += 1
        num += 1


div(2,5)
    
