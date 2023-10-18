'''
Algoritma Menghitung Komisi penjualan
{I.S : Menghitung Penjualan}
{F.S : Menampilkan Komisi untuk Salesman}
Kamus:
s : string
p : integer
k : integer
Aloritma:
input (s)
input (p)
k = ← 0.05 * p
output ('Nama Salesman')
output ('Besaran Komisi')
'''
s = str(input("Masukkan Nama Salesman :"))
p = int(input("Masukkan Jumlah Penjualan : "))
k = 0.05 * p

print("Nama Salesman : ", s)
print("Besaran Komisi : ", k)