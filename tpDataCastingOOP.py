# tipe data casting 

nama = "alim" 
usia = 19 
jomlo = True 

print(type(nama)) 
print(type(usia)) 
print(type(jomlo)) 
print("--------------------------")
#ini fungsinya agar kita bisa tau tipe data yang kita pakai 

#KONVERSI TIPE DATA (IMPLISIT) 

a = 10 / 2 
print(type(a)) 
b = 1/2 
print(type(b))  
c = 10 + 5 
print(type(c))
d = 10 + 5.0 
print(type(d)) 
e = 10.5 - 5 
print(type(e))  
print("-------------------------")

# perkalian string dan integer 
kata = 'jeruk bali' * 10 # hasilnya bakal bertipe data String 
print(kata) 
print(type(kata)) 
print("--------------")  

# STRING KE NUMERIK 

# panjang = int(input("masukkan panjang : ")) 
# lebar = float(input("masukkan lebar : ")) 
# print('luas = ', panjang * lebar)   

# print("---------------------------")

# contoh 2 
nama = 'alim' 
tahun_lahir = 2000 

print(nama + 'lahir di tahun', str(tahun_lahir))  
print(f'{nama} lahir di tahun {tahun_lahir}') # F-STRING
print("________________________________") 

# KONVERSI DARI DAN KE LIST , SET DAN TUPLE 

#CONTOH  
#list ke tuple dan ke set 
listhuruf = ['a','b','c','d','e','f','g'] 

print(listhuruf) 
print(tuple(listhuruf)) 
print(set(listhuruf)) 
print("--------------------------") 
# silahkan mencoba  

settAngka = {1,2,3,4,5,6,7,8,9,10} 

print(settAngka) 
print(tuple(settAngka)) 
print(list(listhuruf))  
print("-----------------")
#memanipulasi string part 1
template = 'Halo , saya %s dari %s' 
print(template %('alim rabbani','kec.mambi/kab.mamasa'))  
print("_______________________")

#manipulasi string part 2 
#part 2 ini kykmya lebih keren ,hehehhehe
template = 'Halo , saya {nama} dari {asal}' 
tempalte_2 = 'saya suka makan {} dan kamu awwww {}'  
template_3 = 'saat ini saya kuliah di {} dan mengambil prodi {} Hmmmm nekat {}'


print(template.format(nama = 'alim rabbani', asal = 'kec.mambi/kab.mamasa')) 
print(tempalte_2.format('nasi ayam dishub','heheheh canda yah'))
print(template_3.format('UNIVERSITAS SULAWESI BARAT','TEKMIK INFORMATIKA','bukan hehehe'))
print("_________________________________")
#part 3 
print('halo selamat pagi'.upper()) 
print('Halo selamat siang'.upper())

salam = "assalamualaikum warahmatullahi awabarakatu" 
print(salam) 
print(salam.upper) 
print("___________________________________")

#part 4 

print("APA KABAR SAHABATKU ?".lower()) 
print("lagi dimana ?".lower()) 
print("SAMA SIAPA ?".lower())  
print("_____________________________________")

#part 5 
print("melihat senyumanmu yang tadi membuatku ingin menjadi pendamping hidupmu".title()) 
print("SEMUAH TENTANG KITA".title())  

 
#part 6 
print("masa depan ? masa depan seseorang tergantung pada seseorang itu sendiri".swapcase()) 
print("kamu harus bisa".swapcase())  

#silahkan mencoba 













