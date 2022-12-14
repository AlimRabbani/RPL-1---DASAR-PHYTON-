#mencari kata pada string 
angka = '12345' 

print("index angka 3 : ",angka.find('3')) # find fungsi yg di pakai untuk mencari 
print("index angka 45 : ",angka.find('45')) 
print("index angka 35 : ",angka.find('35'))  

#mereplace kata pada string 

ibu_kota = "Jakarta" 

print(ibu_kota.replace('a','r'))
print(ibu_kota.replace('t','r')) 

#menghapush karakter 

ibu_negara = "puanmaharani" 

print(ibu_negara.replace('a','')) 

#menghutung jumlah karakter yang muncul 

paragraf = "Baru baru ini telah di temukan meteor di suatu sungai" 

x = paragraf.count('di') 

print(f'kata "di" muncul sebanyak {x} kali')  

#terimakasih