while 1:
    n=int(input("nhap vao so nguyen n: "))
    if(n<=0):
        print("n phai la so nguyen duong")
    if(n>0): break
sl=0
for a in range(n):
    if(a%2 !=0):
        sl=sl+a
print("tong cac so le nho hon n la ",sl)

sc=0
for a in range(n):
    if(a%2 ==0):
        sc=sc+a
print("tong cac so chan nho hon n la ",sc)
