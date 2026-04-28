Tugas akhir percobaan 1 list
judul projek: sistem belanja barang

proyek ini adalah sistem yang digunakan untuk mempermudah pelangan dalam memesan barang atau pakaian. disini saya menggunakan
list 2D pada python dimana diawal jumlah barang belanja atau item  pelangan di masukkan lalu pada akhir (selesai) tertera
ringkasan atau total belanja dari pelangan.

source code:
https://github.com/afifahnaurah-aljabar/Aljabar-matriks-tugas-/blob/a75b2e934f326311502e4249b4e21889239aaca8/Screenshot%202026-04-28%20195647.png


pada gambar tersebut def tampilkan menu berisi baris untuk mendeklarasiakan menu
lalu print "menu toko baju" yaitu untuk mencetak judul menu
lalu pada baris ke 4 sampai 6 terdapat pilihan barang yang tersedia
- Kemeja: Rp. 10.000
- Celana: Rp. 5.000
- Jilbab: Rp. 15.000

lalu print("4. selesai & bayar").

image 2 

def main() baris 9: mendeklarasikan fungsi utama main.
keranjang = [] baris 10: untuk menyimpan item atau barang yang dibeli pelanggan.
harga barang: baris 11 adalah dictionary tempat menyimpan daftar harga 
nama barang baris ke 14: item yang dipilih pelanggan.
total belanja = 0
sedang belanja = true.

image 3

while sedang berjalan: perulangan bernilai = True
tampilkan menu() memanggil fungsi menunjukkan daftar item yang tersedia.
pilihan 1,2,3
if pilihan: in{1,2,3} memeriksa apakah pilihan pelanggan ada di daftar menu.
int berapa banyak barang yang dibeli pelanggan (misalnya: jilbab 30.00 x 1) = 30.000.
print: berhasil menambahkan ke keranjang. berhasil.

image 4


pada elif pilihan == 4 variabel 
sedang berjalan menjadi = False yang akan menghentikan loop atau perulangan.
else
except ValueError: menangani jika memasukkan huruf saan program menginput angka.
baris ke-36: print ringkasan belanja, setelah keliuar dari lop belanja program mencetak daftar item yang ada di list
keranjang menambahkan lalu menampilkan = total biaya digambar tertera Rp. 30.000.

output

=== sistem belanja total ===
- Kemeja: Rp. 10.000
- Celana: Rp.5000
- Jilbab: Rp.15.000
  total: Rp 30.000

  selesai.
  







