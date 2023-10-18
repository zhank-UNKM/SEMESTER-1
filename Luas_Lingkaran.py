'''Algoritma Luas_Keliling_Lingkaran
{I.S : Memasukkan nilai untuk jari-jari dan pi}
{F.S : Menampilkan hasil perhitungan luas dan keliling lingkaran}

Kamus :
  Phi = 3.14
  r : real
  luas, keliling : real

Algoritma :
  input(r)    
  luas ← phi*(r^2)
  keliling  2*phi*r
  output (luas,keliling)
'''
phi = 3.14
r = float(input("Masukkan Nilai Jari-jari: "))
luas = phi * r ** 2
Keliling = 2 * phi * r

print ("Luas Lingkaran : ", luas)
print ("Keliling Lingkaran : ", Keliling)