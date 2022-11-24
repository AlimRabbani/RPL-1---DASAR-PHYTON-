nama = input('masukkan nama = ') 
golongan = input('golongan = ').upper()
lamakerja = int(input('lama kerja = '))

if (golongan == 'I'): 
    gaji = 4000000 
elif (golongan == 'II'): 
    gaji = 7000000 
elif (golongan == 'III'):
    gaji = 10000000 

else : 
    ('golongan tidak terdeteksi') 

if lamakerja > 5 : 
    bonus = lamakerja*1000000 
else : 
    bonus = 0   

    gaji_total = gaji + bonus

print('DATA GAJI KARYAWAN') 
print('nama karyawan = ', nama) 
print('golongan karyawan = ' , golongan) 
print('lama kerja karyawan = ' , lamakerja) 
print('gaji pokok = ' ,gaji) 
print('bonus gaji = ' ,gaji_total)   
# print('gaji bersih = ' , bonus)  

#latihan 

nama = input('masukkan nama = ') 
golongan = input('golongan (I/II/III)= ') .upper()
lamakerja = int(input('lama kerja anda = ')) 

if golongan == 'I' : 
   gaji = 1000000 
elif golongan == 'II': 
   gaji = 7000000 
elif golongan == "III" : 
   gaji = 10000000 
else : 
   print('cek kembali , terimakasih ') 

#bonus gaji berdasarka lama kerja  
if lamakerja > 5 : 
   bonus = lamakerja*100000 
else : 
   bonus = 0  

gaji_total = gaji+bonus

print('nama karyawan = Rp. ', nama ) 
print('golongan karyawan = ', golongan) 
print('gaji pokok karyawan = Rp. ', gaji ) 
print('bonus karyawan = Rp. ' , lamakerja) 
print('gaji bersih karyawan = Rp. ', gaji_total) 