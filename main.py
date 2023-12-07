import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from stegano import lsb

def hide_message():
    # Mendapatkan teks dari input pengguna dan menyembunyikannya dalam gambar
    message = entry_message.get()
    image_path = entry_image.get()
    secret = lsb.hide(image_path, message)
    secret.save("output_image.png")
    label_status.config(text="Pesan berhasil disembunyikan!")
    show_image("output_image.png")

def reveal_message():
    # Mengekstrak dan menampilkan pesan tersembunyi dari gambar
    image_path = entry_image.get()
    try:
        extracted_message = lsb.reveal(image_path)
        label_status.config(text=f"Pesan yang berhasil diambil: {extracted_message}")
    except Exception as e:
        label_status.config(text=f"Gagal mengekstrak pesan: {e}")

def show_image(image_path):
    # Menampilkan gambar di jendela
    img = Image.open(image_path)
    img = img.resize((300, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = tk.Label(window, image=img)
    panel.image = img
    panel.pack()

# Membuat jendela utama
window = tk.Tk()
window.title("Steganography App")

# Membuat label dan input untuk pesan
label_message = tk.Label(window, text="Masukkan Pesan:")
label_message.pack(pady=5)
entry_message = tk.Entry(window, width=30)
entry_message.pack(pady=5)

# Membuat label dan input untuk path gambar
label_image = tk.Label(window, text="Masukkan Path Gambar:")
label_image.pack(pady=5)
entry_image = tk.Entry(window, width=30)
entry_image.pack(pady=5)

# Tombol untuk menyembunyikan pesan
button_hide = tk.Button(window, text="Sembunyikan Pesan", command=hide_message)
button_hide.pack(pady=10)

# Tombol untuk mengekstrak pesan tersembunyi
button_reveal = tk.Button(window, text="Ambil Pesan Tersembunyi", command=reveal_message)
button_reveal.pack(pady=10)

# Label untuk menampilkan status
label_status = tk.Label(window, text="")
label_status.pack(pady=10)

# Tombol untuk memilih gambar
button_select_image = tk.Button(window, text="Pilih Gambar", command=lambda: entry_image.insert(tk.END, filedialog.askopenfilename()))
button_select_image.pack(pady=10)

# Menjalankan loop utama
window.mainloop()
