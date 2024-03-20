#-----------------latihan Contoh lain Versi 1 OOP class-----------------#

class Paspor:
    def __init__(self, nama, kwn, ttl, jk, ktr, kode):
        self.nama = nama
        self.kewarganegaraan = kwn
        self.tanggal_lahir = ttl
        self.jenis_kelamin = jk
        self.kantor_negara = ktr
        self.kode_paspor = kode
        
    def info(self):
        print(f"Nama : {self.nama}\nKewarganegaraan  : {self.kewarganegaraan}\nTempat Tanggal Lahir : {self.tanggal_lahir}\nJenis Kelamin : {self.jenis_kelamin}\nKantor Negara : {self.kantor_negara}\nKode Paspor : {self.kode_paspor}")

paspor = Paspor("Raka", "Indonesia", "Indoensia, Riau, 14/07/2006", "Laki - Laki", "Kuala Lumpur", "M08362817-KL")
paspor.info()        