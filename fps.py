
#loops  in python
# range function in python

#list object
num_list =[]

week_days_list =[
    "SUNDAY",
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY"]


for num in range (1,11):
    print(f"The range from 1 to 10 is:-->{num}")
    num_list.append(num)

print(num_list)

counter = 0
for day in week_days_list:
    counter += 1
    print(f"The {counter} day is :-->{day}")


for position in range (1,len(week_days_list)):
    print(f"The {position} position in day is:-->{week_days_list[position]}")

odd_list =[]
even_list =[]
def filter_odd_even(user_provided_number):
    for num in range (1,user_provided_number+1):
        if num % 2==0:
            even_list.append(num)
        else:
            odd_list.append(num)

def any_num():
 any_num = int(input("Please provider any number"))
 filter_odd_even(any_num)

 print(f"Now, the odd list is:{[odd_list]}")
 print(f"Now, the even list is:{[even_list]}")
   

# ask a num with user and filter odd and add into the odd list
# ask a num with user and filter even and add into the even list
# ask a num with user and check he/sh is eligible for vote (must be greater then 19)or
#Application of loop into the weeks of day:
  #for eg:
        # Day 1 is -->sunday
        # Day 2 is -->monday
# Ask a first_name and second_name from user and return its full name as:
# for eg : Oh! So,year fullname is: John Dee
