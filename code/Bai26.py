n = 0
while (n <= 0):
    n = int(input('Nhap so nguyen duong n: '))
while (n > 0):
    n = n / 2
    if (n == 1):
        print ('n thuoc dang 2^k')
        break
    elif (n != int(n)):
        print ('n khong thuoc dang 2^k')
        break
    