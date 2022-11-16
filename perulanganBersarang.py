#perhatikan kode berikut 
#contoh 1
for i in range(2): 
    print("perulangan luar [i] =" , i ) 

    for j in range(10): 
        print('perulangan dalam [i] =', str(i) + ',' + str(j))  
# #perulangan pertana sebanyak 2 kali 
#perulangan kedua sebanyak 10 kali setiap satu kali perulangan pertama 
#maksudnya satu kali perulangan pertama dengan perulangan kedua(2*10)  

#contoh 2 
for baris in range(4): 
    for kolom in range(3): 
        print('o', end = '') 
    else : 
        print('')  
#semoga ngerti yah gys yah  
#jadi selain for kita juga bisa pake whilw yh gys untuk membangun sebuah perulangan bersarang


listKota = [
    'majene','polman','makassar'
]

for kota in listKota: 
    print(kota) 

    listTempat = [
        'tako','alun-alun','mall' 
    ]

    while listTempat: 
        print('------>>>', listTempat.pop(0))
#terimaksih