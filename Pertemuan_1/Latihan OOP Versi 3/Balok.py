#-----------------latihan Contoh lain Versi 3 OOP class-----------------#


class Balok:
    def __init__(self):
        self._panjang = None
        self._lebar = None
        self._tinggi = None
        
    @property
    def panjang(self):
        return self._panjang
    
    @panjang.setter
    def panjang(self, value):
        self._panjang = value
        
    @property
    def lebar(self):
        return self._lebar
    
    @lebar.setter
    def lebar(self, value):
        self._lebar = value
        
    @property
    def tinggi(self):
        return self._tinggi
    
    @tinggi.setter
    def tinggi(self, value):
        self._tinggi = value
        
    def Volume(self):
        return self._panjang * self._lebar * self._tinggi
    
B = Balok()
P = input("Masukkan Nilai Panjang :")
L = input("Masukkan Nilai Lebar :")
T = input("Masukkan Nilai Tinggi :")

B.panjang = int(P)
B.lebar = int(L)
B.tinggi = int(T)

V = B.Volume()

print("Panjang Sebesar :", P)
print("Lebar Sebesar :", L)
print("Tinggi Sebesar :", T)
print("Jadi Hasil LuasNya sebesar :", V)
