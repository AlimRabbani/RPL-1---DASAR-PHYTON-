
jum_semen = input("Masukkan jumlah semen yanhg nda beli : ") 
harga_semen = 60000
diskon1 = 2/100
diskon2 = 5/100


 
if jum_semen > 100 :
    Total_diskon =  jum_semen * harga_semen - diskon1 

elif jum_semen > 200 :
    Total_diskon = jum_semen * harga_semen - diskon2 
else: 
    Total_diskon = 0  

print("jumlah semen = " , jum_semen) 
print("total disko yang di dpt dari pembelian = " , Total_diskon)

 
