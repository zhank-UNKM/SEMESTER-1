#Algoritma Tukar_Nilai
#{I.S : Nilai variabel a dan b dimasukkan oleh pengguna}
#{F.S : Menampilkan hasil pertukaran nilai variabel a dan b}

#Kamus :
#  a,b : integer
#  bantu : integer
a = int(input("Masukkan Nilai A :" ))
b = int(input("Masukkan Nilai B :" ))

bantu = a
a = b
b = bantu
print ("Nilai a Sekarang : ", a )
print ("Nilai b Sekarang : ", b )