#program to print greatest number among three numbers.
a=int(input("enter a number: "))
b=int(input("enter a number: "))
c=int(input("enter a number: "))
if a>b and a>c:
    print(a,"is greater")
elif b>a and b>c:
    print(b,"is greater")
else:
    print(c,"is greater")
    
'''input : enter a number: 6
enter a number: 7
enter a number: 4
output : 7 is greater'''
