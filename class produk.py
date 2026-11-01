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