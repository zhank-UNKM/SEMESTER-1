'''
Algoritma Menghitung Komisi penjualan
{I.S : Menghitung Penjualan}
{F.S : Menampilkan Komisi untuk Salesman}
Kamus:
salesman : string
penjualan : integer
komisi : integer
Aloritma:
input (salesman)
input (penjualan)
komisi = ← 0.05 * penjualan
output ('Nama Salesman', salesman)
output ('Besaran Komisi', komisi)
'''
salesaman = str(input("Masukkan Nama Salesman :"))
penjualan = int(input("Masukkan Jumlah Penjualan : "))
komisi = 0.05 * penjualan

print("Nama Salesman : ", salesaman)
print("Besaran Komisi : ", komisi)