#BELAJAR SLICING LIST
#mengubah data dalam list 
list_nama =['luffy',' zoro' ,'chopper','sanji','usop'] 
 
#jadi kita akan merubah salah data dalam list di atas dengan cara :  
list_nama[3] = 'akagami' #untuk marubah data dalam list/bebas mau merubah data yg mana saja , yg penting yg di rubah itu data dalam list
#selanjutnya kita akan merubah data dalam list paling terakhir/pada indeks ke 4 
list_nama[-1]= 'dragon' 
#selanjutnya kita akan menambahkan data baru ke dalam list 
list_nama.append('Oden')#data baru ini akan muncul di list paling terakhir .
#pertanyaannya apa kita tidak bisa menambahkan data baru diawal list ? ya tentu saja bisa , mari kita coba coba
list_nama.insert(0,'torao') 
#insert adalah fungsi library phyton yg digunakan untuk menyisipkan elemen tertentu pada indeks tertentu dalam daftar list/data dalam list
#jadi jika teman teman ingin mengubah data dalam list di manapun itu / indeks manapun , teman" bisa menggunakan fungsi insert
print(list_nama) 

#cara menghapus salah satu data dalam list 
#ada tiga cara yg bisa kita gunakan dalam menghapus data dalam list diantaranya :
#fungsi pop . fungsi remove ,  del 
#fugsi pop
list_angka =[1,2,4,3,6,9]  
list_angka.pop(5) # maka data dalam list angka pada indeks ke 5 akan hilang(9)
print(list_angka) 
#fungsi remove 
list_buah=['anggur','nanas','jeruk','mangga','pisang'] 
list_buah.remove('anggur') 
print(list_buah) 
# del 
list_buah1 = ['kelapa','semangka','pepaya','jambu'] 
del list_buah1[1]#masukkan indeks data yg akan di hapus 
print(list_buah1)  
#DAN MASIH BANYAK LAGI FUNGSI YG BISA KITA PAKAI UNTUK MENYELESAIKAN BERBAGAI MACAM PERMASALAHAN 

#cara menggabungkan 1 - 4 buah  list 
a = [1,2,3,4] 
b = ['a','b','c','d'] 
c = [True , 'k', 2,False] 
#kita akan menggabungkan 3 list di atas 
listGabung = a + b + c 
print(listGabung) 
#kira kira seperti itu 


