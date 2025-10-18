while 1:
    n=int(input("nhap vao so nguyen n: "))
    if(n<=0):
        print("n phai la so nguyen duong")
    if(n>0): break

cs=0
while (n>0):
    cs=cs+1
    n=n//10

print("n co",cs," chu so")