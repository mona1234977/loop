num=int(input("enter the number"))
sum=0
a=num
while a>0:
    d=a%10
    sum=sum+d**3
    a=a//10
if sum==num:
    print(num,"armstrong number")
else:
    print(num,"not an armstrong number")


