#menjumlahkan dua angka 
angka1 =input('Tulis angka pertama :') 
angka2 =input('Tulis angka kedua : ') 

#supaya nilai yg nannti keluar dari angka 1 dan 2 itu tidak bernilai string maka kita harus mengonversi angka 1 dan 2 ke integer
#dengan cara : 

sum = int(angka1) + int(angka2) 

#menampilkan hasil penjumlahan 
print('hasil penjumlahan {0} dan {1}adalah{2} '. format (angka1 ,angka2 ,sum))

#menghitung akar kuadrat 
angka = float(input('tuliskan angka :')) 

#menghitung akar kuadrat 
akar_kuadrat = angka ** 0.5 
#nenampilkan hasil akar kuadrat 
print( 'akar kuadrat dari 0%.3f adalah 0%.3f'%(angka , akar_kuadrat))  

#menghitung luas segitiga 
#1 . mengimput alas dan luas segitiga 
alas =float(input('Tulis alas segitiga :')) 
tinggi =float(input('Tulis tinggi segitiga :')) 
#Hitung luas segitiga 
luas = (alas * tinggi) /2 
#menampilkan hasil perhitungan 
print('Luas segitiga adalah %0.2f' %luas) 


