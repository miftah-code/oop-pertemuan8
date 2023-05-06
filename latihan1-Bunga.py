class Bunga:
    def __init__(self, nama, jumlah_kelopak, harga):
        self.nama = nama
        self.jumlah_kelopak = jumlah_kelopak
        self.harga = harga
    
    def set_nama(self, nama):
        self.nama = nama
    
    def set_jumlah_kelopak(self, jumlah_kelopak):
        self.jumlah_kelopak = jumlah_kelopak
    
    def set_harga(self, harga):
        self.harga = harga
    
    def get_nama(self):
        return self.nama
    
    def get_jumlah_kelopak(self):
        return self.jumlah_kelopak
    
    def get_harga(self):
        return self.harga

# membuat objek dari class Bunga
bunga1 = Bunga("Mawar", 5, 10000.0)

# mengambil nilai atribut nama dan harga dari objek bunga1
print("Nama bunga: ", bunga1.get_nama())
print("Harga bunga: ", bunga1.get_harga())

# mengubah nilai atribut harga dari objek bunga1
bunga1.set_harga(12000.0)

# mengambil nilai atribut harga yang sudah diubah dari objek bunga1
print("Harga bunga setelah diubah: ", bunga1.get_harga())
