#function
'''def revature():
    print("Hello students")
revature()'''


'''def revature(marks):
    print("Hello students your marks is ",marks)
revature(90)

def revature(a,b):
    return a+b
print(revature(6,7))
'''

'''def revature(name="sam"):
    print("Hello",name)
#revature()
revature("mam")'''


'''def revature():
    name="sambit"
    age=23
    return name,age
revature("mam")'''


'''def revature(*num):
    return sum(num)
print(revature(1,2,3,4,5))'''


'''def revature(**det):
    for key,value in det.items():
        print(key,value)
print(name="ebk")'''

#dout
'''def smark():
    sub1=int(input("etner your sub1 mark"))
    sub2=int(input("enter your sub2 mark"))
    sub3=int(input("etner your sub3 mark"))
    sub4=int(input("enter your sub4 mark"))
    sub5=int(input("etner your sub5 mark"))
    summarks=sum(sub1,sub2,sub3,sub4,sub5)
smark()   

def summark(*marks):
    return sum(marks)
print(summark(smark()))'''
'''
#array
num=[10,20,30,40]
print(num)
print(num[0])
num[1]=90
print(num)
num.append(80)
num.insert(3,200)
num.remove(30)
num.pop()
del num[2]
del num[1:3]
del num #del entire array


#array module
import array
#i means int ,f for float, d for double
arr=array.array('i',[1,2,3,4,])
print(arr[2])
print(arr.tolist())#convert to list


#lambda
n=lambda x:"+ve" if x>0 else "-ve" if x<0 else "zero"
print(n(6))


sq=lambda x:x**2
print(sq(7))
'''
'''
li=[lambda arg=x:arg * 10 for x in range(1,5)]
for i in li:
    print(i())


cal=lambda x,y:(x+y,x*y)
res=cal(3,4)
print(res)'''

'''
n=[1,2,3,45,6]
even=filter(lambda x:x%2==0,n)
print(list(even))


#map
a= [1,2,34,5]
b=map(lambda x: x*2,a)
print(list(b))'''
'''
#Reduce
from functools import reduce
a=[1,2,3,4]
b=reduce(lambda x,y:x*y,a)
print(b)'''
'''# format
name="sambit"
age=23
#msg="my name is {} and my age is {} years".format("user",19)
msg="my name is {} and my age is {} years".format(name,age)
print(f"my name is {name} and my age is {age} years")
print(msg)
'''
'''
#factorial
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))'''
'''
#Decorator
# it help us to add extra function
#logging,authentication
import inspect
def decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper'''

'''
@decorator
def greet():
    print("hello")
greet()

print(inspect.signature(decorator))


#Class
class animal:
    sound="brak"
sl=animal()
print(sl.sound)'''

#init method
#it python  class ha -init-() finction
# it is atometicaly intiliazes objects attribue when an object is call
'''
class Dog:
    species="canine"

    def __init__(self,name,age):
        self.name=name
        self.age=age


dog1=Dog()
dog2=Dog("hhhh",3)

#print(dog1.name)
print(dog1.species)
print(dog2.age)
print(dog2.name)'''

'''
#3#####
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name} is {self.age}"
dog1= Dog("buddy",2)
dog2= Dog("ffrf",4)
print(dog1)
print(dog2)'''


#inheritance
'''
class Animal:
    def __init__(self,name):
        self.name=name
    def species(self):
        return "hello"
class Dog(Animal):
    def sound(self):
        return "woof"
a= Animal("generic animal")
d =Dog("Buddy")
print(a.name)
print(d.name)
print(d.sound())

#print(a.sond())
print(a.species())

print(d.sound())
print(d.species())'''
'''

#innerclass

class color:
    def __init__(self):
        self.name="green"
        self.lg=self.Lightgreen()
    def show(self):
        print("name",self.name)
    class Lightgreen:
        def __init__(self):
            self.name="light green"
            self.code="3i33r"
        def display(self):
            print("name",self.name)
            print("code",self.code)

outer=color()
outer.show()
g=outer.lg
g.display()'''
'''

#Super

class Animal:
    def species(self):
        print("hello")
class Dog(Animal):
    def species(self):
        super().species()
        print("woof")

b=Dog()
b.species()
'''
'''
#Encapsulation

class Public:
    def __init__(self):
        self.name="sam"
    def display_name(self):
        print(self.name)
obj=Public()
obj.display_name()
print(obj.name)

#protected
class Protected :
    def __init__(self):
        self._name="sam"
class Subclass(Protected):
    def display_name(self):
        print(self._name)
obj=Subclass()
obj.display_name()
   
#private
class private:
    def __init__(self):
        self.__name="sam"
    def display_name(self):
        return self.__name
obj=private()
print(obj.display_name())'''

'''
#math function
import math
print(min(2,3))
print(max(2,3))
print(abs(-3.25))
print(pow(2,3))
print(math.sqrt(64))
print(math.ceil(6.4))
'''


'''
#dict to json
import json
x={
  "name":"xyz",
  "age":45}
y=json.dumps(x)
print(y)
'''
#Json to dictonary

'''import json
x='{"name":"sam","age":23}'
z=json.loads(x)
print(z["name"])
print(z["age"])'''
'''
#Iterator
num=[1,2,3,4,5]
internum=iter(num)
print(next(internum))
print(next(internum))
print(next(internum))
print(next(internum))
print(next(internum))

#Enumators
num=[1,2,3,4,5,6]
for a,d in enumerate(num):
    print(a,d)'''

#logging
'''
import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug('Hello,Debug')
logging.info('Hello,Info')
logging.warning('Hello,warning')
logging.error('Hello,Error')
logging.critical('Hello,critical')'''



import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='app.log',
    filemode='a',
    format='%(name)s - %(levelname)s - %(message)s'

)
logging.debug('Hello,Debug')
logging.info('Hello,Info')
logging.warning('Hello,warning')
logging.error('Hello,Error')
logging.critical('Hello,critical')