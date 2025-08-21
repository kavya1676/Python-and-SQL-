#program to check whether it is a leap year or not.
n=int(input("enter a year : "))
if n%4==0 and n%100!=0 or n%400==0:
    print("Leap year")
else:
    print("Not a leap year")

'''input :enter a year : 1996
output : Leap year
input : enter a year : 1996
output : Leap year'''
