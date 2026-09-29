#zero division error
a=10
b=0
try:
    print(a/b)
except ZeroDivisionError:
    print("division by zero is not allowed")

#type error
a=10
b=input("enter b:")
try:
    print(a+b)
except TypeError:
    print("enter same data type values")

#program for value error
try:
    n=int(input("enter a number:"))
    print("n:",n)
except ValueError:
    print("Data type is not matched![enter same datatype]")
finally:
    print("program completed")

