#largest of three number
n1=int(input("enter the number1:"))
n2=int(input("enter the second number:"))
n3=int(input("enter the third number:"))
if n1>0 and n2>0 and n3>0:
    if n1>n2 and n1>n3:
        print("number 1 is big:",n1)
    elif n2>n3 and n2>n1:
        print("number 2 is big:",n2)
    else:
        print("number 3 is big:",n3)
else:
    print("invalid number")

