#first 20 numbers which are not divisible by 2 and 3
count=0
i=1
while(count<20):
    if(i%2!=0 and i%3!=0):
        print(i)
        count=count+1
    i=i+1