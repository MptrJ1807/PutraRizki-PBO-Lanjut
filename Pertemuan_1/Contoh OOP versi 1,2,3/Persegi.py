#Contoh Versi 2 OOP class#

class Persegi:
    def __init__(self):
        self.panjang = None
        self.lebar = None
        self.luas = None
        
    def Luas(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
        self.luas = self.panjang * self.lebar
        return self.luas
    
P = Persegi()
panjang = input("masukkan Nilai Panjang :")
lebar = input("masukkan Nilai Lebar :")
luas = P.Luas(int(panjang), int(lebar))

print("Panjang :",panjang)
print("lebar :",lebar)
print("Luas :",luas)