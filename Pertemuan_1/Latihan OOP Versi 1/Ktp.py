#-----------------latihan Contoh lain Versi 1 OOP class-----------------#


class Ktp:
    def __init__(self, nama, nik, ttl, jk):
        self.nama = nama
        self.nik = nik
        self.tanggal_lahir = ttl
        self.jenis_kelamin = jk
        
    def info(self):
        print(f"Nama : {self.nama}\nNik : {self.nik}\nTempat Tanggal Lahir : {self.tanggal_lahir}\nJenis Kelamin : {self.jenis_kelamin}")

ktp = Ktp("Budi", "2209123456789", "Riau, 14/07/2006", "Laki - Laki")
ktp.info()        