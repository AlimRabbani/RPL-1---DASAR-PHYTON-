#kakulator 

print(20*"=") 
print("Kakulator Sederhana") 
print(20*"=" + "\n") 

angka_1 = float(input("Masukkan angka 1 = ")) 
operator = input("operator(+,-,x,/) : ") 
angka_2 = float(input("Masukkan angka 2 : ")) 

if operator == "+": 
    hasil = angka_1 + angka_2 
    print(f"hasilnya adalah {hasil}") 
elif operator == "-": 
    hasil = angka_1 - angka_2 
    print(f"hasilnya adalah {hasil}") 
elif operator == "x": 
    hasil = angka_1 * angka_2 
    print(f"hasilnya adalah{hasil}") 
elif operator == "/": 
    hasil = angka_1 / angka_2 
    print(f"hasilnya adalah{hasil}")  
else : 
    print("program error") 
print("Terimakasih")