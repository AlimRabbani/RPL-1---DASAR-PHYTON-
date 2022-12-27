print("=============Selamat Datang=============")

harga_semen = 60000
jumlah_semen = int(input("Masukkan jumlah sak semen yang dibeli: "))

total_harga = 0

if jumlah_semen >= 100:
  total_harga += 0.02 * total_harga

if jumlah_semen >= 200:
  total_harga += 0.05 * total_harga

total_harga += jumlah_semen * harga_semen


print("------------------------------------------")
print('=============Berikut Lapirannya===========')
print('------------------------------------------')
print("Harga semen per sak : Rp. " , harga_semen)
print("jumlah semen yang di beli : " , jumlah_semen)
print("Total harga yang harus dibayarkan: Rp", total_harga) 
print('==============Terimaksih==================') 

