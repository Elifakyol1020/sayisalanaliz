import math
a=math.pi/5
x=math.cos(a)
z=math.cos(0)-(math.sin(0)*(a-0))
kesmehata1=x-z
print('bir terimli taylor seri aciliminda olusan kesme hatasi:',kesmehata1)
e=math.cos(0)-(math.sin(0)*(a-0))-(math.cos(0)*a*a/2)
kesmehata2=x-e
print('iki terimli taylor seri aciliminda olusan kesme hatasi:',kesmehata2)
