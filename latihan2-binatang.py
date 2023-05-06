# superclass
class Binatang:
    def __init__(self, nama, umur, jenis):
        self.nama = nama
        self.umur = umur
        self.jenis = jenis
    
    def makan(self):
        print("Binatang sedang makan.")
    
    def bersuara(self):
        print("Binatang sedang bersuara.")

# subclass 1
class Kambing(Binatang):
    def __init__(self, nama, umur, jenis, ekor):
        super().__init__(nama, umur, jenis)
        self.ekor = ekor
    
    def susu(self):
        print("Kambing sedang memberi susu.")
    
    def lompat(self):
        print("Kambing sedang melompat.")

# subclass 2
class Gajah(Binatang):
    def __init__(self, nama, umur, jenis, hidung):
        super().__init__(nama, umur, jenis)
        self.hidung = hidung
    
    def makan(self, makanan):
        print(f"Gajah sedang makan {makanan}.")
    
    def bersuara(self):
        print("Gajah sedang bersuara NGOOOOOOHH.")
        
# subclass 3
class Kuda(Binatang):
    def __init__(self, nama, umur, jenis, tinggi, warna):
        super().__init__(nama, umur, jenis)
        self.tinggi = tinggi
        self.warna = warna
    
    def lari(self):
        print("Kuda sedang berlari.")
    
    def lompat(self):
        print("Kuda sedang melompat.")

# subclass 4
class Pembalap(Kuda):
    def balapan(self):
        print("Pembalap sedang balapan.")

# subclass 5
class Berkuda(Kuda):
    def __init__(self, nama, umur, jenis, tinggi, warna, bobot):
        super().__init__(nama, umur, jenis, tinggi, warna)
        self.bobot = bobot
    
    def berlari(self):
        print("Berkuda sedang berlari.")
    
    def dilatih(self):
        print("Berkuda sedang dilatih.")

