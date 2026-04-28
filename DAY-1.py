"""
->What is python? : High Level Language(No need to worry about
low level management like memeory allocation)
-> It never saves permanently ,but only save at run time.
-> Object Oriented Language(OOPs)
-> Dynamically-typed language(No need to mention data type as C)

"""
#Adding 2 Numbers
a= int(input("Enter a number1: "))
b= int(input("Enter a number2: "))
print(f"a={a}")
print(f"b={b}")

#To Check Location
a=48
b=78
print("location of variable a :",id(a))
print("location of variable a :",id(b))

#To Check Type of Variable
a=12
b="Sin"
print(a,type(a))
print(b,type(b))

