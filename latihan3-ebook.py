class Ebook:
    def __init__(self, judul, penulis, harga):
        self.judul = judul
        self.penulis = penulis
        self.harga = harga
        self.terbeli = False
    
    def beli(self):
        if self.terbeli:
            print("Anda sudah membeli buku ini sebelumnya.")
        else:
            print(f"Anda berhasil membeli buku {self.judul}.")
            self.terbeli = True
    
    def __str__(self):
        return f"{self.judul} oleh {self.penulis}. Harga: {self.harga}."

class Pengguna:
    def __init__(self, nama):
        self.nama = nama
        self.buku_terbeli = []
    
    def beli_buku(self, buku):
        buku.beli()
        if buku.terbeli:
            self.buku_terbeli.append(buku)
    
    def lihat_buku_terbeli(self):
        if not self.buku_terbeli:
            print("Anda belum membeli buku apapun.")
        else:
            print("Buku yang Anda beli:")
            for buku in self.buku_terbeli:
                print(buku)
    
    def baca_buku(self, buku):
        if not buku.terbeli:
            print("Anda belum membeli buku ini.")
        else:
            print(f"Anda sedang membaca {buku.judul}.")

# contoh penggunaan
ebook1 = Ebook("Harry Potter dan Batu Bertuah", "J.K. Rowling", 50000)
ebook2 = Ebook("To Kill a Mockingbird", "Harper Lee", 45000)

user = Pengguna("John")
user.beli_buku(ebook1)
user.beli_buku(ebook1)
user.beli_buku(ebook2)
user.lihat_buku_terbeli()
user.baca_buku(ebook1)
user.baca_buku(ebook2)

