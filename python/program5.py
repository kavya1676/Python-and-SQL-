
#5.Count the frequency of each Character in a string.
s=input("enter a string: ")
n={}
for i in s:
    if i in n:
        n[i]+=1
    else:
        n[i]=1
print(n)
#input :kavya
# output : enter a string: kavya
#{'k': 1, 'a': 2, 'v': 1, 'y': 1}
