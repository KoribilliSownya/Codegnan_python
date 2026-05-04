"""
-------
pattern programs
---------
TRIANGLE PROGRAM USING STAR
------------
num=5
for j in range(1,num+1):
    print("*" * j)

num=int(input("Enter a number: "))
for i in range(1,num+1):
    for  j in range(1,i+1):
        print("*",end="")  --------> to get  side by side we use end
    print()    ---------------------> to end the for loop so that we will get the output in next line. 
#output:
Enter a number: 5
*
**
***
****
*****

--------------------------------
pattern printing by using numbers
--------------------------------

num=int(input("enter a number"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
enter a number6
1
12
123
1234
12345
123456

# Reverse pattern

num=int(input("enter a number: "))
for i in range(num,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()

num=int(input("enter a number: "))
for i in range(num,0,-1):
    for j in range(1,i+1):
        print(i,end="")
    print()

enter a number: 5
55555
4444
333
22
1

num=int(input("enter a number: "))
for i in range(num,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()
#output
enter a number: 5
12345
1234
123
12
1
-----------
pyramid pattern
-------------

num=int(input("enter a number: "))
for i in range(num):
    for j in range(num-i-1,0,-1): #------------>it specifies the position of where we have to start num-i-1 tell the cursor where it is
        print(" ",end="")
    for k in range(i+1):
        print("* ",end="")#----->"*space give the requires output for pyramid
    print()
enter a number: 5
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
"""
num_1=int(input("Enter number 1: "))
num_2=int(input("enter number 2: "))
choice=int(input("enter what operation you would like to perform\n 1.ADD\n 2.SUB\n 3.MUL\n 4.DIV\n 5.floor division\n 6.power\n "))
if choice==1:
    print(num_1 + num_2)
elif choice ==2:
    print(num_1 - num_2)
elif choice ==3:
    print(num_1 * num_2)
elif choice ==4:
    print(num_1 / num_2)
elif choice ==5:
    print(num_1 // num_2)
elif choice ==6:
    print(num_1 ** num_2)






























