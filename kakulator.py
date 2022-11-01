bil1 = int(input("masukkan bilangan 1 :")) 
bil2 = int(input("masukkan bilangan 2 : ")) 
operator = input("masukkan operator :") 
if (operator == "+"):
    hasil = bil1 + bil2
    print("hasil penjumlahan = ", hasil)
elif (operator == "-"):
    hasil = bil1 - bil2
    print("hasil pengurangan = ", hasil)
elif (operator == "*"):
    hasil = bil1 * bil2
    print("hasil perkalian = ", hasil)
elif (operator == "/"):
    hasil = bil1 / bil2
    print("hasil pembagian = ", hasil) 
elif (operator == "**"):
    hasil = bil1 ** bil2
    print("hasil perpangkatan = ", hasil) 
else : 
    print("maaf operator yg anda masukkan salah") 

    #I'm sorry, the calculator that I made earlier is very short and also very uncool, for the kind-hearted mentor, I apologize profusely for making such a calculator program. next time I will make a shorter one, just kidding