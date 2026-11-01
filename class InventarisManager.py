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