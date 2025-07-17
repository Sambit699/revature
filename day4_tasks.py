"""def add(x,y,a):
return x+y"""
#Count the number of item in the list
'''
from collections import Counter
words=["apple","banana","apple","orange"]
count=Counter(words)
print(count)'''

#defaultdict
'''
from collections import defaultdict
d=defaultdict(int)
d['a']+=1
print(d['a'])
print(d['b'])'''

#namedtuple
'''
from collections import namedtuple
paint=namedtuple('point',['x','y'])
p=paint(10,20)
print(p.x,p.y)'''

#deque
'''from collections import deque
dq=deque([1,2,3])
dq.appendleft(0)
dq.append(4)
print(dq)
dq.pop()
dq.popleft()
print(dq)'''

#Chainmap
from collections import ChainMap
dict1={'a':1,'b':2}
dict2={'b':3,'c':4}
cm=ChainMap(dict1,dict2)
cm['b']=8
print(cm['b'])
print(cm['c'])
#regural expresion ---re
import re

