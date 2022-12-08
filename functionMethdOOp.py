class Mahasiswa : 

    def __init__(self,inputNama,inputaAlamat,inputUmur,inputStatus) : 
        self.nama = inputNama
        self.alamat = inputaAlamat 
        self.umur = inputUmur 
        self.status = inputStatus  
    #void function,method tanpa return , tanpa argumen 
    def data(self):
        print("nama saya " + self.nama)
        print("Alamat  " + self.alamat) 
        print("umur"  + self.umur) 
        print("Status " + self.status)
   

mahasiswa1 = Mahasiswa("ALIM RABBANI","MAMASA","19","Mahasiswa") 
print("--------------------------")
mahasiswa2 = Mahasiswa("Mel","POLMAN","19","Mahasiswa") 

print(mahasiswa1.__dict__) #menampilkan semuah data pada objek pertama
mahasiswa1.data() #cara pemanggilan untuk method yang kita buat untuk objek pertama
print("________________________")
mahasiswa2.data() #objek kedua 

#next time masih di method , class , objek 
        