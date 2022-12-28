#program untuk mengecek bonus dan diskon

total_belanja =int(input("Total belanja:Rp ")) 
bayar = total_belanja 
if total_belanja > 100000: 
    print("Kamu mendapatkan bonus minuman Coca-cola") 
    print("Dan diskon 5%") 

    diskon = total_belanja * 5/100 
    bayar = total_belanja - diskon 


print("Total yang harus di bayar : Rp %s" % bayar) 
print("Terimakasih sudah belanja") 
print("Datang lagi yah ")  

#cek umur bestiee 
#ini cuman contoh yh 
umur = int(input("Berapa umur kamu : ")) 

if umur == 18 : 
    print("Kamu boleh membuat SIM") 
elif umur == 17 : 
    print("Kamu belum bisa membuat KTP") 
elif umur == 16 : 
    print("Kamu masih di kelas menengah") 
elif umur == 15 : 
    print("Belajar yang rajin yah ") 
else : 
    print("selamat kamu dikeluarkan dari sekolah ini hahahah") 

# contoh 
#input data 

var_presiden = input("Presiden pertama indonesi : ") 

if var_presiden == "SOEKARNO": 
    print("jawaban anda benar") 
elif var_presiden =="PUAN MAHARANI": 
    print("salah yah , Puan itu ketua DPR RI")
elif var_presiden =="SOEHARTO": 
    print("salah yah soalnya pak soeharto itu presiden kedua republik indonesia yh")
elif var_presiden == "JOKOWI":
    print("yah kalo pak jokowi mah presiden ke tujuh republik indonesia") 
elif var_presiden == "BJ.HABIBIE": 
    print("salah lagi ,kalo pak BJ habibie mh presiden ke tiga Republik indonesia") 
elif var_presiden == "MEGAWATI": 
    print("salah yah , Bu megawati itu presiden ke lima republik indonesia ") 
else : 
    ("Belajar yang rajian yah guys ")   

# CONTOH 

total_belanja =int(input("total belanja : Rp ")) 

bayar = total_belanja 

if total_belanja > 200000: 
    print("kamu mendapatkan minuman dingin") 
    print("kamu juga mendapatkan dison 4%") 

    diskon = total_belanja * 2/200 
    bayar = total_belanja - diskon 
    

print("Total yang harus di bayar : Rp %s" % bayar) 
print("Terimaksih") 
print("Datang lagi yah ")  