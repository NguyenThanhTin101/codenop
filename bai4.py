import math
a,b,c=map(float,input("nhap vao 3 canh cua tam giac: ").split())

p=(a+b+c)/2
s=math.sqrt(p*(p-a)*(p-b)*(p-c))

print("chu vi tam giac= ",a+b+c)
print("dien tich tam giac= ",s)