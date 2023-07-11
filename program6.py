#program to count the number of sentences in a string
str=input("Enter a string: ")
count=0
for i in range(0,len(str)):
    if(str[i]=='.' or str[i]=='?' or str[i]=='!'):
        count=count+1
print("Number of sentences in string are:",count)
