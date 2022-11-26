#contoh penggunaan rertrun pada function 
def hitung_luas_segitiga(alas , tinggi) : 
    luas = alas * tinggi /2 
    return luas 
vin = hitung_luas_segitiga(10 , 2) 
print('luas segitiganya adalah = ', vin)  

#contoh 2 

def hitung_lias_segitiga(alas , tinggi): 
    return(alas * tinggi) / 2 
print('luas segitiganya adalah = ',hitung_lias_segitiga(2,4)) 
 

#contoh 3 
def hitung_lias_segitiga(alas , tinggi): 
    return(alas * tinggi) / 2 
    print('alim rabbani')#tidak akan di eksekusi  

print('luas segitiga adalah = ', hitung_lias_segitiga(5,6)) 

#contoh 4 
def harga_setelah_pajak(harga_dasar):
  return harga_dasar + (harga_dasar * 10/100)
 
harga_cilok = 5000
harga_final_cilok = harga_setelah_pajak(harga_cilok)
print("Harga cilok 1 porsi Rp.", harga_final_cilok) 

#terimakasih 