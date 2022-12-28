#latihan program nilai
#program predikat yang di dapatkan mahasiswa berdasarkan nilai IPK
nama = input("Masukkan nama anda : ") 
nilai = float(input("Masukkan nilai IPK anda =  "))


if nilai > 4.0:
    print("selamat anda mendapatkan predikat A+") 
elif nilai < 3.0:
    print("selamat anda mendapatkan predikat A")   
elif nilai >= 2.50:
    print("selamat anda mendapatkan predikat B+") 
elif nilai <= 2.0: 
    print("selamat anda mendapatkan predikat B") 
elif nilai == 1.0: 
    print("selamat anda mendapatkan predikat C") 
else : 
    print("Masukan nilai anda = ") 

print("Nama : " , nama)
print("Nilai : " , nilai)  



