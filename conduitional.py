age= int(input("Please provide your age:"))

#conditional statement
#if block only

print("Code started.....")
if age>18:
   print("you can play this game because yuo are above {age}")
print("Code ended.....")

#if-else block
if age>18:
    print("you can play this game because yuo are above {age}")
else:
    print("You need to be above 18 years to play this game")    


## proper use of if-elif-else block



if age<0:
    print("please input your valid age")
elif 0<age<=10:
    print("So you are kid,your movie ticket is Nrs.100")
elif 10<age<20:
    print("Your movie ticket is Nrs.200")
else:
    print("Your movie ticket is Nrs.300") 

