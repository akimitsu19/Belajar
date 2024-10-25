print("Program Menentukan Bilangan Yang Terbesar")
print('*****************\n')
a = int(input("Masukan Bilangan Ke 1 = "))
b = int(input("Masukan Bilangan Ke 2 = "))
c = int(input("Masukan Bilangan Ke 3 = "))

print('\n')

if(a > b) and (a > c):
    print("Bilangan Ke 1 paling besar")
elif(b > a) and (b > c):
    print("Bilangan Ke 2 paling besar")
elif(c > a) and (c > b):
    print("Bilangan Ke 3 paling besar")
else:
    print("ada dua atau tiga masukan memiliki nilai sama")