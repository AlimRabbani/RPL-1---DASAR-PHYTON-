HARGA_PAKET = 120000 

jumlah_paket = int(input("Masukkan jumla paket yang di beli : "))  
harga_total_sebelum_diskon = jumlah_paket * HARGA_PAKET 

if jumlah_paket >= 10 and jumlah_paket <= 19:  
    diskon = 20 
elif jumlah_paket >= 20 and jumlah_paket <= 49: 
    diskon = 30 
elif jumlah_paket >= 50 and jumlah_paket <= 69: 
    diskon = 35
elif jumlah_paket >= 70 and jumlah_paket >= 99: 
    diskon = 40 
else : 
    diskon = 50 

harga_total_setelah_diskon = harga_total_sebelum_diskon *(100 - diskon)/100
hemat = harga_total_sebelum_diskon - harga_total_setelah_diskon 

print('harga normal per paket:Rp.', HARGA_PAKET) 
print("harga total sebelum diskon:Rp.",harga_total_sebelum_diskon) 
print("harga total setelah diskon :Rp.",harga_total_setelah_diskon) 
print("uang yang di hemat setelah diskon:Rp.",hemat)
print("Terima kasih") 



