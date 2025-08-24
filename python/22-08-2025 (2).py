#program to check the given number is armstrong or not.
n=int(input())
l=len(str(n))
temp=n
sum=0
while(n>0):
    rem=n%10
    sum=sum+pow(rem,l)
    n=n//10
if(temp==sum):
    print("Armstrong number")
else:
    print("Not a armstrong number")
#input : 46
#output : Not a armstrong number
