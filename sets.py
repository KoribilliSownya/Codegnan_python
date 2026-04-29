"""
SET DATA TYPE
-----------

SET--------> set is a collection of unordered elements or unique elements unlike list list or tuple set is not permit duplicates in side.
-----------> Set is mutable.
METHODS ---
1.add()------>This method is used to add new item into the set..It only accepts one item
Syntax---->varaible_name.add(item)
Example---->s={1,2,3,2,3,4}
            print(s)
            print(s)
           s.add((5,6))
           print(s)
 ---------          
2.remove()
------------>This method is used to add new item into the set
Syntax---->varaible_name.remove(value)
--------
EXAMPLE
--------
s={1,2,3,2,3,4}
print(s)
s.remove(3)
print(s)
-------
3.pop()
--------> This is also used to delete element in the set ,but we can not specify the element
syntax--->varaible_name.pop(no arguments)
EXAMPLE
------
s={1,2,3,2,3,4,7,6,0}
s.pop()
print(s)
--------
4.clear()
------------>This method is used to delete all elements in the set.
syntax------> variable_name.clear()

EXAMPLe
------
s={1,2,3,2,3,4,7,6,0}
s.clear()
print(s)   #output-->set()

5.update()
--------->same like add(),but this method will add more than one element
syntax
------->varaible_name.update([elements])
EXAMPLE
-------
s={1,2,3,2,3,4,7,6,0}
s.update([8,9,10,11])
print(s)

6.UNION
-------->This method will return a set of all elements from both sets, but not duplicates
Syntax-->set_1.union(set_2) or set_1 | set_2
EXAMPLE
-------
s={1,2,3,4}
t={2,5,6}
print(s.union(t))  #output--->{1, 2, 3, 4, 5, 6}
print(s | t)

7.INTERSECTION
------------->This method will only give the common elements from both sets
syntax----->set_1.intersection(set_2) or set_1 & set_2
EXAMPLE
-------
s={1,2,3,4}
t={2,5,6}
print(s.intersection(t)) 
print(s  & t)

8.difference()
-------------->This method is used to get the different elements from both sets
Syntax----->set_1.difference(set_2) or set_1 - set_2
EXAMPLE
--------
s={1,2,3,4}
t={2,5,6}
print(s.difference(t)) 
print(s - t)


9.Type Convertions
-----------------> converting one data type into another data type
EXAMPLE----> INTEGER TO string and float
a=8
b=str(a)
print(str(8))
print(type(a))
print(float(a))
print(b)
print(type(b))
float --> string and int


a=80.97
b=str(a)
d=int(a)
print(a,b,d)


c="67"
i=list(c)
d=[6,7]
z=str(d)
h="[6,7,.,9,10]"
l=list(h)
print("l is :",l)
print(z)
print(i)



r=[1,2]
u=str(r)
print(type(u))
print(u)
"""
r=[1,2]
u=tuple(r)
print(u)
a="123"
b=tuple(a)
c=set(a)
print(b)
print(c)


