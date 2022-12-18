# inheritance / pewarisan 
# contoh 1 

class orang : 
    def __init__(self, nama , asal,hobi ): 
        self.nama = nama 
        self.asal = asal
        self.hobi = hobi
        print('fungsi orang.__init__() dieksekusi')

    def perkenalan (self): 
        print(f'perkenalkan nama saya {self.nama} dari {self.asal} hobi saya {self.hobi} ') 

class pelajar(orang): 
    pass 

class pekerja(orang): 
    pass  

class kaum_rebahan(orang): 
    pass 
lim = orang('alim rabbani','mamasa','ngoding')   
lim.perkenalan() 

ainul = orang('ainul akram jaya','salu assing','menggambar') 
ainul.perkenalan ()

rasyid = pelajar('harun al rasyid','lino maloga','bermain main dengan aturan') 
rasyid.perkenalan ()

ramadhan= pekerja('ramadhan','mambi','bermail game')  
ramadhan.perkenalan () 

ahmad = kaum_rebahan('ahamad','loka','belajar')
ahmad.perkenalan 

#terimakasih 

 


