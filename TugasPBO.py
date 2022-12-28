class Luas: 
    def __init__(self, a,t): 
        self.alas = a 
        self.tinggi = t 
    def __str__(self):
        luasSegitiga = 0.5 *self.alas * self.tinggi 
        return f'segitiga(alas={self.alas}={self.tinggi} luas={"luas egitiga adalah ",luasSegitiga})' 

    def __init__(self, a,r): 
        self.luas = a 
        self.jari_jari = r
    def __str__(self):
        luasLingkaran= 0.5 *self.luas* self.jari_jari
        return f'luas(alas={self.luas}={self.jari_jari} luas={"luas lingkaran adalah ",luasLingkaran})' 

    def __init__(self, p , l , t): 
        self.panjang = p
        self.lebar= l 
        self.tinggi = t 
    def __str__(self):
        luasVolume = 0.5 *self.panjang * self.lebar * self.tinggi  
        return f'segitiga(alas={self.panjang}={self.lebar}={self.tinggi} luas={"luas kubus adalah ",luasVolume})'  
    
    def __init__(self, p , l ,t): 
        self.panjang = p
        self.lebar = l
        self.tinggi = t
    def __str__(self):
        luasBalok = 0.5 *self.panjang * self.lebar * self.tinggi
        return f'segitiga(alas={self.alas}={self.tinggi} luas={"luas egitiga adalah ",luasBalok})' 

    
 

    

