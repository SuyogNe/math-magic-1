def roman_int(n):
    roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    intg=0
    for i in range(len(n)):
        if i+1<len(n) and roman[n[i]]<roman[n[i+1]]:
            intg-=roman[n[i]]
        else:
            intg+=roman[n[i]]
    return intg
n=input("Enter a roman number: ")
print(roman_int(n))