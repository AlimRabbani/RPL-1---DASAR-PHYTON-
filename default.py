#Default parameter pada function phyton 
#contoh 

def tambah(vin1,vin2): 
    return vin1 + vin2 
print(tambah(10,4))#nilai dalam parameter akan di tambah 
print(tambah(5,7))  

#ok contoh 2 

def tambah_nilai(var1 = 10 , var2 = 5): #default parameter 
    return var1 + var2 
print(tambah_nilai()) 
print(tambah_nilai(1)) 
print(tambah_nilai(2,4)) 
print(tambah_nilai(5,7)) 

#contoh pembuatan defaulat parameter yang sesat/salah 

def tambah(var1 = 10 , var2): 
    return var1 + var2 
#kalo teman teman teman buat kyk gini outputnya bakalan error  
#intinya kalo teman teman sudah membuat parameter pertama dengan nilai default , parameter kedua , ketiga dan seterusnya juga harus memiliki nilai default 

