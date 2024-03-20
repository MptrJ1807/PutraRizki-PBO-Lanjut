#-----------------latihan Contoh lain Versi 1 OOP class-----------------#

class Pejabat:
    def __init__(self, nama, kwn, ttl, jk, pejabat):
        self.nama = nama
        self.kewarganegaraan = kwn
        self.tanggal_lahir = ttl
        self.jenis_kelamin = jk
        self.pejabat = pejabat
        
    def info(self):
        print(f"Nama : {self.nama}\nKewarganegaraan  : {self.kewarganegaraan}\nTempat Tanggal Lahir : {self.tanggal_lahir}\nJenis Kelamin : {self.jenis_kelamin}\nPejabat : {self.pejabat}")

pejabat = Pejabat("Udin", "Indonesia", "Indoensia, Semarang, 14/07/1980", "Laki - Laki", "Menteri Keuangan")
pejabat.info()        