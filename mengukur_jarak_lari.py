"""
{I.S : Menghitung waktu Tempuh jarak lari}
{F.S : Mengetaui waktu tempuh seorang pelari marathon}

Kamus :
jam     : ril
menit   : ril
detik   : ril
waktu tempuh : ril

Algoritma :
input (jam)
input (menit)
input (detik)
waktu_tempuh ← 3600 * jam + 6 * menit + detik

"""
#Kode Program :
jam = int(input("Masukkan Waktu tempuh dalam satuan jam : "))
menit = int(input("Masukkan Wkatu tempuh dalam satuan menit : "))
detik = int(input("Masukkan Wkatu tempuh dalam satuan detik : "))

waktu_tempuh = 3600 * jam + 6 * menit + detik
print (waktu_tempuh)