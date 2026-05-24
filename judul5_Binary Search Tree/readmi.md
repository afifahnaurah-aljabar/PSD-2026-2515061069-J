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

