#contoh method 
class Hero: 
#class variabel 

    jumlah_hero = 0 

    def __init__(self,inputName,inputHealt,inputPower,inputArmor): 
        #instance variabel  
        self.nama = inputName 
        self.healt = inputHealt 
        self.power = inputPower
        self.armor = inputArmor 
        Hero.jumlah_hero += 0 
    
    #void function,method tanpa return , tanpa argumen 
    def siapa(self):
        print("nama saya adalah" + self.nama)
    #method dengan argumen tanpa return 
    def healttUp(self,Up): 
        self.helat += Up
    #method dengan return 
    def gethealt(self):
        return self.healt
hero1 = Hero("mikasa" , 10000 , 500000 , 200)
hero2 = Hero("ymir" , 10000 , 500000 , 200) 

hero1.siapa()
hero1.healtUp(70) 
print(hero1.gethealt()) # jadi helat nya itu bakalan nambah  

        
     