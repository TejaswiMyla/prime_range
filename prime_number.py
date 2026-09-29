#print prime or not
n=int(input("enter the number:"))
counter=0
for i in range(1,n+1,1):
    if n%i==0:
        counter+=1
if counter==2:
    print("prime")
else:
    print("not prime")

