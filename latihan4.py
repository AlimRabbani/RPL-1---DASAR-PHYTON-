# nama_karyawan = input('masukkan nama nada = ') 
# gaji_pokok = int(input('masukkan gaji pokok anda = ')) 
# jumlah_anak = int(input('jumlah anak = ')) 
# status_istri = input('Sudah punya istri? = ').lower()
# tunjangan_anak = 5/100 
# tunjangan_istri = 2/100 
# pajak = 10/100 


# bonus_anak = gaji_pokok*tunjangan_anak*jumlah_anak

# if status_istri == "ya":
#     bonus_istri = gaji_pokok*tunjangan_istri 
# else:
#     bonus_istri= 0

# gaji_total_nonpajak = gaji_pokok+bonus_anak+bonus_istri
# total_tunjangan = bonus_anak * bonus_istri
# total_pajak = gaji_total_nonpajak*pajak
# gaji_bersih = gaji_total_nonpajak-total_pajak

# print('nama = ', nama_karyawan)   
# print('gaji pokok = ', gaji_pokok)    
# print('jumlah anak = ' , jumlah_anak)   
# print("Bonus tunjangan anak= ", bonus_anak) 
# print("Bonus tunjangan istri = " , bonus_istri) 
# print('gaji sebelum pajak = ' , gaji_total_nonpajak) 
# print('total tunjangan = ' , total_tunjangan) 
# print('total pajak = ' , total_pajak) 
# print('gaji bersih anda = ' , gaji_bersih)  


nama = input('masukkan nama = ') 
gaji_pokok = int(input('input masukkan gaji = '))   
jumalah_anak = int(input('jumlah anak = ')) 
status_pernikahan = input('sudah beristri = ').lower() 
tunjanganper_anak = 5/100 
tunjangan_istri = 2/100 
pajak = 10/100 

total_tunjangan = gaji_pokok * tunjanganper_anak *jumalah_anak   

if status_pernikahan == "ya": 
    bonus_istri = gaji_pokok*tunjangan_istri 
else : 
    bonus_istri = 0  

    gaji_total_nonpajak = gaji_pokok+tunjanganper_anak+bonus_istri 
    total_asuransi = tunjanganper_anak * bonus_istri
    total_pajak = gaji_total_nonpajak*pajak
    gaji_bersih = gaji_total_nonpajak-total_pajak 



print('nama = ', nama)   
print('gaji pokok = ', gaji_pokok)    
print('jumlah anak = ' , jumalah_anak)   
print("Bonus tunjangan anak= ", total_tunjangan) 
print("Bonus tunjangan istri = " , bonus_istri) 
print('gaji sebelum pajak = ' , gaji_total_nonpajak) 
print('total tunjangan = ' , total_tunjangan) 
print('total pajak = ' , total_pajak) 
print('gaji bersih anda = ' , gaji_bersih)   








