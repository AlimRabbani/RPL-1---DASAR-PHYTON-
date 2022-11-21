nama =input('masukkan nama anda = ') 
pekerjaan = input('masukkan pekerjaan =').lower() 
gaji = int(input('masukkan gaji anda ='))  
pajak1 = 2/100
pajak2 = 5/100
pajakpns = 3/100

if pekerjaan == 'pns':
    if gaji >= 10000000:
        total_pajak = gaji*(pajak1+pajakpns)
        gaji_bersih = gaji-total_pajak
        
    elif gaji >= 20000000:
        total_pajak = gaji*(pajak2+pajakpns)
        gaji_bersih = gaji-total_pajak
    
    else:
        total_pajak = gaji*pajakpns
        gaji_bersih = gaji-total_pajak

else:
    if gaji >= 10000000 and gaji < 20000000:
        total_pajak = gaji*pajak1
        gaji_bersih = gaji-total_pajak
        
    elif gaji >= 20000000:
        total_pajak = gaji*pajak2
        gaji_bersih = gaji-total_pajak
    
    else:
        total_pajak = 0
        gaji_bersih = gaji

print("Nama Lengkap: ", nama)
print("Pekerjaan: ", pekerjaan)
print("Gaji Bulanan: ", gaji)
print("Total Pajak: ", total_pajak)
print("Gaji Bersih Karyawan: ", gaji_bersih)