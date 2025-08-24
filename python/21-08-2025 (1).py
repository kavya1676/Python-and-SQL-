#program to print sum of digits of a number.
n=input()
l=len(n)
s=0
i=0
while(i<l):
    s+=int(n[i])
    i+=1
print(s)
#input : 1234
#output : 10
