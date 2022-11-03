#menghitung volume kubus 
#menginput sisi kubus 
sisi = float(input('Tulis sisi kubus :')) 
#hitung volume kubus  
volume = sisi ** 3
#menampilkan hasil perhitungan 
print('volume kubus adalah %0.2f'%volume) 

#Menukar nilai variabel 
#mengimput nilai variabel 
x = input('Tuliskan nilai x :') 
y =input('tuliskan nilai y :') 
#membuat variabel tukar dan menukar nilai variabel lain 
tukar = x 
x = y 
y = tukar 
#menampilkan nilai varibel setelah ditukar 
print('nilai x setelah ditukar adalah :{}'. format(x)) 
print('nilai y setelah ditukar adalah: {}'. format(y)) 

#menampilkan angka acak antara 0 sampai 10 
#yg pertama yg harus kita lakukan adalah mengimpor modul random 

import random 
#menampilkan angka acak 
print(random.randint(0,10)) 

