#-----------------latihan Contoh lain Versi 2 OOP class-----------------#

class JajarGenjang:
    def __init__(self):
        self.alas = None
        self.tinggi = None
        self.luas = None
        
    def Luas(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        self.luas = self.alas * self.tinggi
        return self.luas
    
J = JajarGenjang()
alas = input("masukkan Nilai Alas :")
tinggi = input("masukkan Nilai Tinggi:")
luas = J.Luas(int(alas), int(tinggi))

print("Alas :",alas)
print("Tinggi :",tinggi)
print("Luas :",luas)