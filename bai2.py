t=int(input("nhap vao so giay: "))

gio= t//3600 #số giờ bằng số giây chia 3600
a= t%3600    
phut =a//60
giay= a%60

print(gio,phut,giay,sep=":")
