#Berikut format penuliasan dictionary 
nama_variabel = {"key1","key2","key3","key4" , 100 , 1.10 ,True} 
print(nama_variabel)  
#Cara pembuatan tipe data dictionary phyton 
luffy = {1: "key1"  , 2 : "key2" , 3: "key3" , 4 : "key4"} 
zoo = {"balajar" : "phyton" , "di" :  "gogle"} 
onee = {1: "belajar" , "phyton1" : "di" , "youtobe" : "semangat"} 
#untuk mengetahai jenis tipe data yang digunakan : 
print(type(luffy)) 
print(type(zoo)) 
print(type(onee))  
#output 
print(luffy) 
print(zoo) 
print(onee)  

#cara mengakses elemen/nilai/indeks 
foo = {"kegiatan":"belajar phyton", 
       "anime Vaforit" : "Naruto" ,
       "karakter ter GG" : "Uchiha sasuke"} 
print(foo["anime Vaforit"])
#berikut cara merubah elemen pada tipe data dictionary  
foo["karakter ter GG"] = "uchiha itachi"
print(foo) 
#cara menambhakan elemen baru dictionary 
foo["anime OP"] = "one piece"
print(foo) 
#cara menghapus 
del foo["kegiatan"] 
print(foo)  
#terimakasih
