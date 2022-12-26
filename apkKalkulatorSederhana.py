# Program kalkulator sederhana
# pertambahan, pengurangan, perkalian, dan pembagian
print("============================================")
print("Pilih Opsi Operasi Yang Anda Inginkan:")
print("============================================")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

pemilihan = int(input("Masukkan Pilihan (1/2/3/4):"))
bilpertama = float(input("Masukkan bilanga pertama:"))
bilkedua = float(input("Masukkan bilanga kedua:"))

if pemilihan == 1:
    jumlah = bilpertama + bilkedua
    print(bilpertama,"+",bilkedua,"=",jumlah)
elif pemilihan == 2:
    kurang = bilpertama - bilkedua
    print(bilpertama,"-",bilkedua,"=",kurang)
elif pemilihan == 3:
    kali = bilpertama * bilkedua
    print(bilpertama, "x", bilkedua, "=", kali)
elif pemilihan == 4:
    bagi = bilpertama / bilkedua
    print(bilpertama, "/", bilkedua, "=", bagi)