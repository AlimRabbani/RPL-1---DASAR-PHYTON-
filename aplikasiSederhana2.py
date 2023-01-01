
print ("============Selamat Datang Di Rokok Store============")
print("=============Silahkan belanja==============") 

#Untuk lebih mudah dalam menentukan total harga nanti kita pakai variabel (nomo1 dst)
Diskon = 10/100
Nomor1 = str(input("Masukkan merek rokok: "))
Nomor2 = int(input("Masukkan Harga rokok : "))
Nomor3 = int(input("Masukkan Jumlah rokok Yang Di Beli :  "))
Nomor4 = int(input("Jumlah Uang Yang Di Bayar : "))

Total = (Nomor2 * Nomor3 - Nomor4 ) 



print("Merek  rokok yang di beli = " , Nomor1)
print("Harga rokok yang di beli = " , Nomor2) 
print("Banyak rokok yang di beli  = " , Nomor3) 
print("Jumlah yang di bayar = " , Nomor4) 
print("Total kembalian = Rp." , Total) 

print("|============Terimakasih=============|") 

