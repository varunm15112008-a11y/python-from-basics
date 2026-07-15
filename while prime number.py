num=int(input("enter the value of num: "))
data=1
count=0
while (data<=num):
    if (num%data==0):
        count = count+1
    data=data+1
if (count==2):
    print("It is an prime number")
else:
    print("Not an prime number")
