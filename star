num=int(input("Enter the value of num:"))
start=0
count=0
while(start<num):
    space=num
while(space<start):
    print(" ")
    space=space-1
    star=0
while(star<=count):
    print("*")
    star=star+1
    print("\n")
    count+=2
