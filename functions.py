
FUNCTIONS
---------- This is a block of code that can be reusable
------->A function can only run when it is called.
------->def is the keyword is to define the function

def func_name(parameters):
    -----------
    -----------
func_name(arguments)

num=9
def even_odd(num):
    if num %2 ==0:
        print(f"{num} is even number")
    else:
        print(f"{num} is odd number")
even_odd(num)
even_odd(120)

--------
Required arguments
---------------->A function must called with the correct number of arguments,that means if function expects 2 arguments,we have to
                call function with 2 arguments not less or not more
                example:
                def even_odd(num1,num2):
                      print(num1+num2)
                even_odd(9,8)
            
 
def even_odd(num1,num2):
    print(num1+num2)     #output---->17
even_odd(9,8)

def even_odd(num1,num2):
    print(num1+num2)    
    even_odd(9,8,90) # TypeError: even_odd() takes 2 positional arguments but 3 were given even_odd(9,8,90)
--------------
default arguments --->By default,value is taken from the calling function if we dont provide arguments then it is taken from the parameters
----------

def welcome(name="sownya"):
    print(f"hello {name}")
welcome("world")
welcome("visakhapatnam")
welcome()


num=9
def number(num_1):
    print(num_1)
number(num)

---------
Keyword Arguments(**kwargs)
--------------->Here, we can send arguments with key = value syntax.By this,the order of arguments does not matter.

def sum(num_2,num_3,num):
    print(num+num_2+num_3)
sum(num=9,num_2=8,num_3=1)   #output=18

def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Sownya", age=21, hobby="Coding")


----------
variable length arguments
--------------->Adding a star(*) before the parameter bane in the function,receive a tuple of arguments and can be access
items with indices

def function(*name):
    print(name[2])
function("sownya","pavani","mahima","sandhya")


----->In Python, the * symbol is used to represent arbitrary arguments (often called *args).
It allows a function to accept a variable number of positional arguments without knowing in advance how many will be passed.

Here’s a simple example:

python
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_numbers(1, 2, 3))       # Output: 6
print(add_numbers(10, 20, 30, 40)) # Output: 100





















    
