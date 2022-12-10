# percabangan 

print("rencana setelah lulus kuliah?\n1.Kuliah\n2.kerja") 

jawaban =input("Masukkan pilihan : ") 

if(jawaban==1): 
    print("Kuliah jurusan apa?\n1.Teknik infromatika\n2.Teknik sipil") 
    jB = input("Masukkan pilihan : ")   
    if jB ==1: 
     print("kuliah di jurusan TEKNIK INFORMATIKA") 
    else : 
     print("kuliah di jurusan TEKNIK SIPIL")
else : 
    print("Kerja di industri apa ?\n1.pertambangan\n2.perikanan") 
    jwb = input("Masukkan pilihan : ") 
    if jwb ==1 : 
         print("Kerja di industri PERTAMBANGAN") 
    else : 
         print("kerja di INDUSTRI perikanan")  

# contoh 2 
buah_yang_tersedia = ['anggur','jeruk','semangka','manggis','apel'] 
print("Buah Yng Tersedia")
print(buah_yang_tersedia)
buah_yang_dicari =input("Halo , buah apa yang anda cari :") 
if(buah_yang_dicari in buah_yang_tersedia): 
    print("buah tersdia harga sekian") 
else : 
    print("buah tidak tersedia!") 

#contoh 
nilai = int(input("masukkan nilai  :"))  
usia = int(input("Masukkan usia :")) 

if (nilai >= 90): 
 if (usia < 20) : 
    print("Selamat anda di terima bekerja di perusahaan kami")
    
 else: 
    print("Selamat anda mendapatkan hadiah sebesar 10000000000000000000000000 ")  
else :
   if(usia<20):  
     print("coba lagi")
   else : 
    print("mohon maaf coba lagi yah")  