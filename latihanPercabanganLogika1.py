#percabangan logika if , elif , else phyton 
#menentukan nilai siswa
nilaiSiswa = int(input("masukkan nilai :"))
if nilaiSiswa >= 90 :
    print("nilai A") 
elif nilaiSiswa >= 80 : 
    print("predikat B") 
elif nilaiSiswa >= 70 :
    print("Predikat C") 
elif nilaiSiswa >= 60 :
    print("predikat D") 
elif nilaiSiswa >= 50 :
    print("predikat E") 
    print("ngulang tahaun depan kamu") 
else : 
    print("Error") 

    
#percabangan logika phyton 

Hari = input("masukkan jadwal kuliah :") 

if Hari == "senin": 
    print("libur") 
elif Hari == "selasa":
    print("kuliah") 
elif Hari == "rabu":
    print("kuliah")
elif Hari == "kamis": 
    print("kuliah") 
elif Hari == "jum'at": 
    print("kuliah") 
elif Hari == "sabtu": 
    print("libur") 
else : 
    print("program Error")

