#contoh  statict method 
class Mahasiswa: 
    def __init__(self,nama ): 
        self.__nama = nama 

    def getnama(self): 
        return self.__nama


    def HurufKapital(nama): 
        return nama.upper() 

joko = Mahasiswa('Alim') 


print(joko.getnama()) 
print(Mahasiswa.HurufKapital(joko.getnama())) 
print(Mahasiswa.HurufKapital("alim rabbani"))   

#contoh 2  class OOP 
class mobil :  
    pass

mobil1 = mobil() 
mobil2 = mobil() 
mobil3 = mobil() 

mobil1.name = "BMW" 
mobil1.power = 10000000 
mobil1.color = "BLACK WAITE" 
mobil1.harga = 1000000000000000000000000 
print(mobil1.name) 
print(mobil1.power) 
print(mobil1.color) 
print(mobil1.harga)  

mobil2.name = "SUNNY" 
mobil2.power = 500000000000000000000000000000000 
mobil2.color = "ORANGE"
mobil2.harga = "life/tidak bisa di beli dengan papun "
print(mobil2.name) 
print(mobil2.power) 
print(mobil2.color) 
print(mobil2.harga)
mobil3.name = "SUNNY" 
mobil3.power = 500000000000000000000000000000000 
mobil3.color = "ORANGE"
mobil3.harga = "life/tidak bisa di beli dengan papun "
print(mobil3.name) 
print(mobil3.name) 
print(mobil3.power) 
print(mobil3.color) 
print(mobil3.harga) 

#contoh isntance 

class manusia : 
    def __init__(self,inputnama,inputalamat,inputumur,inputstatus): 
        self.nama = inputnama 
        self.alamat = inputalamat
        self.umur = inputumur
        self.status = inputstatus  

karyawan1 = manusia('alim rabbani' ,'mamasa',19,'mahasiswa aktif') 
karyawan2 = manusia('harun','lino maloga',50,'Duda anak dua') 


print(karyawan1.__dict__) 
print(karyawan1.nama)#untuk mengakses salah satu indeks dalam obkjek1  
print(karyawan2.__dict__) 
print(karyawan2.nama)





    

    





