#contoh 1 overriding phyton 

class Kendaraan : 
    def berjalan(self): 
        print('berjalan...') 

class mobil(Kendaraan): 
    def berjalan(self): 
        print('berjalan dengan sangat cepat..') 

sepeda = Kendaraan() 
sedan = mobil() 

sepeda.berjalan()
sedan.berjalan() 

# contoh 2 

class Kendaraan : 
    def berjalan(self): 
        print('berjalan...') 

class mobil(Kendaraan): 
    def berjalan(self , kecepatan , satuan = 'km/j'): 
        super().berjalan()
        print(f'  ---->>>> berjalan dengan sangat cepat..{kecepatan} {satuan}') 

sepeda = Kendaraan() 
sedan = mobil() 

sepeda.berjalan()
sedan.berjalan(140) 

#contoh 3 
class Macan: 
    def berjalan(self): 
        print('berlari.....') 

class Singa(Macan): 
    def berjalan(self , kecepatan , satuan = 'km/j'): 
        super().berjalan()
        print(f'  ---->>>> berlari dengan sangat cepat kecepatan mencapai..{kecepatan} {satuan}') 

esse = Macan() 
sedan = Singa() 

esse.berjalan()
sedan.berjalan(500)  

#terimaksih 



