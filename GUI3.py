import tkinter as tk
from tkinter import messagebox

class AplikasiPesanMakanan:
    def __init__(self, root):
        self.root = root
        root.title("Aplikasi Pemesanan Makanan")
        root.configure(bg="#006400")

        # Daftar harga menu
        self.harga_menu = {
            "Nasi Goreng": 20000,
            "Mie Goreng": 15000,
            "Ayam Goreng": 25000,
            "Sate Ayam": 30000
        }

        # Frame untuk formulir pemesanan
        self.frame = tk.Frame(root, bg="#006400")
        self.frame.pack(padx=10, pady=10)

        # Label untuk judul
        self.judul_label = tk.Label(self.frame, text="Pesan Makanan Anda", font=("Helvetica", 16), bg="#006400", fg="white")
        self.judul_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        # Label dan Entry untuk Nama
        self.nama_label = tk.Label(self.frame, text="Nama:", bg="#006400", fg="white")
        self.nama_label.grid(row=1, column=0, sticky="e", padx=(0, 10))
        self.nama_entry = tk.Entry(self.frame)
        self.nama_entry.grid(row=1, column=1, pady=5)

        # Label dan Entry untuk Alamat
        self.alamat_label = tk.Label(self.frame, text="Alamat:", bg="#006400", fg="white")
        self.alamat_label.grid(row=2, column=0, sticky="e", padx=(0, 10))
        self.alamat_entry = tk.Entry(self.frame)
        self.alamat_entry.grid(row=2, column=1, pady=5)

        # Label dan Entry untuk Menu Makanan
        self.makanan_label = tk.Label(self.frame, text="Menu Makanan:", bg="#006400", fg="white")
        self.makanan_label.grid(row=3, column=0, sticky="e", padx=(0, 10))
        self.makanan_entry = tk.Entry(self.frame)
        self.makanan_entry.grid(row=3, column=1, pady=5)

        # Label dan Entry untuk Jumlah
        self.jumlah_label = tk.Label(self.frame, text="Jumlah:", bg="#006400", fg="white")
        self.jumlah_label.grid(row=4, column=0, sticky="e", padx=(0, 10))
        self.jumlah_entry = tk.Entry(self.frame)
        self.jumlah_entry.grid(row=4, column=1, pady=5)

        # Tombol untuk mengirimkan pesanan
        self.pesan_button = tk.Button(self.frame, text="Pesan", command=self.kirim_pesanan, bg="#228B22", fg="white")
        self.pesan_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Kanvas untuk menggambar garis pemisah
        self.canvas = tk.Canvas(root, height=2, bd=0, relief="ridge", bg="black")
        self.canvas.pack(fill="x", padx=10, pady=10)

        # Widget Text untuk menampilkan ringkasan pesanan
        self.ringkasan_pesanan = tk.Text(root, height=10, width=50, state="disabled", bg="#2E8B57", fg="white")
        self.ringkasan_pesanan.pack(padx=10, pady=10)

    def kirim_pesanan(self):
        nama = self.nama_entry.get()
        alamat = self.alamat_entry.get()
        makanan = self.makanan_entry.get()
        jumlah = self.jumlah_entry.get()

        if not nama or not alamat or not makanan or not jumlah:
            messagebox.showwarning("Kesalahan Input", "Semua kolom harus diisi.")
            return

        try:
            jumlah = int(jumlah)
        except ValueError:
            messagebox.showwarning("Kesalahan Input", "Jumlah harus berupa angka.")
            return

        if makanan not in self.harga_menu:
            messagebox.showwarning("Kesalahan Input", "Menu makanan tidak tersedia.")
            return

        harga_per_item = self.harga_menu[makanan]
        total_harga = harga_per_item * jumlah
        detail_pesanan = f"Nama: {nama}\nAlamat: {alamat}\nMenu Makanan: {makanan}\nJumlah: {jumlah}\nHarga per item: Rp{harga_per_item}\nTotal Harga: Rp{total_harga}\n\n"

        self.ringkasan_pesanan.configure(state="normal")
        self.ringkasan_pesanan.insert("end", detail_pesanan)
        self.ringkasan_pesanan.configure(state="disabled")

        self.kosongkan_entry()

    def kosongkan_entry(self):
        self.nama_entry.delete(0, tk.END)
        self.alamat_entry.delete(0, tk.END)
        self.makanan_entry.delete(0, tk.END)
        self.jumlah_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiPesanMakanan(root)
    root.mainloop()


