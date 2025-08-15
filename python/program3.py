
#3.Count the number of vowels and consonants in a string.#
s=input("enter a string: ")
v=0
c=0
for i in s:
    if (i>='a' and i<='z'):
        if i in "aeiou":
            v+=1
        else:
            c+=1
print("vowels:",v)
print("consonants:",c)
#input : enter a string: i am learning python
#vowels: 6
#consonants: 11
