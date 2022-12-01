#arbitary keyword phyton  
#perbedaan antara arbitary keyword dengan arbitary argumen ada di penulisan named argumen/parameter

#contoh arbitary argumen 
def sambung_kata(*args): 
    for i in args : 
        print('hellow',i)

sambung_kata('yuni','her','cinta',) 

#contoh arbitary keyword  
def sambung_kata(**kwargs): #nama parameternya bebas yh cuman jangan lupa (**)< wajib pake simbol itu untuk arbitary keyword
    print(kwargs) 
    print(type(kwargs)) 
sambung_kata(a='kamu lucu',b='kamu baik',c='kamu jangan begitu yh')#outputnya bakal berbentuk dictionary 
 
#contoh 2 menampilkan nilai 
def sambung_kata(**kwargs): 
    for i in kwargs: 
        print(i)  
sambung_kata(a='kamu lucu',b='kamu baik',c='kamu jangan begitu yh') # jadi yg bakal tampil itu cuman key nya ygy 

#cara buat tampilin valuenya seperti ini / arbitary keyword 
def sambung_kata(**kwargs): #nama parameternya bebas yh cuman jangan lupa (**)< wajib pake simbol itu untuk arbitary keyword
    for i in kwargs.values(): 
        print(i) 
sambung_kata(a='kamu lucu',b='kamu baik',c='kamu jangan begitu yh')
#jadi gitu yh guys yah 

#contoh 3 sambun kata 
def sambung_kata(**kwargs): #nama parameternya bebas yh cuman jangan lupa (**)< wajib pake simbol itu untuk arbitary keyword
  hasil = "" 
  for i in kwargs.values(): 
        hasil += i + " " # biar rapih sambungan katanya 
  return hasil; 

print(sambung_kata(a='kamu lucu',b='kamu baik',c='kamu jangan begitu yh'))#seperti itu guys 
 
# ok neks kita bakal menggabung *args dengan **keywowds 
# contoh 1 
def test(var1,var2,*args,**keywords): 
    print(var1) 
    print(var2) 
    print(args) 
    print(keywords) 
test(10,20,30,40,50, a = 60,b=70,c=80) #gitu guys


#terimakasih 
