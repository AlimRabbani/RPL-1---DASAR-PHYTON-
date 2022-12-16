#tidak menghasilkan output apapaun 
luas_persegi(10) 
#menghasilkan output 
print('Luas persegi dengan sisi 4 adalah :', luas_persegi(4)) 

persegi_besar = luas_persegi(100) 
persegi_kecil = luas_persegi(50) 

print('total luas persegi besar dan kecil adalah : ', persegi_besar + persegi_kecil )   

#contoh 2 

def persentase (total,jumlah): 
    if (total >=0 and total <= jumlah): 
        return total / jumlah * 100 

    return False 
#output 50 
print(persentase(30,60)) 

#output false 
print(persentase(100 , 60 )) 

#contoh 3 

kota = 'lamongan' 

def halo(): 
    print(kota) 

print('[print secara langsung]',kota) 
print('[panggil fungsi halo]', end='') 


#kita sempurnakan contoh yang di atas  

kota , profinsi = 'lamongan','jawa timur' 

def halo(): 
    profinsi = 'jawa barat' 
    print((kota , profinsi)) 

print('[PANGGIL FUNGSI HALLO()]') 
halo() 


print('\n[SECARA LANGSUNG]')
print(kota , profinsi) 







