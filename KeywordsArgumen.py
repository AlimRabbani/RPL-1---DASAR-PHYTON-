#Named parameter/keyword arguments 
#contoh penggunaan 
def foo (vin1 , vin2 , vin3): 
    #isi fungsi di sini 
    #isi fungsi di sini 
    foo(vin1 = 10 , vin2= 17 , vin3= 5) 
#contoh penggunaannya ! 

#contoh 2 

def pangkat(angka,pangkat = 2) :
    hasil = 1
    for i in range(0,pangkat):
        hasil = hasil * angka 
    return hasil; 
print(pangkat(5) ) # 25
print(pangkat(5,4) ) # 625 
print(pangkat(6,6) ) # 46656 

#program di atas digunakan untuk mencari sebuah hasil dari pangkat 

#contoh 3
def pangkat(angka,pangkat = 2) :
    hasil = 1
    for i in range(0,pangkat):
        hasil = hasil * angka 
    return hasil;  
print(pangkat(angka = 4 , pangkat = 3)) #64 
print(pangkat(pangkat = 2,angka = 9)) #81 

#terimakasih 


