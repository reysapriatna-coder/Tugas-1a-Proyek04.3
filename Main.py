class Produk:
    """Kelas untuk merepresentasikan entitas data produk."""
    def __init__(self, product_id, nama_produk, kategori, harga, stok):
        self.product_id = product_id
        self.nama_produk = nama_produk
        self.kategori = kategori
        self.harga = harga
        self.stok = stok

    def __str__(self):
        return f"ID: {self.product_id} | Nama: {self.nama_produk} | Kategori: {self.kategori} | Harga: Rp {self.harga:,.2f} | Stok: {self.stok}"


class InventarisManager:
    """Kelas untuk mengelola inventaris menggunakan Hash Table (Dictionary)."""
    def __init__(self):
        # Penyimpanan utama menggunakan Hash Table (Dictionary Python)
        # Key: product_id (String/Int), Value: Objek Produk
        self.data_inventaris = {}

    def tambah_produk(self, product_id, nama_produk, kategori, harga, stok):
        """Menambahkan produk baru ke sistem dengan kompleksitas O(1)."""
        if product_id in self.data_inventaris:
            print(f"\n[Gagal] Produk dengan ID '{product_id}' sudah terdaftar!")
            return
        
        produk_baru = Produk(product_id, nama_produk, kategori, harga, stok)
        self.data_inventaris[product_id] = produk_baru
        print(f"\n[Sukses] Produk '{nama_produk}' berhasil ditambahkan.")

    def cari_produk(self, product_id):
        """Mencari detail produk berdasarkan ID Produk dengan kompleksitas rata-rata O(1)."""
        if product_id in self.data_inventaris:
            print("\n--- HASIL PENCARIAN PRODUK ---")
            print(self.data_inventaris[product_id])
        else:
            print(f"\n[Informasi] Produk dengan ID '{product_id}' tidak ditemukan.")

    def hapus_produk(self, product_id):
        """Menghapus produk dari sistem berdasarkan ID Produk dengan kompleksitas O(1)."""
        if product_id in self.data_inventaris:
            produk_dihapus = self.data_inventaris.pop(product_id)
            print(f"\n[Sukses] Produk '{produk_dihapus.nama_produk}' (ID: {product_id}) telah dihapus dari sistem.")
        else:
            print(f"\n[Gagal] Produk dengan ID '{product_id}' tidak ditemukan untuk dihapus.")

    def tampilkan_semua(self):
        """Menampilkan seluruh daftar produk yang tersimpan di inventaris."""
        if not self.data_inventaris:
            print("\n[Informasi] Belum ada data produk di dalam inventaris.")
            return
        
        print("\n================ DAFTAR INVENTARIS PRODUK ================")
        for produk in self.data_inventaris.values():
            print(produk)
        print(f"Total Jenis Produk Unik: {len(self.data_inventaris)}")
        print("==========================================================")


def main():
    manager = InventarisManager()
    
    # Menambahkan beberapa data contoh awal
    manager.tambah_produk("P001", "Laptop Gaming X", "Elektronik", 15000000, 12)
    manager.tambah_produk("P002", "Mouse Wireless Ergonomis", "Aksesoris", 250000, 45)
    manager.tambah_produk("P003", "Mechanical Keyboard RGB", "Aksesoris", 750000, 30)

    while True:
        print("\n=== SISTEM MANAJEMEN INVENTARIS E-COMMERCE ===")
        print("1. Tambah Produk Baru")
        print("2. Cari Detail Produk Berdasarkan ID")
        print("3. Hapus Produk")
        print("4. Tampilkan Semua Produk")
        print("5. Keluar Program")
        
        pilihan = input("Pilih menu (1-5): ").strip()
        
        if pilihan == "1":
            pid = input("Masukkan ID Produk (contoh: P004): ").strip()
            nama = input("Masukkan Nama Produk: ").strip()
            kategori = input("Masukkan Kategori: ").strip()
            try:
                harga = float(input("Masukkan Harga (Rp): "))
                stok = int(input("Masukkan Jumlah Stok: "))
                manager.tambah_produk(pid, nama, kategori, harga, stok)
            except ValueError:
                print("\n[Error] Harga harus berupa angka desimal dan stok berupa bilangan bulat!")
        
        elif pilihan == "2":
            pid = input("Masukkan ID Produk yang ingin dicari: ").strip()
            manager.cari_produk(pid)
        
        elif pilihan == "3":
            pid = input("Masukkan ID Produk yang ingin dihapus: ").strip()
            manager.hapus_produk(pid)
        
        elif pilihan == "4":
            manager.tampilkan_semua()
        
        elif pilihan == "5":
            print("\nKeluar dari program. Terima kasih!")
            break
        else:
            print("\n[Peringatan] Pilihan tidak valid. Silakan masukkan angka 1 hingga 5.")


if __name__ == "__main__":
    main()