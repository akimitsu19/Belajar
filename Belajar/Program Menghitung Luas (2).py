print("Program Menghitung Luas")
print('** *** *** *** *** *** **')
print('\n')
print("Pilih Menu")
print('=====> 1. Luas Lingkaran')
print('       2. Luas Persegi')
print('       3. Luas Segitiga')
print('\n')
pilihan = int(input("Masukan Pilihan = "))
print('\n')

if pilihan == 1:
    print("Program Lingkaran")
    print('************/n')
    print('\n')
    jari = int(input("Masukan jari-jari = "))
    luas = 3.14 * jari * jari
    print("Luas adalah :", luas)
elif pilihan == 2:
    print("Program Persegi Panjang")
    print('===============\n')
    print('\n')
    panjang = int(input("Masukan Panjang = "))
    lebar = int(input("Masukan Lebar = ")) 
    luas = panjang * lebar
    print("Luas adalah :", luas)
elif pilihan == 3:
    print("Program Segitiga")
    print('===========\n')
    print('\n')
    a = int(input("masukan Alas = "))
    t = int(input("Masukan Tinggi = "))
    luas = 0.5 * a * t
    print("Luas adalah :", luas)
else:
    print("Pilihan Menu Tidak Ada")   