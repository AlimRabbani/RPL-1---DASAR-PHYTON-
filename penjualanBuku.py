print("==========Selamat datang=========")
harga_buku = 100000

jumlah_buku = int(input("Berapa banyak buku yang anda ingin beli : ")) 
total_harga = harga_buku * jumlah_buku 

print("Total harga buku = " , total_harga)  


#Diskon penjualan produk 

harga_awal = int(input("Masukkan harga awal : ")) 
persentase_diskon = int(input("Masukkan persentase diskon(Dalam persen)  : " )) 


diskon = harga_awal * persentase_diskon / 100 

harga_setelah_diskon = harga_awal - diskon  

print(f"jumlah diskon :  {diskon:2f} ") 
print(f"harga setelah diskon : {harga_setelah_diskon : 2f}")
 

#batas angka  phyton 
total = 0 
batas = int(input("Masukkan batas angka  : "))  

for i in range(1,batas + 1): 
    total += i 


print(f"total penjumalahan dari 1 hingga {batas} adalah {total} ") 


