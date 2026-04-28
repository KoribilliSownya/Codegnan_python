#  list is a collection of different data types and it is represent by []  separated by comma

"""
a = [1,"python is a language",[2,"this is 5th class",3],56]
print(a[2])   # output [2,"this is 5th class",3]
print(a[2][1]) # output  "this is 5th class"
print(a[2][1][10]) ## output h

any=[1, "python is a language",67,68,[34,["this is python class"],78,"i'm looking for good bat"],[2,"this is 5th class",3],56]
print(any[4][1][0][14])

print(any[4])

print(any[4][1][0])

b="Python is a language"
print(b.replace("Python","Java")) Here we are doing changes only we cant modify the string so string is immuatable. we cant directly perform the operation
print(b)
----------------
methods in list
----------------
1.Append ------>This method is used to add new item into the list but it will add to the last index position of the list
 Syntax -------> variable_name.append(item)
                Only takes single argument
         new=[1,2,3]
         new.append(78)
         new.append([3,6]) output as [1,2,3,78,[3,6]]
         print(new)

 
2.Extend ------>  This method is also used to add new item into list,but this extend add as each position to each index in the list
        ------->Extend() only takes iterables
Syntax -------> Variable_name.extend(item(iterables))
Example ---->  new=[1,2,3]
        new.extend([1,78])  #output [1, 2, 3, 1, 78] it combines the new values in it
       print(new)
       new.append("Python")
       new.extend("python")  #output [1, 2, 3, 1, 78]
                           #output [1, 2, 3, 1, 78, 'Python', 'p', 'y', 't', 'h', 'o', 'n']
        print(new)
        
3.Pop ----------> pop only remove index postion value
                  This is used to delete an item from the list, this pop() remove the value based on the index position mentioned in the parameterd
                  If nothing is mentioned in the parameters,it will remove th last index position value
Syntax ---------->  Variable_name.pop(index position))

                a=[1,2,3,4]
                a.pop()
                print(a)#output [1, 2, 3]
                a.pop(2)
                print(a) #output [1,2]
                a.pop(5) #output IndexError: pop index out of range
               print(a)  



4.Remove ------->   This is also used to delete item from the list, but remove() method will delete value itself.
                    If we try to delete the value that is not in the list it shows error as x not in the list
Syntax ---------> variable_name.remove(value)
             a=[1,2,3,4]
             a.remove(4)  output is [1,2,3]
             print(a)

 Slicing()----->1. This is used to get particular part of the list,string or tuple.
                2.This will work based on the index position
Syntax --------> Variable_name[starting index : ending index]

len()---------->This method is used to find the number of items present in the list
Syntax--------->len(variable)
Example-------> a=[1,2,3,4]
               print(len(a)) output :4
               b="python is a language"
               print(len(b)) output : 20
"""
#index(value)
a=[1,2,3]
print(a.index(2))

#count()

a=[1,1,1,2,3,4]
print(a.count(2))
#insert(position,value)


a=[1,27,95,6]
a.sort()
print(a)   # sort is permanently sort where as sorted like temporary sorts the list

