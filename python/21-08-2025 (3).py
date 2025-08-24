#program to print prime numbers between given range.
low=int(input())
high=int(input())
for i in range(low,high):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count+=1
    if(count==2):
        print(i)
    
'''input: 2
10
output: 2
3
5
7'''
