#contoh 1 

class Angka :
    def __init__(self , angka): 
        self.angka = angka 


    def __add__ (self , objek): 
        return self.angka + objek.angka 

x1 = Angka(10) 
x2 = Angka(20) 

print(x1.angka) 
print(x1 + x2)  

# contoh 2 

class Dunia : 
    def __init__(self): #magic mathod 
        print("hallow dunia") 
alim = Dunia() 
alim1 = Dunia()  

#contoh 3 '

class Segitiga : 
    def __init__(self, a,t): 
        self.alas = a 
        self.tinggi = t 
    def __str__(self):
        luas = 0.5 *self.alas * self.tinggi 
        return f'segitiga(alas={self.alas}={self.tinggi} luas={luas})' 

a = Segitiga(10 , 3) 
b = Segitiga(20 , 2)

print(a) 
print(b) 
        


        
        