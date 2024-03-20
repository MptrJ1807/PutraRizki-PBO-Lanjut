#-----------------latihan Contoh lain Versi 2 OOP class-----------------#

class LayangLayang:
    def __init__(self):
        self.diagonal1 = None
        self.diagonal2 = None
        self.luas = None
        
    def Luas(self, diagonal1, diagonal2):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2
        self.luas = (self.diagonal1 * self.diagonal2) / 2
        return self.luas
    
L = LayangLayang()
diagonal1 = input("masukkan Nilai Diagonal 1 :")
diagonal2 = input("masukkan Nilai Diagonal 2 :")
luas = L.Luas(int(diagonal1), int(diagonal2))

print("Diagonal 1 sebesar :",diagonal1)
print("Diagonal 2 sebesar :",diagonal2)
print("Luas :",luas)