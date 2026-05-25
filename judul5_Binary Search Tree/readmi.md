TUGAS AKHIR JUDUL 5 BINARY SEARCH TREE (BST) DASAR
- PENYIMPANAN ID MAHASISWA
  

SOURCE CODE:


![alt text](https://github.com/afifahnaurah-aljabar/Aljabar-matriks-tugas-/blob/925a07c3b9d626842fd73d602b6d39d50507e9ff/Screenshot%202026-05-24%20193725.png?raw=true)


penjelasan
- class node: adalah sebuah kelas yang bernama (node) fungsinya sebagai tempat awal atau kerangka untuk setiap simpul pada tree.
- def __init__(self, key): adalah fungsi otomastis yang yang dijalankan saat buat node baru, dan parameter key yaitu nilai misalnya ID mahasiswa yang disimpan pada simpul
- self.key = key : adalah baris penyimpan nilai yang dimasukkan dalam stribut key dari simpul tree
- self.left = None : adalah tempat untuk child subpohon kiri
- self.right = None : adalah tempat untuk child subpohon kanan

  ![ alt text](https://github.com/afifahnaurah-aljabar/Aljabar-matriks-tugas-/blob/a09345b95ee7c3345c7531b0165f40f444eafccc/Screenshot%202026-05-24%20193832.png?raw=true)

  penjelasan

  - class BSTDasar : adalah kelas bernama BSTDasar binary tree
  - def __init__(self) : menjalankan program saat objek dibuat
  - self.root = None : adalah awal saat tree dibuat rootnya none atau kosong
  - def insert_node(self, root, key)
  - if root is None : adalah jika root kosong, maka node akan dibuat dengan nilai key sebagai nilai baru yang telah dibuat
  - return Node(key) : adalah tempat data tersimpan pada anak kiri dan anak kanan
  - if key < root.key : adalah jika nilai yang dimasukkan lebih kecil dari node saat itu
  - root.left = self.insert_node(root.left, key) : adalah fungsi yang memanggil dirinya sendiri atau rekursif dan mencari posisi di sebelah kiri
  - elif key > root.key : adalah jika nilai yang dimasukkan lebih besar dari dari node saat itu
  - root.right = self.insert_node(root.right, key) : adalah fungsi yang memanggil dirinya sendiri atau rekursif dan mencari posisi di sebelah kanan
  - return root : adalah tempat pengembalian node.
 

    ![alt text](https://github.com/afifahnaurah-aljabar/Aljabar-matriks-tugas-/blob/a3252337975a4315fc2d41b8ed6e88b700c30bb3/Screenshot%202026-05-24%20193845.png?raw=true)


    penjelasan

    - self.root = self.insert_node(self.root, key) : adalah pemanggil fungsi pembantu dengan rekursif untuk menempatkan key pada posisi yang tepat serta untuk memperbarui struktur root tree
    - search_node(self, root, key): adalah fungsi pencari apakah nilai atau key ada di dalam tree
    - if root is None : jika ujung cabang nodenya kosong, lalu nilai belum ditemukan, maka fungsi akan mengembalikan False
    - if root.key == key : adalah jika nilai pada node sama dengan nilai  yang dicari maka fungsi akan mengembalikan nilai true
    - if key < root.key : adalah jika ninail yang dicari lebih kecil dari nilai node saat ini, maka pencarian akan dilanjutkan ke root let atau cabang kiri
    - return self.search_node(root.right, key) : adalah jika jika nilai yang diacri lebih besar dari node saat ini, maka pencarian akan dilanjutkan ke root right atau cabang kanan



      ![alt text](https://github.com/afifahnaurah-aljabar/Aljabar-matriks-tugas-/blob/66470f193fb6d7615a98aa2a65050e9f82eeba61/Screenshot%202026-05-24%20193901.png?raw=true)



penjelasan

-  def search(self, key) : adalah fungsi pecarian berparameter key
-  return self.search_node(self.root, key) : adalah pemanggil fungsi jadi dia mencari dari titik paling atas tree atau self.root
-  def inorder(self, root) : adalah metode dengan mengunjungi setiap node dengan urutan tertentu dan hasil akan menampilkan nilai terkecil ke terbesar
- if root is None : adalah jika node yang diperiksa kosong, maka fungsi berhenti dan akan kembali ke pemanggilnya
- self.inorder(root.left) : adalah fungsi yang memanggil dirinya sendiri atau rekursif untuk pindah ke cabang kiri sejauh mungkin
- print(root, kry, rnd=" ") : adalah tempat mencetak nilai key dari node yang lagi dikunjungi dan parameter end adalah untuk memastikan hasil cetak menyamping dengan spasi
- self.inorder(root.right) : adalah fungsi yang memanggil dirinya sendiri untuk mengunjungi cabang sebelah kanan

![alt text](https://github.com/afifahnaurah-aljabar/Aljabar-matriks-tugas-/blob/2f8d210f8f4acfd022931a4235a0a48fb857cc46/Screenshot%202026-05-24%20193910.png?raw=true)


penjelasan: 


- def preorder(self, root):
- if root is None return : adalah base case, dimana saat fungsi sampai ke simpul node (kosong), maka rekursi akan berhenti dan kembali ke pemanggilya
- print(root.key, end=" ") : adalah mencetak nilai di simpul saat ini, atau root sebelum berpindah ke cabang lain
- self.preorder(root.left) : adalah untuk melakukan pemanggilan rekursif ke child left
- self.preorder(root.right) : adalah untuk melakukan pemanggilan rekiursif ke kanan
- if root is None : return : adalah untuk memastikan rekursi berhenti pada saat sampai di simpul yang kosong
- self.postorder(root.left) : adalah untuk melakukan rekursi ke cabang kiri hingga mencapai paling ujung
- self.postorder(root.right) : adalah untuk melakukan rekursi ke cabang kanan
- print(root.key, end=" ") : adalah tempat untuk mencetak nilai simpul setelah proses selesai



  ![alt text](https://github.com/afifahnaurah-aljabar/Aljabar-matriks-tugas-/blob/80629126a5f7e29a6de925c25de074b112e33e18/Screenshot%202026-05-24%20193919.png?raw=true)



penjelasan:


- def find_min(self, root) : adalah untuk mencari nilai terkecil di tree atau yang berada pada cabang kiri
- if root is None return 1 : adalah tempat pengecekan apakah tree kosong, dan saat kosong maka fungsi akan mengembalikan -1
- current = root : adalah tempat untuk menetapkan titik awal pencarian dari akar pohon atau rootnya
- while current.left is not None : adalah tempat perulangan saat simpul punya anak di kiri
- current = current.left : adalah untuk melakukan pergerakan terus ke kiri tree
- return current.key : adalah pada saat sampai simpul paling kiri, maka fungsi akan mengembalikan nilai atau key sebagai nilai minimum
- def find_max(delf, root) : adalah fungsi untuk mencari nilai paling besar dan berada di simpul kanan
- if root is None return -1 : adalah jika pohon kosong, maka fungsi akan mengembalikan -1
- current = root : adalah untuk menetapkan titik awal pencarian di akar pohon
- while current.right is not None : adalah tempat untuk melakukan loop selama simpul masih punya anak di kanan tree
- current = current.right : adalah terus bergerak ke kanan tree
- return current.key : adalah pada saat sampai di simpul paling kanan, maka fungsi akan mengembalikan nilai atau key ke nilai maximum.





![alt text](https://github.com/afifahnaurah-aljabar/Aljabar-matriks-tugas-/blob/440835fb6531e9c935b7a709a806c09e064699ae/Screenshot%202026-05-24%20193927.png?raw=true)




penjelasan:


- def count_nodes(self, root) : adalah fungsi untuk menghitung total jumlah node dalam tree
- if root is None: return 0 : adalah base case jika fungsi sampai di bagian none tree atau kosong, dan dia akan mengembalikan nilai 0
- return 1 + self.count_nodes(root.left) : adalah 1 node saat ini, lalu mencari dan menjumlahkan node pada cabang kiri
- self. count_nodes(root.right) : adalah tempat mencari serta menjumlahkan node pada cabang kanan
- def sum_nodes(self, root) : adalah fungsi yang digunakan untuk menjumlahkan total nilai atau key yang tersimpan di tiap-tipa node tree
- if root is None: retun 0 : adalah nilai akan 0 saaat node kosong biar tidak berpengaruh ke hasil penjumlahannya
- return root.key + self.sum_nodes(root.left) : adalah tempat mengambil nilai pada node saat ini, lalu untuk menambahkan nilai total dari node pada cabang kiri tree
- self.sum_nodes(root.right) : adalah untuk menambhakan nilai total dari node di cabang kanan tree



  ![alt text](https://github.com/afifahnaurah-aljabar/Aljabar-matriks-tugas-/blob/d075a69f166334749accfd13d097652500f412f0/Screenshot%202026-05-24%20193942.png?raw=true)



  penjelasan:



  - bst = BSTDasar() : mendefinisikan objek bernama BSTDasar
  - pilih = 0 : variabel pilih 0 adalah tempat penyimpanan nilai yang dipilih
  - while pilih != 10 : adalah loop yang akan berjalan jika kita tidaak memilih nilai 10
  - print(...) : adalah tempat untuk mencetak daftar menu yaitu insert, search, inorder, preorder, postorder) dan min, max, total, dan sum)
  - try : adalah blok penanganan jika terjadi kesalahan saat memasukkan input
  - pilih = int(input("pilih: ") : adalah program meminta kita menginputkan angka, dan int() akan mengubah input text dari kita menjadi bilangan bulat integer
  - except ValueError : saat pengguna menginputkan selain angka atau memasukkan huruf, maka program akan masuk ke bagian blok ini
  - print("input tidak valid" ) : adalah tempat menampilkan pesan jika terjadi kesalahan atau jika menginputkan selain angka
  - continue : adalah perintah dari program untuk mengabaikan sisa kode dibawahnya lalu kembali ke awal loop while untuk mengambil input secara ulang
  
