'''Algoritma Bil_Ganjil_Genap
{I.S : Memasukkan suatu bilangan}
{F.S : Menampilkan bilangan ganjil atau bilangan genap}

Kamus :
  bil : integer


Algoritma :
  input(bil)    
  if (bil mod 2=0)
    output(‘Bilangan Genap’)
  else
    output (‘Bilangan Ganjil’)
'''
bil = int(input("Masukkan Angka : "))
if bil % 2 == 0:
    print("Bilangan Genap")
else:
    print("Bilangan Ganjil")