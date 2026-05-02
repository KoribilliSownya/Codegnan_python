"""
elif statement
------> This statement gives more options to get result of that program
example

marks_stu=int(input("enter your marks: "))
if marks_stu>=90:
    print("A+")
elif marks_stu>=80:
    print("A")
elif marks_stu>=70:
    print("B+")
elif marks_stu>=60:
    print("B")
elif marks_stu>=50:
    print("C+")
else:
    print("Failed")
---------
Nested if statement
---------------- If statement in side another if statement is called Nested if statement

user_sbi_info={"ATM PIN": "1234"}
user_pin=input("please enter your pin: ")
if len(user_pin) == 4:
    if user_pin in user_sbi_info["ATM PIN"]:
        print("WELCOME TO SBI")
    else:
        print("You have entered the wrong pin enter the correct pin")

else:
    print("please enter 4 digit pin")

--------
FOR STATEMENT
-----------
-----> for statement is used to increase to iterate over items like (string, list,tuple) with fixed number of iterations
------
EXAMPLE
------
any=[11,22,33,25,67]
for j in any:
     print(j)

------
ELSE STATEMENT IN FOR
--------
After completing all iterations this else statement will execute


any=[11,22,33,25,67]
for j in any:
     print(j)
else:
    print("Loop finished")

s="sownya"
empty=""
for j in s:
    empty=j+empty
print(f"reversed of {s} is {empty}")

so="madam"
empty=""
for j in so:
    empty=j + empty
if empty == so:
    print("Palindrome")
else:
    print("Not a palindrome")

any="koribilli"
empty=""
for i in range(len(any)-1,-1,-1):
    empty+=any[i]
print(empty)

----while statement
-------->This statement will keep on executing until unless condition becomes true

v=1
while v <=5:
    print(v)
    v+=1

range()---->This range() will generate sequence numbers upto the limit
syntax----> range(starting,ending,step) step is optional

choice_u=int(input("Enter the limit: "))
for j in range(100,choice_u+1,2): # j here as a instance variable or temporary variable
    print(j)


for i in range(2,50+1):
    if i % 2==0:
        print(f"{i} is even number")
    else:
        print(f"{i} is odd number")

break
------>This break statement will execute if the condition becomes true and never enters into next loops


any=["pavani","mahima","sownya","indhrani"]
for i in any:
    print(i)
    if i=="sownya":
         break


-----
Continue
---------> This statement will skip that particular itteration and goes to next iterations

any=["pavani","mahima","sownya","indhrani"]
for i in any:
    if i =="sownya":
        continue
    print(i)

pass
----->Pass is space holder,holds the space not to get any error



for i in range(1,10): # it will gives error
     pass           #-----> it will not give error


a=9
b=90
if a >=b:
    pass

number=int(input("enter number to check prime or not: "))
count=0
for i in range(1,number+1):
    if number % i==0:
        count+=1
if count==2:
    print(f"{number} is a prime")
else:
    print(f"{number} is not a prime")


----
Nested Loop
----------> A loop in side the loop is called nested loop
"""
for j in range(2,100):
    count=0
    for an in range(1,j+1):
        if j % an ==0:
            count+=1
    if count==2:
        print(f"{j} is a prime")
    else:
        print(f"{j} is not a prime")


















