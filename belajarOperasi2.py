#menentukan bilangan ganjil genap 
#mengimput angka 
angka = int(input("masukkan angka :")) 

#jika angka habis dibagi nol , maka genap 
if(angka % 2) == 0: 
    print((angka)) 
#jika angka tidak habis dibagi nol , maka ganjil 

else : 
    print("{0} adalah bilangan ganjil".format(angka)) 
#jadi misalkan anda memasukkan nilai/angka 8 maka output yg keluar adalah ("8 adalah bilangan genap")   


#mengurutkan kata sesuai abjad 
#mengimput kalimat 

kalimat = input("Tulislah sebuah kalimat :") 
#memecah kalimat menjadi kata kata 
kata = kalimat.split() #split untuk memecah kalimat menjadi kata kata 
#mengurutkan kata kata 
kata.sort() #sort untuk mengurutkan kata kata sesuai abjad 
#menampilkan kata kata yg telah di urutkan 
print("Berikut urutan kata kata :") 
for urut in kata : 
    print(urut)   

#menampilkan tabel perkalian 
#mengimput angka 
angka = int(input("Tabel perkalian : ")) 
#menghitung 10 kali dari kisaran 1 sampai 10 
for i in range(1,11): 
#menampilkan tabel perkalian 
  print(angka , 'x','i','=',angka*i)  
#if you're afraid to take a step , then you won't know how big the world is 
