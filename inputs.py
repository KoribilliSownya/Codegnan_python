"""
int data type
-------------

a=int(input("enter a number: "))
print(a)
print(type(a))
-------------
String data type
--------------
b=input("enter the word: ")
print(type(b))
print(b)


a,b=map(int,input("enter two numbers: "))
print(a)
print(b)
c,d=map(int,input("enter two numbers").split(" "))
print(c)
print(d)

f,g=map(int,input("enter two numbers:").split())
print(f)
print(g)

# LIST DATA TYPE
cv=list(map(int,input("enter the number: ").split()))
print(type(cv))
print(cv)
# TUPLE DATA TYPE
tu=tuple(map(int,input("enter the numbers: ").split()))
print(type(tu))
print(tu)

#f- string or doc string

a=3
b=89
print("the addition of a and b is: ", a+b)
print(f"the addition of a and b is {a+b}")
print(f"{a} + {b} ={a+b}")



-----CONDITION STATEMENT
1.IF STATEMENT --->This is used to check condition is true or not.



an=9
if an ==9:
    print(f"an is equal to {an}")
#ELSE STATEMENT
-------------> else is fall back statement,incase if statement becomes false,it will enter into else statements
an=10
if an < 9:
    print(f"It is less than {an}")
else:
    print(f"It is not less than than 9")

a=10
b=5
if a==b:
    print(f"a and b are equal")
else:
    print(f"{a} and {b} are not equal")

----eval()---> it is a function it will automatically takes the datatype however it is mention by user input

v=eval(input("enter a : "))
print(type(v))
print(v)

age=int(input("enter your age to check eligibility: "))
if age >=18:
    print("You are eligible to vote")
else:
    print(f"you have to wait for {18-age} years")

marks=int(input("enter your marks: "))
if marks < 35:
    print(f"you are failed")
else:
    print("you are passed")
"""





























