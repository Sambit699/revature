'''tup=("app","fff","dfeuf")
for i in tup:
    print(i)'''

'''for i in range(5):
    for j in range(5):
        print(j)'''

'''dis={"mmm":"cvev","ededv":3,"guegf":"fgedu"}
for k in dis.keys():
    print(k)'''

'''dis={"mmm":"cvev","ededv":3,"guegf":"fgedu"}
for k in dis.values():
    print(k)'''

"""a=10
b=20
add=a+b
sub=a-b
mul=a*b
div=a/b
flo=a//b
mod=b%a
exp=b**a
print(add,sub,mul,div,flo,mod,exp)"""

"""a=100
b=20
a+=b
a-=b
a*=b
a/=b
a//=b
b%=a
b**=a
print(a,b)"""
 
'''a=10
b=20
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)'''

'''a=[3,4,5,7]
b=5
print(b in a)
print( b not in a)'''

'''f=float(input("enter the temp in fahrenheit"))
cel=(f-32)*(5/9)
print(cel)'''
'''cel=float(input("enter the temp in cel"))
f=(cel*(9/5))+32
print(round(f,2))'''

#partten
'''for i in range(5):
    for j in range(i):
        print("*",end=" ")
    print()'''

#age calculator
'''birthyear=int(input("enter your Birth year:"))
curryear=int(input("enter current year:"))
age=int(curryear-birthyear)
print("your age is",age)'''
#Simple intrest
'''principal=float(input("enter your principle amount:"))
time=float(input("enter your time period:"))
rate=float(input("enter the interest rate:"))
si=(principal*time*rate)/100
print("sample intrest is ",si)'''
#Area calculator
#circle
'''import math
radi=int(input("enter the radious:"))
area=math.pi*radi**2
print("Area of circle is :",round(area,2))'''
#rectangle
'''length=float(input("enter the length:"))
breth=float(input("enter the breth:"))
area=length*breth
print("Area of rectangle is :",round(area,2))'''
#triangle
'''height=float(input("enter the length:"))
breth=float(input("enter the breth:"))
area=0.5*height*breth
print("Area of triangle is :",round(area,2))'''
#Grade calculator
'''grade=float(input("enter your percentage :"))
if grade>=90:
    print("your grade is A")
elif grade>=80:
    print("your grade is B")
elif grade>=70:
    print("your grade is C")
elif grade>=60:
    print("your grade is D")
elif grade>=50:
    print("your grade is E")
else:
    print("you are failed")'''
 #Tip calculator
'''totalbill=float(input("enter the total bill:"))
pertip=float(input("enter the tip % in number:"))
tip_amount=(pertip/100)*totalbill
total_pay=totalbill+tip_amount
print("Total bill you have to pay is :",total_pay)'''
#Condition & Loops
#even/odd check
'''num=int(input("enter a number"))
if num%2==0:
    print("number is even")
else:
    print("number is odd")'''
#Leap year 
'''year=int(input("enter the year"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It is a leap year.")
else:
    print("it is not a leap year.")'''
#number Guessing game
"""import random
num=random.randint(1,100)
i=0
while True:
    guessnum=int(input("enter any num between 1 to 1000:"))
    i+=1
    if guessnum>num:
        print("the num is too big")
    elif guessnum<num:
        print("the num is too loo")
    else:
        print("congrats you guess the correct number")
        break"""
#Multiplication table
'''num=int(input("Enter a number to find the table:"))
for i in range(11):
    print (i*num)'''
#prime num check
'''num=int(input("Enter a num :"))
c=0
for i in range(1,num+1):
    if num%i==0:
        c +=1
if c==2:
    print("prime")
else:
    print("not prime")'''
#Factorial
'''num=int(input("Enter a number:"))
mul=1
for i in range(1,num+1):
    mul *=i
print(mul)'''
#sum of digit
'''num=int(input("Enter a number:"))
summ=0
while num>0:
    digt=num%10
    summ+=digt
    num //=10
print(int(summ))'''
#patterns
'''for i in range(6):
    for j in range(i):
        #print(i,end=" ")
        print(j,end=" ")
    print()'''
'''for i in range(6):
    print(" " * (6 - i), end="")
    for j in range(i):
        print(i,end=" ")
    print()'''
#String Operations
#Palindrome check
'''num=int(input("Enter a number:"))
num1=num
rev=0
while num>0:
    digt=num%10
    rev=rev*10+digt
    num//=10
if(num1==rev):
    print("number is palindrome")
else:
    print("number is not palindrome")'''
#Srting reverse
'''string=input("Enter a string:")
print(string[::-1])'''