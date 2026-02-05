from abc import ABC, abstractmethod

# =========================================
# ABSTRACT CLASS (ABSTRACTION)
# =========================================
class BarangElektronik(ABC):
    def __init__(self, nama, harga_dasar):
        self.nama = nama
        self.__harga_dasar = harga_dasar
        self.__stok = 0

    # Getter stok
    def get_stok(self):
        return self.__stok

    # Setter / tambah stok dengan validasi
    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {jumlah} unit.")

    # Protected getter harga (untuk anak class)
    def _get_harga_dasar(self):
        return self.__harga_dasar

    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass


# =========================================
# CHILD CLASS: LAPTOP (INHERITANCE)
# =========================================
class Laptop(BarangElektronik):
    def __init__(self, nama, harga_dasar, processor):
        super().__init__(nama, harga_dasar)
        self.processor = processor

    def tampilkan_detail(self):
        pajak = int(self._get_harga_dasar() * 0.10)
        print(f"[LAPTOP] {self.nama} | Proc: {self.processor}")
        print(f"   Harga Dasar: Rp {self._get_harga_dasar():,} | Pajak(10%): Rp {pajak:,}")

    def hitung_harga_total(self, jumlah):
        pajak = self._get_harga_dasar() * 0.10
        total = (self._get_harga_dasar() + pajak) * jumlah
        return int(total)


# =========================================
# CHILD CLASS: SMARTPHONE (INHERITANCE)
# =========================================
class Smartphone(BarangElektronik):
    def __init__(self, nama, harga_dasar, kamera):
        super().__init__(nama, harga_dasar)
        self.kamera = kamera

    def tampilkan_detail(self):
        pajak = int(self._get_harga_dasar() * 0.05)
        print(f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}")
        print(f"   Harga Dasar: Rp {self._get_harga_dasar():,} | Pajak(5%): Rp {pajak:,}")

    def hitung_harga_total(self, jumlah):
        pajak = self._get_harga_dasar() * 0.05
        total = (self._get_harga_dasar() + pajak) * jumlah
        return int(total)


# =========================================
# POLYMORPHISM
# PROSES TRANSAKSI
# =========================================
def proses_transaksi(daftar_barang):
    print("\n--- STRUK TRANSAKSI ---")
    total_bayar = 0
    no = 1

    for barang, jumlah in daftar_barang:
        print(f"{no}. ", end="")
        barang.tampilkan_detail()
        subtotal = barang.hitung_harga_total(jumlah)
        print(f"   Beli: {jumlah} unit | Subtotal: Rp {subtotal:,}\n")
        total_bayar += subtotal
        no += 1

    print("----------------------------------------")
    print(f"TOTAL TAGIHAN: Rp {total_bayar:,}")
    print("----------------------------------------")


# =========================================
# USER STORY (MAIN PROGRAM)
# =========================================
print("--- SETUP DATA ---")

# 1) Admin membuat produk
laptop = Laptop("ROG Zephyrus", 20_000_000, "Ryzen 9")
hp = Smartphone("iPhone 13", 15_000_000, "12MP")

# 2) Admin mencoba stok negatif
laptop.tambah_stok(10)
hp.tambah_stok(-5)
hp.tambah_stok(20)

# 3) User membeli
keranjang = [
    (laptop, 2),
    (hp, 1)
]

# 4) Tampilkan struk dan total harga
proses_transaksi(keranjang)
