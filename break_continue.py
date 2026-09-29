#program for break
n=int(input("enter the numbers required:"))
for i in range(1,n+1,1):
    if i==5:
        break
    print(i)

#program for continue
n=int(input("enter the no.of number required:"))
for i in range(1,n+1,1):
    if i%5==0:
        continue
    print(i)

