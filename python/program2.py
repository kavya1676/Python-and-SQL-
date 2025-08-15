
#2.Check if a String is a palindrome.
num=x
rev=0
while num!=0:
    d=num%10
    rev=rev*10+d
    num=num//10
if x==rev:
    print("Palindrome")
else:
    print("Not Palindrome")
# input:enter a number: 362
#output: Not Palindrome
