#contoh1
panjang = int(input("masukkan panjang segitiga: "))   
lebar = int(input("masukkan lebar segitiga: "))   
tinggi = int(input("masukkan tinggi segitiga: "))   


def segitiga(): 
    luas_segitinganya = ((panjang * lebar) + (panjang * tinggi ) + (lebar * tinggi))   
    
    
    print("hasilnya :", luas_segitinganya)  


segitiga()   
#silahkan mencoba

#contoh2

panjang = int(input("masukkan panjang segitiga: "))   
lebar = int(input("masukkan lebar segitiga: "))   
tinggi = int(input("masukkan tinggi segitiga: "))   


def segitiga(): 
    luas_segitinganya = panjang * lebar * tinggi    
    
    print("hasilnya :", luas_segitinganya)  


#Bonus 

menu_makanan = ["ayam","bakso","nasi bungkus","nasi lemak"] 
menu_pesanan = input("masukkan menu pesanan anda :")   
print("DAFTAR MENU")
print(menu_makanan)

if(menu_pesanan in menu_makanan):
    print("menu makanan yang anda pesa  tersedia") 
    print("hasrga menu pesanan anda sebesar Rp.10.000") 
    print("20 menit lagi menu yang anda pesan akan disajikan") 
else : 
    ("mohon maaaf menu yang anda pesan tidak tersedia") 
    ("silahkan pesan menu yang lain atau pulang aj ")





