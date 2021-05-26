i=0
sum=0
avg=0
while i<11:
    n=int(input("enter the number"))
    sum=sum+n
    i=i+1
    print(sum)
    avg=sum//11
    if avg%5==0:
        print(avg,"multiply by 5")
    else:
        print(avg,"not multiply by 5")