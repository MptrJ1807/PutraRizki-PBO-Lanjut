#-----------------latihan Contoh lain Versi 2 OOP class-----------------#

class PersegiPanjang:
    def __init__(self):
        self.panjang = None
        self.lebar = None
        self.keliling = None
        
    def Keliling(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
        self.keliling = 2 * (self.panjang + self.lebar)
        return self.keliling
    
P = PersegiPanjang()
panjang = input("masukkan Nilai Panjang :")
lebar = input("masukkan Nilai Lebar :")
keliling = P.Keliling(int(panjang), int(lebar))

print("Panjang :",panjang)
print("lebar :",lebar)
print("Keliling :",keliling)