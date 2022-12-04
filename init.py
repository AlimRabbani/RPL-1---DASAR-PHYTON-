class Hero : 

    def __init__(self,inputName,inputHealt,inputPower,inputArmor): 
        self.name = inputName 
        self.helat = inputHealt
        self.Power = inputPower
        self.armor = inputArmor

hero1 = Hero("alim",1000 , 1000000,5000) # jadi di sini teman teman  bisa membuat lebih dari satu objek
print(hero1.__dict__) 
print(Hero,hero1)#kalo masih bingumg tentang kelas dan objek teman teman bisa cek dengan cara seperti berikut 


#contoh 2 

class Hewan : 
    def __init__(self , inputNama,inputWarna,inputKaki): 
        self.nama = inputNama
        self.warna = inputWarna  
        self.kaki = inputKaki  

kucing1 = Hewan("catty","abu - abu" , 4) 

print(kucing1.nama) 
print(kucing1.warna) 
print(kucing1.kaki) 
print(kucing1.__dict__) 
#sampai sini paham yah soal atribut 





        

        

        




        