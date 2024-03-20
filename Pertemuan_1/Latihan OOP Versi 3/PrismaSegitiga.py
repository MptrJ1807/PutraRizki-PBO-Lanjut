#-----------------latihan Contoh lain Versi 3 OOP class-----------------#


class PrismaSegitiga:
    def __init__(self):
        self._alas = None
        self._tinggi = None
        
    @property
    def alas(self):
        return self._alas
    
    @alas.setter
    def alas(self, value):
        self._alas = value
        
    @property
    def tinggi(self):
        return self._tinggi
    
    @tinggi.setter
    def tinggi(self, value):
        self._tinggi = value
        
    def Volume(self):
        return 0.5 * self._alas * self._tinggi * self._tinggi
    
P = PrismaSegitiga()
A = input("Masukkan Nilai Alas :")
T = input("Masukkan Nilai Tinggi :")

P.alas = int(A)
P.tinggi = int(T)

V = P.Volume()

print("Alas Sebesar :", A)
print("Tinggi Sebesar :", T)
print("Jadi Hasil LuasNya sebesar :", V)
