"""
-------
list comprehension
--------------->List comprehension offers shorter syntax when we we want to create a new list based on the values  of an
                exisiting list.
 syntax------->[expression loop condition]
-------------
2.Dictionary comprehension
---------------->Dict comprehencion offers shorter syntax when we want to create a new dict based on the values of an existing dict.
 syntax--------->{expression loop condition}

old=[1,2,3,4,5]
new=[i for i in old]
print(new)
#output:[1,2,3,4,5]

old=[2,5,8,14,80,1,5,6]
new=[i if i%2==0 else 'odd' for i in old]
print(new)
#output--->[2, 'odd', 8, 14, 80, 'odd', 'odd', 6]


old=[2,5,8,14,80,1,5,6]
new=[i if i%2!=0 else 'even' for i in old]
print(new)
#output---->['even', 5, 'even', 'even', 'even', 1, 5, 'even']
#dictionary comprehension
"""
some={'a':2,'b':3,'c':5}
result={x:y for(x,y) in some.items() if y%2==0}
print(result)
some={'a':2,'b':3,'c':5}
result={x:y for(x,y) in some.items()if y%2==0}
print(result)
