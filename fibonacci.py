
"""a=0
b=1
user_input=int(input("enter a number:"))
print(a,b,end=" ")
for i in range(1,user_input+1):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
#output
enter a number:10
0 1 1 2 3 5 8 13 21 34 55 89

-----
ARMSTRONG NUMEBR
---------
"""
"""
number=int(input("enter a number to check it is armstrong or not: "))
length=len(str(number))
total=0
for i in str(number):
    total+=int(i)**length
if total==number:
    print(f"{number} is a armstrong number")
else:
    print(f"{number} is not a armstrong number")
#output

enter a number to check it is armstrong or not: 153
153 is a armstrong number

#divisibility of 3 and 5:
num=int(input())
if num %3==0 and num%5==0:
    print(f"{num} is divisible by 3 and 5")
else:
    print(f"{num} is not divisible by 3 and 5")

#output:
15
15 is divisible by 3 and 5
enter range to know divisibilty of 3 and 5
----------
W.A.P TO PRINT THE NUMBERS F=DIVISIBLE BY BOTH 3,5

num=int(input("enter range to know divisibilty of 3 and 5"))
for j in range(1,num+1):
    if j %3==0 and j%5==0:
        print(f"{j} is divisible by 3 and 5")
#output:
enter range to know divisibilty of 3 and 5100
15 is divisible by 3 and 5
30 is divisible by 3 and 5
45 is divisible by 3 and 5
60 is divisible by 3 and 5
75 is divisible by 3 and 5
90 is divisible by 3 and 5

-------
calculate even numbers sum in a list
-------
number=[1,8,9,1,2,4]
def even_sum(number):
    sum=0
    for num in number:
        if num%2==0:
            sum+=num
    print(sum)
even_sum(number)
#output: 14

#print the sum of numbers in a list which are in the even position
number=[1,4,6,8,3,7]
sum=0
for i in range(len(number)):
    if i%2==0:
        sum+=number[i]
print(sum)
#output: 10
--------------
LAMBDA FUNCTION----->A lambda function is a small anonymous function
-------->This lambda function can take n number of arguments but can only have one expression
syntax--->lambda keyword (arguments): expression
--------->arguments → inputs to the function
-------->expression → single line of code that gets evaluated and returned

add=lambda a,b:a+b
print(add(2,4))

mul=lambda c,d:c*d
print(mul(7,8))

power=lambda e,f:e**f
print(power(2,3))

add=lambda a:a+b
print(add(5))     #output:   add=lambda a:a+b
                   #NameError: name 'b' is not defined
                   

        
add=lambda a:a+a
print(add(5))   #output:10

"""
is_even = lambda n: "Even" if n % 2 == 0 else "Odd"
print(is_even(4))   # Output: Even
print(is_even(7))   # Output: Odd

















