# CLASS OPP PHYTON INSTANCE VARIABLE 
class PELAMAR_KERJA : 

    def __init__(self,inputName,inputAlamat,inputStatus,inputkeahlian,inputKesukaan): 
        self.name = inputName 
        self.almat = inputAlamat
        self.status =inputStatus
        self.kemampuan = inputkeahlian 
        self.kesukaan = inputKesukaan

manusia1 = PELAMAR_KERJA("ALIM RABBANI","KAB.MAMASA IN KEC .MAMBI","Mahasiswa","KERJA BANGUNAN","saya suka kalian semuah")
manusia2 =  PELAMAR_KERJA("MONKEY D LUFFY","ONE PIECE","Bajak laut","BERTARUNG","saya suka kalian semuah")
manusia3 =  PELAMAR_KERJA("ultaraman","GALAKSI ULTRAMAN","PAHLAWAN JEPANG","BERTARUNG","SAA SAA SAA SEBENERNYA BEBAN SIH")


print("PROFIL PELAMAR KERJA 2022")
print(manusia1.name)
print(manusia1.almat)
print(manusia1.status)
print(manusia1.kemampuan) 
print(manusia1.kesukaan)
print(manusia1.__dict__)  
print("PROFIL PELAMAR KERJA 2022")
print(manusia2.name)
print(manusia2.almat)
print(manusia2.status)
print(manusia2.kemampuan) 
print(manusia2.kesukaan)
print(manusia2.__dict__) 
print("PROFIL PELAMAR KERJA 2022")
print(manusia3.name)
print(manusia3.almat)
print(manusia3.status)
print(manusia3.kemampuan) 
print(manusia3.kesukaan)
print(manusia3.__dict__) 

        



#latihan CLASS OOP PHYTON 
#contoh sederhana 
class Laptop : 
    pass 

laptop1 = Laptop() # objek dan class 
laptop2 = Laptop() 
laptop3 = Laptop() 

laptop1.name = "ASUS MDAO AMD Ryzen 3 3500 U" 
laptop1.power = 10000
laptop1.color = "blacak wait" 
laptop1.layar = "IPS" 
laptop1.ukuran = "14 inci"
print("SPESIFIKASI LAPTOP") 
print(laptop1.name) 
print(laptop1.power)
print(laptop1.color)
print(laptop1.layar) 
print(laptop1.ukuran)
print(laptop1.__dict__)  

laptop2.name = "LENOVO IP SLIM 3 AMD Ryzen 5 5500 U" 
laptop2.power = 50000 
laptop2.color = "black panter" 
laptop2.layar = "IPS" 
laptop2.ukuran = "15 inci" 
print("SPESIFIKASI LAPTOP") 
print(laptop1.name) 
print(laptop1.power)
print(laptop1.color)
print(laptop1.layar) 
print(laptop1.ukuran)
print(laptop1.__dict__)  


laptop3.name = "ACAER SWIF 3 AMD Ryzen 5 5400 U" 
laptop3.power = 350000 
laptop3.color = "black orange" # ngakak sih 
laptop3.layar = "IPS" 
laptop3.ukuran = "14 inci" 
print("SPESIFIKASI LAPTOP") 
print(laptop1.name) 
print(laptop1.power)
print(laptop1.color)
print(laptop1.layar) 
print(laptop1.ukuran)
print(laptop1.__dict__)  


 





        
     

     
   
        
    

 