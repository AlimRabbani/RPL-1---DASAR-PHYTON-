print("===============================================")
print("----------------Selamat datang-----------------")
print("________________________________________________") 

apel = int(input("|masukkan banyak apel yang anda inginkan  : ")) 
jeruk = int(input("|masukkan banyak jeruk yang  anda inginkan : "))
semangka = int(input("Masukkan banyak semangka yang anda inginkan  : "))



Harga_apel = 5000 
harga_jeruk = 3000 
harga_semangka = 25000
total = (Harga_apel * apel + harga_jeruk * jeruk + harga_semangka * semangka)

print("|Harga apel = Rp.5000 X",apel,"buah") 
print("|Harga jeruk = 3000 X",jeruk,"buah")
print("|Harga semangka = 25000 X",semangka,"buah") 
print("|Total bayar = Rp.",total) 
bayar = int(input("|Uang Bayar = Rp."))
print("|Kembalian = Rp. " , bayar - total)   

print("__________________________________________________")
print("--------------------Terima kasih-----------------")
print("__________________________________________________")

