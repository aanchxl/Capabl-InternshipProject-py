#probability of getting 6,6,6 for 3 dice
list=[1,2,3,4,5,6]
total=0
count=0
for i in range(0,6):
    for j in range(0,6):
        for k in range(0,6):
            total+=1
            if(list[i]==6 and list[j]==6 and list[k]==6):
                count+=1
                
a=round(count/total,5)                
print("Probability of getting 6,6,6 for 3 dice is:",a)