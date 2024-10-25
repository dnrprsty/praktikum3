# Program Menemukan Bilangan Tertinggi

Sebuah program sederhana yang dirancang untuk menemukan nilai tertinggi dari sejumlah bilangan yang dimasukkan oleh pengguna, dengan memanfaatkan loop `while True` dan pernyataan `break`.

## Rincian Program

Program ini ditulis dalam bahasa Python dan memiliki fitur sebagai berikut:

- Menggunakan loop `while True` untuk perulangan yang tidak terbatas
- Memanfaatkan pernyataan `break` untuk mengakhiri eksekusi program
- Membandingkan setiap masukan dengan nilai maksimum yang sudah ada
- Menampilkan bilangan tertinggi yang berhasil ditemukan

## Contoh Kode

```python
def find_max_number():
    max_number = None
    
    while True:
        user_input = input("Masukkan bilangan (atau ketik 'exit' untuk keluar): ")
        
        if user_input.lower() == 'exit':
            break
        
        try:
            number = float(user_input)
            if max_number is None or number > max_number:
                max_number = number
        except ValueError:
            print("Harap masukkan bilangan yang valid.")

    if max_number is not None:
        print(f"Bilangan terbesar yang ditemukan adalah: {max_number}")
    else:
        print("Tidak ada bilangan yang dimasukkan.")

# Menjalankan fungsi
find_max_number()
