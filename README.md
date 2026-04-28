Tugas akhir percobaan 1 list

judul projek: sistem belanja barang

proyek ini adalah sistem yang digunakan untuk mempermudah pelangan dalam memesan barang atau pakaian. disini saya menggunakan
list 2D pada python dimana diawal jumlah barang belanja atau item  pelangan di masukkan lalu pada akhir (selesai) tertera
ringkasan atau total belanja dari pelangan.

source code

image 1


<img width="518" height="199" alt="Image" src="https://github.com/user-attachments/assets/77c3b7c4-eb3b-4c9c-af7f-a0d1c0b52cca" />


pada gambar tersebut def tampilkan menu berisi baris untuk mendeklarasiakan menu
lalu print "menu toko baju" yaitu untuk mencetak judul menu
lalu pada baris ke 4 sampai 6 terdapat pilihan barang yang tersedia
- Kemeja: Rp. 10.000
- Celana: Rp. 5.000
- Jilbab: Rp. 15.000

lalu print("4. selesai & bayar").

image 2 


<img width="728" height="220" alt="Image" src="https://github.com/user-attachments/assets/f11d7ebb-72f4-4649-b7f2-f8080a88cb09" />



def main() baris 9: mendeklarasikan fungsi utama main.
keranjang = [] baris 10: untuk menyimpan item atau barang yang dibeli pelanggan.
harga barang: baris 11 adalah dictionary tempat menyimpan daftar harga 
nama barang baris ke 14: item yang dipilih pelanggan.
total belanja = 0
sedang belanja = true.

image 3


<img width="921" height="337" alt="Image" src="https://github.com/user-attachments/assets/6aecc06a-4941-4838-8afc-0d5a38f1f54f" />


while sedang berjalan: perulangan bernilai = True
tampilkan menu() memanggil fungsi menunjukkan daftar item yang tersedia.
pilihan 1,2,3
if pilihan: in{1,2,3} memeriksa apakah pilihan pelanggan ada di daftar menu.
int berapa banyak barang yang dibeli pelanggan (misalnya: jilbab 30.00 x 1) = 30.000.
print: berhasil menambahkan ke keranjang. berhasil.

image 4



<img width="735" height="466" alt="Image" src="https://github.com/user-attachments/assets/cea81eb6-52e0-4f04-b6a8-86a8a737807d" />



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
  







