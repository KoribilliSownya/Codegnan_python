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
"""
any="koribilli"
empty=""
for i in range(len(any)-1,-1,-1):
    empty+=any[i]
print(empty)




















