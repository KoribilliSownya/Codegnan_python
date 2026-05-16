"""
INHERITANCE
------------>Inheriting the methods from the base to child
class parent:
    pass
class child(parent):
    pass
-------------
single inheritance
-----------------> A child class inheritance from one base class.


class parent:
    pass
class child(parent):
    pass
class animal:
    def sound(self):
        print("Animals make sounds")
class dog(animal):
    def bark(self):
        print("Dog bark")
D=dog()
D.sound()
D.bark()
------------
Multiple inheritance
-------------->A child class inherits more than one class is called multiple inheritance.

class Father:
    def skill_1(self):
        print("Driving")
class Mother:
    def skill_2(self):
        print("Cooking")
class child(Father,Mother):
    def All_skills(self):
        print("Coding")
c=child()
c.skill_1()
c.skill_2()
c.All_skills()

#example for single-inheritance
class birds:
    def flying(self):
        print("All birds  has a features to fly")
class parrot(birds):
    def eat(self):
        print("parrots eat apple")
p=parrot()
p.flying()
p.eat()
#example for multiple:

class dsa_teac:
    def dsa(self):
        print("learning dsa")
class aptitude_teac:
    def apti(self):
        print("solving apti problems")
class py_teac:
    def py(self):
        print("learnig language")
class student(dsa_teac,aptitude_teac,py_teac):
    print("learning 3 subjects to upskill")
s=student()
s.dsa()
s.apti()
s.py()
#Multi-level--->Inherits from the other child

class grandfather:
    def house(self):
        print("Grandfather's house")
class father(grandfather):
    def land(self):
        print("father's land")
class son(father):
    def flat(self):
        print("son's flat")
s=son()
s.house()
s.land()
s.flat()
#hierarchial inheritance--> multiple child classes inherits from one base class


class father:
    def property(self):
        print("Father property")
class child_1(father):
    def car(self):
        print("first child car")
class child_2(father):
    def flat(self):
        print("second child flat")
c1=child_1()
c2=child_2()
c1.property()
c1.car()
c2.property()
c2.flat()
#Hybrid Inheritance--->


class A:
    def methodA(self):
        print("class A")
class B(A):
    def methodB(self):
        print("class B")
class C(A):
    def methodC(self):
        print("class c")
class D(B,C):
    def methodD(self):
        print("Class D")
d=D()
d.methodA()
d.methodB()
d.methodC()
d.methodD()
#super() method-->The super() method is used to call methods or constructor
#from the parent class
"""
class parent:
    def __init__(self):
        print("Parent constructor")
class child(parent):
    def __init__(self):
        super().__init__()
        print("child Constructor")
c=child()

        












