TUGAS AKHIR JUDUL 6 HASH MAP 






SAYA MENGGUNAKAN OPEN ADDRESSING DENGAN STUDY KASUS "KONTAK NOMOR"


SOURCE CODE:

![alt text](https://github.com/afifahnaurah-aljabar/Aljabar-matriks-tugas-/blob/76270ea5609146241f0c8b17bc1aa7712e820825/Screenshot%202026-06-06%20174503.png?raw=true) 

penjelasan: 
- class slotstate = adalah kelas yang digunakan untuk penanda status ruang penyimpanan dalam hash
- EMPTY = 0 : adalah penanda slot masih kosong dan belum diisi
- OCCUPIED = 1 : adalah penanda slot telah diisi oleh data
- DELETED = 2 : adalah penanda bahwa slot telah dihapus

  \
class Entry:
- self.key = adalah tempat penyimpan kunci unik
- self.value = adalah tempat penyimpan nilai tersebut
- self.state = adalah tempat penyimpan status slot




SOURCE CODE:


![alt text](https://github.com/afifahnaurah-aljabar/Aljabar-matriks-tugas-/blob/5a083c75732870008590e81c9581571735be9988/Screenshot%202026-06-06%20174522.png?raw=true)



penjelasan:
- class HahMapOpenAddressing : sebagai kelas utama
- def __init__(self, size=10) = untuk penyimpan key dan value dalam tabel hash
- self.SIZE = adalah untuk menentukan ukuran tabel hash digambar tertera 10
- self.table = [Entry() for _ in range(self.SIZE)] = tempat daftar array yang berisi objek Entry


- def hash_function(self. key) = adalah tempat untuk menentukan dimana data akan disimpan
- hash(key) = adalah pengubah kuci text atau angka yang diubah menjadi integer
- % self.SIZE = menggunakan operasi modulo agar angka ada di indeks 0-9 misalnya
- self.SIZE = adalah untuk memastikan hasil modulo tetap positif jika fungsi hash berangka negatif





SOURCE CODE:



![alt text](https://github.com/afifahnaurah-aljabar/Aljabar-matriks-tugas-/blob/c0e809c153c5e989d2abe2bcc34f928c96f9d9af/Screenshot%202026-06-06%20174540.png?raw=true)




penjelasan:
- def insert(self, key, value)
- idx= = self.hash_function(key) = adalah untuk menghitung posisi indeks di awal dengan fungsi hash
- first_deleted = -1 = adalah variabel tempat mencatat indeks awal dengan status deleted
- for step in rang(self.SIZE)
- i = (idx + step) % self.SIZE = adalah untung menghitung indeks baru dari step ini dan % untuk indek agar tetap berada dalam batas tabel
- slotstate.OCCUPIED = adalah jika slot terisi maka nilai akan diperbarui dengan value baeu dan fungsi selesai (return true)
- slotstate DELETED = adalah jika slot telah dihapus, program mencatat indeks first_deleted
- else = adalah jika ditemukan slot yang kosong ini jika ada slo deleted lalu data baru masuk ke slot tersebut dan jika tidak ada slot deleted, data akan masuk ke slot kosong saat ini
- first_deleted = adalah saat loop selesai dan key tidak ditemukan di slot OCCUPIED, tapi slot DELETED ada yang tersimpan lalu data tersebut masuk ke first_deleted




SOURCE CODE:

![alt text](https://github.com/afifahnaurah-aljabar/Aljabar-matriks-tugas-/blob/58cc2410168520dd8b11d0f38c9364c76487836b/Screenshot%202026-06-06%20174557.png?raw=true)



penjelasan:
- def search(self, key): = adalah fungsi yang digunakan untuk menemukan data dalam tabel berdasarkan key
- idx = self.hash_function(key) = adalah tahap awal yang digunakan untuk menghitung indeks awal\
- for step in range(self.SIZE): = adalah untuk melakukan loop sebanyak size tabel untuk mencari key
- i = (idx + step) % self.SIZE  = adalah untuk menentukan indeks sebelumnya yang telah diperiksa
- if self.table[i].state == AlotState.EMPTY: = adalah saat menemukan slot yang kosong, dan data tidak ada dalam tabel, maka fungsi mengembalikan None
- if self.table[i].state == SloteState.OCCUPIED and self.table[i].key == key: adalah saat slot terisi dan key cocok, maka data ditemukan dan fungsi mengembalikan data tersebut
- remove_key(self, key) = adalah fungsi untuk menghapus data dari tabel hash
- entry = self.search(key) = adalah untuk memanggil fungsi search untuk mencari tahu apakah key tersebut ada dalam tabel
- if entry is None: return False = adalah jika key tidak ditemukan, maka fungsi akan mengembalikan False
- entry.state = SloteState.DELETED = adalah jika ditemukan, maka status slot akan DELETED





SOURCE CODE:


![alt text](https://github.com/afifahnaurah-aljabar/Aljabar-matriks-tugas-/blob/d6a003715cf266ca518fca241a46f03bd10c4d02/Screenshot%202026-06-06%20174609.png?raw=true)




penjelasan:
- def display(self): = adalah untuk menampilkan isi dari table hash (linear probing)
- for i in range(self.SIZE): = adalah loop tempat memerikasa slot dalam tabel dari 0-9 sesuai max size table hash
- if self.table[i].state == SlotState.EMPTY = untuk memeriksa data di slot kosong atau tidak jika ya maka akan EMPTY
- if self.table[i].state == SlotState.DELETED = adalah untuk memeriksa data dalam slot sudah dihapus atau belum, jika dihapus maka akan DELETED
- else = adalah saat slot kosong dan tdak dalam status dihapus maka program mencetak sis data dengan format (key, value)




SOURCE CODE:


![alt text](https://github.com/afifahnaurah-aljabar/Aljabar-matriks-tugas-/blob/915689a7a4845f4d860d5c2bda92c64228c83c75/Screenshot%202026-06-06%20174629.png?raw=true)





penjelasan:
- def main()
- hashmap = HashMapOpenAddressing(10) = adalah tabel hash berkapasitas 10 slot
- hashmap.insert(...) = adalah untum memasukkan key dan value kedalam hash map pada gambar misalnya "Zia", "Ani", "Yona", dan "Lin"
- hashmap.display() = adalah perintah menampilkan isi table hash dalam slot
- hasil = hashmap.search("Ani") = mencari data dengan key "Ani" dalam tabel
- jika "Ani" ditemukan, maka key 'Ani' ditemukan, value = 085638462048
- jika "Ani" tidak ditemukan, maka program run else dan menampilkan key 'Ani' tidak ditemukan





  SOURCE CODE:


  ![alt text](https://github.com/afifahnaurah-aljabar/Aljabar-matriks-tugas-/blob/bada0ae3750332b3a3272b056ce40f7c1000e214/Screenshot%202026-06-06%20174650.png?raw=true)


  penjelasan:
  - hashmap.remove_key("Ani") = adalah untuk menghapus data dengan key "Ani" dalam hash map
  - hashmap.display() = adalah fungsi memanggil untuk menampilkan isi tabel hash map terbaru
  - hasil = hashmaop.search('Yona'): adalah untuk melakukan searching data kunci "Yona" dan hsilnya disimpan di variasi tabel
  - if else
  - if hasil is not None = adalah jika "Yona" ditemukan, akan menampilkan key tersebut masih ada dengan value yang disimpan
  - else = adalah saat "Yona" tidak ditemukan, maka nobne atau kosong dan akan menmpilkan pesan key tersebut tidak ditemukan
  - if __name__ == " __main__ ": main() : = adalah blok untuk memastikan fungsi main() dijalankan jika di run langsung




SOURCE CODE OUTPUT:



![alt text](https://github.com/afifahnaurah-aljabar/Aljabar-matriks-tugas-/blob/5b16168b72a30601fe362d558d9ebe289baf61b0/Screenshot%202026-06-06%20174708.png?raw=true)

- adalah outputnya = indeks 0-9
- isi hash table = indeks 0 ada dalam data Yona
- EMPTY = penanda slot kosong dan siap diisi data baru
- operasi = key 'Ani' ditemukan artinya Ani berhasil ditambahkan ke indeks 9 yang diambil dari nomor teleponnya
- setelah menghapus key 'Ani' = deleted bahwa proses pengosongan slot di indeks 9. dalam linear probing, setelah dihapus maka slot di beri penanda agar tidak tabrakan


- adalah outputnya ke-2:
- isi hash table (open addresing, linear probing):
- indeks 0 dan 1 : berisi data "Yona" dan "Lin" serta nomor telepon
- indeks 2 sampai 6 : berstatus EMPTY atau kosong dan belum diisi data sebelumnya
- indeks 8 : berisi data "Zia"
- indeks 9 : berstatus DELETED : sebagai penanda sebelumnya terisi data pada slot ini, tapi telah dihapus
- operasi : key 'Yona' masih ditemukan, value = 085436293749 : yang menunjukkan pencarian  berhasil menemukan data dengan key "Yona" pada tabel hash map serta mengembalikan velue berupa nomor telepon yang telah tersimpan.










link youtube: https://youtu.be/w0GfPyXwP0Q?si=6yV6SsmWr0nG7gp8





