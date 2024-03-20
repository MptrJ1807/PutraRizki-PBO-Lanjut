#-----------------latihan Contoh lain Versi 3 OOP class-----------------#


class LimasSegiEmpat:
    def __init__(self):
        self._sisi = None
        self._tinggi = None
        
    @property
    def sisi(self):
        return self._sisi
    
    @sisi.setter
    def sisi(self, value):
        self._sisi = value
        
    @property
    def tinggi(self):
        return self._tinggi
    
    @tinggi.setter
    def tinggi(self, value):
        self._tinggi = value
        
    def Volume(self):
        return ((1/3) * self._sisi**2 * self._tinggi)
    
L = LimasSegiEmpat()
S = input("Masukkan Nilai Sisi :")
T = input("Masukkan Nilai Tinggi :")

L.sisi = int(S)
L.tinggi = int(T)

V = L.Volume()

print("Sisi Sebesar :", S)
print("Tinggi Sebesar :", T)
print("Jadi Hasil LuasNya sebesar :", V)
