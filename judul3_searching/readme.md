TUGAS AKHIR JUDUL 3 SEARCHING

PROJEK: PENCARIAN DATA NILAI UTS MAHASISWA

pencarian nilai uts mahasiswa saya menggunakan linear search atau sequential search
dengan sekumpulan data nilai mahasiswa yang belum terurut.

source code:

![alt text](https://github.com/afifahnaurah-aljabar/Aljabar-matriks-tugas-/blob/main/Screenshot%202026-05-09%20190353.png?raw=true?raw=true)


penjelasan: 

data adalah jumlah nilai yang akan diperiksa, lalu n adalah jumlah total elemen dalam data, lalu target adalah nilai yang ingin dicari
dalam data. pada baris ke 2 yaitu i = 0 adalah indeks i bernilai 0 posisi untuk mengecek nilai dari elemen pertama. lalu baris ke 3
yaitu counter = 0 ini adalah variabel yang digunakan untuk menghitung berapa kali nilai atau target ditemukan di dalam data.
lalu while i < n: adalah perulangan jika nilai indeks i masih lebih kecil dari jumlah total data n. dan untuk memastikan bahwa setiap data diperiksa satu per satu.
lalu pada if data [i] == target: untuk mengecek elemen indeks ke-i punya nilai yang sama dengan target atau tidak.
lalu counter += 1 jika nilai ditemukan, maka counter ditambah 1 nilainya. lalu i += 1 ini menambah nilai 1 untuk pindah ke elemen selanjutnya.
lalu return counter: jika semua elemen selesai diperiksa dengan perulangan, maka fungsi akan kembalidari total jumlah yang ditemukan dan disimpan dalam counter.



source code 2:


![alt text](https://github.com/afifahnaurah-aljabar/Aljabar-matriks-tugas-/blob/ebb98859aea0ecc095bd746c4dd70cc5ddf3f082/Screenshot%202026-05-09%20190404.png?raw=true)



penjelasan:


data: berisi sekumpulan angak acak [70, 80, 30, 60, 70, 40, 30, 80, 50]. 
n = len(data) untuk menghitung jumlah elemen.
print(f"Data array: {data}") : untuk menampilkan isi data.
While True : perulangan terus-menerus dari program
try : jika terjadi kesalahan disini tempat penanganannya misal jika memasukkan teks bukan angka.
target = n int(input("masukkan angka yang ingin dicari: ")) : user disuruh masukin angka yang ingin dicari
break : jika input benar loop akan berhenti
counter = sequential_search(data, n, target) : untuk menghitung berapa kali angka atau target muncul di dalam data
if counter > 0 : untuk mengecek angka yang muncul lebih dari nol atau tidak
print(f"Angka {target} ditemukan sebanyak {counter} kali. ") : jika ada, tampilkan jumlah yang muncul
print(f"Angka {target} tidak ditemukan. ") : jika tidak ada atau 0, maka tampilkan pesan bahwa angka tidak ada di dalam daftar



output/hasil: 

![alt text](https://github.com/afifahnaurah-aljabar/Aljabar-matriks-tugas-/blob/d806624a2f18879cef97d1e5107e870bbf212211/Screenshot%202026-05-09%20191150.png?raw=true)
![alt text](https://github.com/afifahnaurah-aljabar/Aljabar-matriks-tugas-/blob/6a70d0cdaa9b12f20dddc2c2ed3ee62a28e29c43/Screenshot%202026-05-09%20191222.png?raw=true)
![alt text](https://github.com/afifahnaurah-aljabar/Aljabar-matriks-tugas-/blob/5a43ca33551493af17df1e2ffb96994549f9550c/Screenshot%202026-05-09%20191244.png?raw=true)


penjelasan: 

masukkan angka yang ingin dicari misalnya kita masukkan 70
maka angka 70 ditemukan sebanyak 2 kali. atau misalnya masukkan angka 80 atau 20 yang 
ditemukan sebanyak masing-masing 3 kali, tergantung kita jumlah elemen yang diinputkan ada berapa 
jumlahnya.









