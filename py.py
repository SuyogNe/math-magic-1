def printfac(num):
    print("The factors of the number are:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)
num = int(input("Enter a number: "))
printfac(num)