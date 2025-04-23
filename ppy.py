number=int(input("Enter a number: "))
result=0
temp=number
while temp!=0:
    digit=temp%10
    result=result + digit**3
    temp=temp//10
print(result)

if result==number:
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")



