# latihan perulangan membuat segitiga 

sisi = 10
# 1. menggunakan for
print("awal dari for")
count =1 
for i in range(sisi): 
    print("*"*count) 
    count += 1 
print("akhir dari for")

# 2. menggunakan while
print(20*"=")
print("awal while") 
count = 1 
while True: 
    print("*"*count) 
    count += 1  

    if count > sisi: 
        break 

print("akhir dari wahile")  

# hanya ganjil saja 
print(20*"=")
print("awal while") 
count = 1 
while True: 
    # print jika ganjil 
    if (count%2):
        print("*"*count) 
        count += 1 
    # akan kembali ke atas jika ganjil    
    else :    
        count += 1 
        continue
    
    # ini akan break jika count melebihi sisi 
    if count > sisi: 
        break  

print("akhir wahile") 

# latihan logika phyton 

print('           coffe                   ')
print("=======================================")

nama = input("Nama pelanggan : ") 
tanggal = int(input("Tanggal pembelian : ")) 
print(20*"=") 
print("    ===MENU===== ")
print(" 1 . copi gula aren               Rp.3000 ")
print(" 2 . copi ABC mocca               Rp.7000 ") 
print(" 3 . copi boba aren               Rp.20000")  
print(" 4 . MILK KHAMU                   Rp.30000") 
print("    =====MENU=====") 
h = [] 
a = 1 

menu_pesanaan = int(input("Masukkan menu pesanan(Nomor menu) : "))
if menu_pesanaan == 1 : 
    harga = 3000 
elif menu_pesanaan == 2 : 
    harga = 7000 
elif menu_pesanaan == 3: 
    harga = 20000 
elif menu_pesanaan == 4 : 
    harga = 30000 

else : 
    while True: 
        print("======Menu tidak tersedia silahkan pilih menu yang lainnya=====")
        if menu_pesanaan == 1 or menu_pesanaan == 2 or menu_pesanaan == 3 or menu_pesanaan == 4: 
            if menu_pesanaan == 1 : 
               harga = 3000 
            elif menu_pesanaan == 2 : 
               harga = 7000 
            elif menu_pesanaan == 3: 
               harga = 20000 
            elif menu_pesanaan == 4 : 
               harga = 30000  
               break
    
jumlah_pembelian = int(input("Masukkan jumlah pembelian : "))
for i in range(jumlah_pembelian): 
    h.append(harga)
while True: 
    jawab = input("Apakah anda yang ingin di tambah/dikurangi ? tambah/kurang/tidak") 
    if jawab == 'tambah': 
        tambah = int(input("Masukkan menu pesanan (nomor menu) : "))
        if tambah == 1 : 
               harga = 3000 
        elif tambah == 2 : 
               harga = 7000 
        elif tambah == 3: 
               harga = 20000 
        elif tambah == 4 : 
               harga = 30000  
        jumlah_tambahan = int(input("Masukkan jumlah pembelian : ")) 
        for i in range (jumlah_tambahan): 
            h.append(harga) 
        c = jumlah_tambahan + jumlah_pembelian 
        print("Total pesanan : " , c) 
        bayar = sum(h) 
        print("Total pembayaran : Rp.{}",format(bayar)) 
        break 
    elif jawab == 'kurang': 
        kurang = int(input("Berapa jumlah yang dikurangkan ? : "))
        for i in range (kurang): 
            if kurang <= 1 : 
                a -= kurang 
                del h[a]
                bayar = sum(h) 
                break 
            else : 
                kurang -= a 
                del h[kurang] 
                if kurang < 0: 
                    break 

        c = jumlah_pembelian - kurang 
        print("Total pemesanan : ",c) 
        bayar = sum(h)
        print("Total pembayaran : Rp.{}" .format(bayar))
        break 
    else : 
        bayar = sum(h) 
        c = jumlah_pembelian 
        print("Total pemesanan : ", c) 
        print("Total pembayaran : Rp. ", format(bayar))  
        break 

    






