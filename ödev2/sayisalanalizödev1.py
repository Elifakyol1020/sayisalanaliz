x1=2
x2=4
i=0
while i<4:
    x = (x1 + x2) / 2
    a = x **3 -2 * x **2 - 5
    if a<0:
        x1=x
        x2=x2
    else:
        x1=x1
        x2=x
    i+=1
print("ikili bölmede bulunan kökümüz:",x1)
