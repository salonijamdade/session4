
print("calculator")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.factorial")
print("exit")

while True:
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    option=int(input("enter your choice"))

    if option==1:
        print("addition is:",a+b)   
    elif option==2:
        print("subtraction is:",a-b)
    elif option==3:
        print("multiplication is:",a*b)
    elif option==4:
        print("division is :",a/b)
    elif option==5:
        fact=1
        for i in range(1,a+1):
            fact=fact*i
        print("factorial is:",fact)
    elif option==6:
        print("exit")
        break
    else:
        print("invalid option")