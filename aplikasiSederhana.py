pilihan = 'y' 
while pilihan == 'y': 
    print("""
    ====================================
    
    Alim Coffe 
    List menu minuman kopi 
    =====================================
    A . Es Cappuccino : Rp. 15000
    B . kopi pait     : Rp. 10000
    C . kopi susu     : Rp. 20000
    D . bakso bakar   : Rp. 15000
    =====================================
    """) 

    pesan = str(input("Masukkan list abjad menu kopi = ")) 
    jumlah_pesan = int(input("Masukkan jumlah pesanan = "))
    if pesan == 'a': 
        listnama = 'Es Cappuccino' 
        harga  =(15000*jumlah_pesan) 
        ppn = int(harga*0.1) 
        if jumlah_pesan >= 5:
            diskon = int(harga*0.2)
            total_harga = int(harga-diskon+ppn)
        else : 
            diskon =(0)
            total_harga = int(harga+ppn)
    elif pesan == 'b': 
         listnama = 'kopi pait' 
         harga  =(10000*jumlah_pesan) 
         ppn = int(harga*0.1) 
         if jumlah_pesan >= 5:
            diskon = int(harga*0.2)
            total_harga = int(harga-diskon+ppn)
         else : 
            diskon =(0)
            total_harga = int(harga+ppn) 

    elif pesan == 'c': 
        listnama = 'kopi susu' 
        harga  =int(20000*jumlah_pesan) 
        ppn = int(harga*0.1) 
        diskon =0
        total_harga = int(harga+ppn) 
    elif pesan == 'd': 
        listnama = 'bakso bakar' 
        harga  =int(15000*jumlah_pesan) 
        ppn = int(harga*0.1) 
        diskon =(0)
        total_harga = int(harga+ppn) 
    else : 
        listnama = '--------' 
        harga  = '---------' 
        ppn = '--------'
        diskon ='------'
        total_harga = '--------' 
        pilihan=input('Menu tidak tersedia,silahkan masukkan abjad menu yang tersedia ulanhi kembali Y/N') 
    print('------------------------------------')
    print('Alim Coffe') 
    print('------------------------------------')
    print("Menu : ", listnama) 
    print("Jumla pesanan : ",jumlah_pesan) 
    print("Harga : ", harga) 
    print('Diskon : ', diskon) 
    print('PPN : ', ppn) 
    print('-------------------------------------') 
    print('Jumlah bayar : ', total_harga) 
    print('---------------------------------------') 
    pilihan=input('Apakah anda ingin order kembali Y/N : ') 
    print('Terimakasih')



    