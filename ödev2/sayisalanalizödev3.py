import math
x1=2
i=0
while i<4:
    a=(4*math.e**(-0.5*x1))-x1
    b=(-2*math.e**(-0.5*x1))-1
    c=x1-(a/b)
    x1 = c
    i+=1
print("Newton-raphson yöntemi ile bulanan kökümüz:",x1)