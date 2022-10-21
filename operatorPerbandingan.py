#operator perbandingan PHYTON
#contoh 1 , perbandingan nilai  a dan b menggunakan operator perbandingan 
# variabel nilai
a = 10 
b = 5  

print('a == b hasilnya ' , a==b) # a sama dengan b (==) hasil False 
print('a != b hasilnya' , a!=b) # a tidak sama dengan b (!=) hasil True 
print (' a > b hasilnya ' , a > b)# a lebig besar dari b(>) hasil True 
print('a < b hasilnya ' , a < b)# a lenih kecil dari b(<) hasil False  
print (' a >= b hasilnya ' , a >= b)# a lebih besar / sama dengan b(>=) hasil True 
print (' a <= b  hasilnya ' , a <= b)# a lebih kecil / sama dengan b(<=) hasil False

#operator perbandingan  tidak hanya untuk tipe data angka saja , tapi bisa juga kita pakai untuk berbagai tipe data lain seperti String .
# berikut contohnya 
#perbandingan string bersifat case sensitive 
print("--------------------------")
print('LuffyTaro' == 'LUffyTaro') #hasil akan bernilai False
print('Zorojuro' =='Zorojuro') #hasil akan bernilai True
print('12345' == 12345)# akan bernilai False 
print('1234' != 1234) # akan bernilai True



