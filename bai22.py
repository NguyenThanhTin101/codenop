while 1:
    n=int(input("nhap vao so nguyen n: "))
    if(n<=0):
        print("n phai la so nguyen duong")
    if(n>0): break

s=0
for a in range(n+1):
    s=s+a

print("tong cac so tu 1-n la: ",s)