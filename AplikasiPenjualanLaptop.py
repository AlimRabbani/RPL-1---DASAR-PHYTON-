pilihan = 'y' 
while pilihan == 'y':
    print(""" 
    ============================== 
    Selamat datang di laptop Store 
    Berikut produk yang tersedida
    =============================
    1 . Asus MDAO Amd ryzen 332500U      Rp.7.500.000
    2 . Asus MDAO Amd ryzen 55500U       Rp.9.500.000 
    3 . lenovo IP slim 3 intel core i5   Rp.10.500.000
    4 . acer swif 3 Amd ryzen 55500U     Rp.10.500.000
    ========================================================
    """) 

    pesan = int(input("Masukkan pesanan anda sesuai nomor urutan di atas : "))   
    jumlah_pesanan = int(input("Jumlah pesanan : ")) 

    if pesan == 1: 
        listnamaproduk = 'Asus MDAO Amd ryzen 332500U ' 
        harga  =(7500000*jumlah_pesanan) 
        ppn = int(harga*0.1) 
        if jumlah_pesanan >= 5:
            diskon = int(harga*0.2)
            total_harga = int(harga-diskon+ppn)
        else : 
            diskon =(0)
            total_harga = int(harga+ppn)
    elif pesan == 2: 
         listnamaproduk = 'Asus MDAO Amd ryzen 332500U ' 
         harga  =(9500000*jumlah_pesanan) 
         ppn = int(harga*0.1) 
         if jumlah_pesanan >= 5:
            diskon = int(harga*0.2)
            total_harga = int(harga-diskon+ppn)
         else : 
            diskon =(0)
            total_harga = int(harga+ppn) 
    elif pesan == 3: 
        listnamaproduk = 'lenovo IP slim 3 intel core i5' 
        harga  =int(10500000*jumlah_pesanan) 
        ppn = int(harga*0.1) 
        diskon =0
        total_harga = int(harga+ppn) 
    elif pesan == 4: 
        listnamaproduk = ' acer swif 3 Amd ryzen 5500U' 
        harga  =int(10500000*jumlah_pesanan) 
        ppn = int(harga*0.1) 
        diskon =(0)
        total_harga = int(harga+ppn) 
    else : 
        listnamaproduk = '--------' 
        harga  = '---------' 
        ppn = '--------'
        diskon ='------'
        total_harga = '--------' 
        pilihan=input('Menu tidak tersedia,silahkan masukkan abjad menu yang tersedia ulanhi kembali Y/N') 

    print('------------------------------------')
    print('Laptop Store') 
    print('------------------------------------')
    print("Menu : ", listnamaproduk) 
    print("Jumla pesanan : ",jumlah_pesanan) 
    print("Harga : ", harga) 
    print('Diskon : ', diskon) 
    print('PPN : ', ppn) 
    print('-------------------------------------') 
    print('Jumlah bayar Rp. : ', total_harga) 
    print('---------------------------------------') 
    pilihan=input('Apakah anda ingin order kembali Y/N : ') 
    print('Terimakasih')




