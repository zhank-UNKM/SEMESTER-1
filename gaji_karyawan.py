"""
{I.F : Mengitung Gaji pokok dan tunjangan Karyawan}
{F.S : Menghitung gaji bersih kayawan setelah di potong pajak}

Kamus : 
nama_karyawan       : string
gaji_pokok          : ril
tunjangan           : ril
pajak               : ril
gaji_bersih         : ril

algoritma:
input (nama_karyawan)
input (gaji_pokok)
tunjangan ← 0.2 * gaji_pokok
pajak ← 0.15 * gaji_pokok + tunjangan
gaji_bersih ← gaji_pokok + tunjangan - pajak

"""

nama_karyawan = input("Masukkan Nama Karyawan : ")
gaji_pokok = float(input("Masukkan Gaji karyawan : "))
tunjangan = 0.2 * gaji_pokok
pajak      = 0.15 * gaji_pokok + tunjangan
gaji_bersih = gaji_pokok + tunjangan - pajak

print ("Nama Karyawan : ", nama_karyawan)
print ("Tunjngan Karyawan : ", tunjangan)
print ("Potongan Pajak :", pajak )
print ("Gaji Bersih : ", gaji_bersih)