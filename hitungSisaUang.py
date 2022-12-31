print(""" 
==================================
Selamat Datang di Toko Amanda Jaya
===================================
""") 

def Total(Harga, Jumlah): 
    return Harga * Jumlah 

Harga = int(input("Masukkan harga Baju  : ")) 
Jumlah = int(input("Masukkan jumlah Baju yang di beli  : ")) 

total = Total(Harga,Jumlah)  
# Diskon 5% tiap pembelian di atas Rp.100 rb 
if total > 100000: 
    total = total-0.05 * total 
    print("Total harga = Rp. " , total ) 

Bayar =int(input("Jumlah nominal uang : ")) 
kembalian = (Bayar - total) 

print("uang kembalian : Rp." , kembalian)   

print("===========Terimakasih atas kunjungannya===========") 
print("Datang lagi yah kk")  


 