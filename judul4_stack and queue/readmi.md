TUGAS AKHIR JUDUL 4 STACK AND QUEUE
MENGURUTKAN ANGKA

SOURCE CODE:
![alt text](https://github.com/afifahnaurah-aljabar/tugas-aljabar-matriks-kelompok-5/blob/25f36ae61fb80b6d0c16b0189d63d89573e34e73/Screenshot%202026-05-19%20184154.png?raw=true)

penjelasan:
- stack atau tumpukan menggunakan array list
- self.MAX = sebagai batas maximal elemen yang ditampung
- self.st = sebagai wadah penyimpanan berupa list kosong yang diisi none max_size
- self.top_idx = sebagai penanda elemen paling atas dimulai -1 yaitu stack masih kosong
- def is_empty(self) = atau cek kosong dalam stack atau tumpukan
- def is_full(self) = atau stack penuh dan tidak akan diisi lagi karena akan overflow jika diisi lagi
- def push = sebagai tempat untuk memasukkan data x kedalam stack
- if self.is_full() = program akan mengecek terlebih dahulu apakah stack sudah penuh jika penuh, maka akan muncuk pesan "stack penuh". dan agar tidak terjadi stack overflow.
- print("stack penuh") = bahwa stack sudah penuh dan mencapai batas maximal
- return = sebagai penghenti fungsi. karena stack penuh jadi harus keluar
- self.top_idx += 1 : untuk menambah nilai indeks penanda posisi paling atas 1 kali.
- self.st[self.top_idx] = x : untuk memasukkan nilai x kedalam array atau list self.st atau proses penambahan data ke dalam stack
- print(f"push {x} berhasil") : penanda proses pemasukkan data x telah berhasil dan selesai




code 2:

![alt text](https://github.com/afifahnaurah-aljabar/tugas-aljabar-matriks-kelompok-5/blob/81172555ff23013a32ba45fc75ba031feaa73210/Screenshot%202026-05-19%20184212.png?raw=true)


penjelasan:


- pop(self) = untuk mengambil atau menghapus elemen teratas stack
- if self.is_empty(): = kode pemanggil jika benar akan muncul pesan "stack kosong" dan fungsi berhenti
- return = berhenti
- peek(self) = untuk melihat elemen yang ada paling atas tanpa menghapusnya
- self.top_idx = tempat eksekusi jika ada, program langsung mencetak nilai yang ada di indeks paling atas.
- def display(self) = tempat menampilkan seluruh isi stack dari atas sampai bawah
- for i in range(self.top_idx, -1, -1) = atau looping program membaca indeks paling atas hingga bawah sampai 0.
- end = pengecekan elemen satu persatu dengan parameter end



  code 3:

  ![alt text](https://github.com/afifahnaurah-aljabar/tugas-aljabar-matriks-kelompok-5/blob/342cffdeed1f65d6ba043bd94f42b7f69b566e90/Screenshot%202026-05-19%20184221.png?raw=true)


  penjelasan:

  - def main() = fungsi utama menjalankan logika program
  - stack = StackArray = objek ini digunakan untuk memanggil fungsi-sungsi stack
  - pilih = 0 : adalah variabel untuk menampung pilihan menu dari kita
  - while pilih != 5: loop yang akan berjalan selama nilai yang dipilih bukan 5, jika 5 maka akan berhenti dan keluar
  - try except vallueError = sebagai penanganan jika salah memasukkan input data selain angka misalnya huruf dan akan menampilkan pesan input tidak valid
  - pilih = int(input("pilih: ")) = program mengambil input dari kita dan mengubahnya menjadi integer atau angka dan menyimpannya ke variabel
  - if pilih == 1 : jika kita memilih menu nomor 1 push maka logika pemasukan data akan ada dibawah baris ini



    output
    code:

   ![alt text](https://github.com/afifahnaurah-aljabar/tugas-aljabar-matriks-kelompok-5/blob/8601f1d5e2e830c342e8c6fa0bcd08759f310757/Screenshot%202026-05-19%20194254.png?raw=true)


  penjelasan:
  - pilih 1 dengan fungsi push
  - nilai 24 untuk ditambahkan ke stack
  - push 24 berhasil ditambahkan ke stack


  code:

  ![alt text](https://github.com/afifahnaurah-aljabar/tugas-aljabar-matriks-kelompok-5/blob/63b92bb977a2486c1d94c28691abe9f9eda70dee/Screenshot%202026-05-19%20194301.png?raw=true)

  penjelasan:
  - jika kita memilih 3 fungsi peek
  - maka stack kosong ini adalah respon dari program bahwa data belum ada data yang dimasukkan (push) dalam stack dan tidak ada elemen yang dapat dilihat oleh peek
 
    link youtube: 
    


  
