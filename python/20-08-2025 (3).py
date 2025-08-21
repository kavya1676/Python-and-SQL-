#program to check given number is prime or not.
n=int(input())
count=0
for i in range(1,n+1):
    if(n%i==0):
        count+=1
if count==2:
    print("Prime")
else:
    print("Not prime")
'''input : 4
output : Not prime
input : 5
output : Prime
