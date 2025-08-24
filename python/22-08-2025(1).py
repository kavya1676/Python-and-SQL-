#program to check given number is palindrome or not.
n=int(input("enter a number : "))
temp=n
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if(rev==temp):
    print("palindrome")
else:
    print("Not palindrome")
'''input : enter a number : 1221
output : palindrome
input : enter a number : 654
output : Not palindrome'''
