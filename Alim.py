#ok utuk kali ini saya bakal buat contoh program  paradigma OOP phyton 
# > fungsional 
# > OOP 
# > prosedural  

# > PROSEDURAL 
def hitung_luas(): 
    alas = float(input('masukkan alas : ')) 
    tinggi = float(input('masukkan tinggi :'))
    print('luas=',  0.5 * alas * tinggi)  
#kita bisa panggil berkali kali dan menginputkan nilai yang berbeda 
hitung_luas() 
#panggil lagi 
hitung_luas() 
#panggil lagi 
hitung_luas() 
#dan lagi 
hitung_luas()
#jadi seperti itu , PROSEDURAL ini melakukan pengelompokan tugas tertentu yang bisa kita gunakan berkali kali untuk memecahkan suatu masalah 


# FUNGSIONAL 
def input_alas_dan_tinggi(): 
    alas = float(input('masukkan alas : ')) 
    tinggi = float(input('masukkan tinggi :')) 

    return alas , tinggi


def hitung_luas(alas , tinggi): 
    return 0.5 *alas*tinggi  

print(hitung_luas(10 , 5))  # nialainya bisa teman teman rubah / bebas 

alas , tinggi = input_alas_dan_tinggi() 
print(hitung_luas(alas , tinggi)) 


#perhatikan struktur progammnya , soalnya kalo ada yang salah itu biasanya ga bakal error tp programmnya ga bakal  jalan 
#gitu guys 
# sebenarnya ini hampir sama dengan PROSEDURAL , cuman yang mebedekan itu paradigma ini lebih ke "input-output" 
#jadi di FUNGSIONAL ini penggunaaanya cuman sekali yh , ini cuman contoh nanti kedepannya kita bakal bahas ini lagi .heheehe

# > OOP 

        


