#program for multiple return value
def calculate(a,b):
    addition=a+b
    subtraction=a-b
    multiplication=a*b
    return addition,subtraction,multiplication
#calling the function
sum_result,diff_result,product_result=calculate(10,5)

print("addition:",sum_result)
print("subtraction:",diff_result)
print("multipication:",product_result)
