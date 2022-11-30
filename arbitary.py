#menggunakan fuction 
def sapa_teman(nama1,nama2,nama3): 
    print("hellow", nama1) 
    print('hellow',nama2) 
    print('hellow',nama3) 
sapa_teman('vifin','pia','alim')  
#namun bagaimana jika kita memanggil fungsi sapa teman dengan 4 parameter ? 
def sapa_teman(nama1,nama2,nama3): 
    print("hellow", nama1) 
    print('hellow',nama2) 
    print('hellow',nama3) 
sapa_teman('vifin','pia','alim','luffy') # yup program error  

#mari kita coba menggunakan teknik arbitary arguments 
#contoh 
def sapa_teman(*args): #jadi untuk nama parameternya bebas ya guys yah  tp wajip di awali dengan tanda * 
    print(args) 
    print(type(args))#untuk mengetahui tipe data . btw args itu singkatan dari ARGUMENTS 

sapa_teman('alim','arif','hendra','adriawan','rasyid','fitri','ucup','ayu')  
#yup program berhasil  
#jadi kita bisa membuat sebuah fungsi untuk menerima 3,4 atau 100 argumen sekaligus , silahkan di coba soalnya saya juga masih mencoba ini 
 
#contoh 2 arbitary arguments 
def sapa_teman(*nama) : 
  for i in nama: 
     print('hallow',i) 
sapa_teman('ayu','pia','fitri','nami','sakura','himata','rapunzel','akila','putri','mikasa') 
#pake perulangan aj kalo mau mengakses setiap elemen biar lebih keren juga  

#contoh 3 
def jumlah(*args): # sekali lagi itu nama parameternya bebas yh guys yh 
   hasil = 0 
   for i in args: # biar hasilnya lebih berurut ke bawa / rapih 
      hasil += i 
   return hasil 

print(jumlah(2,4))#akan di jumlahkan 
print(jumlah(10,20,100,100,40) ) 
print(jumlah(10,2,10,100,70) ) 
print(jumlah(10,20,50,60,40) )   

#contoh 3  
#buat mencari nilai rata rata 
def jumlah(*args): 
   hasil = 0 
   for i in args: 
      hasil += i 
   return hasil /len(args) 

print(jumlah(2,4))#akan di jumlahkan 
print(jumlah(10,20,100,100,40) ) 
print(jumlah(10,2,10,100,70) ) 
print(jumlah(10,20,50,60,40) )  

#sekian yh guys yah 

    
   


