"""
TUPLE----->Tuple is a collection of different data types that represent by () and the items in the tuple is separated by comma....
          2.Tuple are immuatble  t = (10, 20, 30)
                                 t[0] = 100   # trying to change value but it will give an error
          3.Tuple is ordered --> this means position is specified we can do indexing
"""

'''
tup=(1,"python",[1,2],(5,0),1)
print(tup)

tup1=(1,2,3)
tup2=(1,4,5,6)
print(tup1 + tup2)'''

'''DICTIONARY ----> Dict is a collection of key :value pair,where keys are immutable (string,int and tuple) and values we can take any data type.
                 we represent in {}
                  keys must be unique.
METHODS---
1.keys()---->this method is used to access only keys in the dictionary
syntax ---->dict.keys()

2.values()-----> >this method is used to access only values in the dictionary
syntax ---->dict.values()

3.items()----->This method is used to access key : value pair in the dictionary.
Syntax--------> dict.items()

4.clear()---> This method is used to delete all the items in the dictionary
syntax----->dict.clear()

5.Update() ----> This method is used to add new item(key:value)into the dictionary
Syntax -----> dict.update({key:value})



my={"Name":"Sownya",
    "age" : 21,
    "Edu":"B.Tech",
    }
print(my)
print(type(my))
print()
print(my.keys())
print()
print(my.values())
print()
print(my.items())
print()
print(21 == my['age']) ----> here output is true beacuse  we directly take the 21 which is exactly in the value

an='21'
if an in my['age']: ---->here 21 is in string format and we have value in int so thats why error
    print("yes")
else:
    print("No")    ----> it shows error

print("Sownya" in my["Name"])
print()
print('21' in my['age'])

my.update({"Role":"python developer"})
print(my)

my={"Name":"Sownya",
    "age" : 21,
    "Edu":"B.Tech",
    }
print(my['Name'])
print("sownya" in my.values())

t=("s","u","s","s")
print(max(t))
num=(1,2,3,4,5,2,2)
print(max(num))

t = ([1, 2], [3, 4])
t[0][0] = 100
print(t)
# output as ([100, 2], [3, 4])  Tuple is immutable ✅
But it contains lists (mutable objects) inside

So:
👉 Tuple structure cannot change, but mutable elements inside it can change


'''

t = (10, 20, 30)
b = t   # copying reference but here b=(10,20,30) after we are adding the value  but it doesnot getting add to b only to t=(10,20,30,40)

t = t + (40,)
print(t)

print(b)
print(t)
'''
l=[1,2,3,4]
s=l
l.append(5)
print(l)      ----->here in both s and l the output will be [1,2,3,4,5]
print(s)
'''
a=[1,2,3]
print(a)
a[1]=90
print(a)
a.insert(2,99)
print(a)

d = {'x': [1, 2, 3]}
a = d['x']
b= d.copy()
print(b)


print(a)

