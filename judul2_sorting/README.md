TUGAS AKHIR JUDUL 2 SORTING 



PROJEK: mengurutkan kartu dari nilai terkecil ke nilai terbesar (Ascending) Bubble Sort


source code:
![alt text](https://github.com/afifahnaurah-aljabar/PSD-2026-2515061069/blob/main/Screenshot%202026-05-03%20082513.png?raw=true?raw=true) 



penjelasan: 
def tukar(arr, i, j)
def temp = arr [j]:
digunakan untuk menukar posisi 2 elemen dan juga untuk menyimpan nilai elemen.
arr[i] = arr[i] digunakan untuk mengganti nilai elemen ke 1 ke elemen 2.
arr[j] = temp digunakan untuk mengisi elemen 2.




def bubble_sort(arr, n): digunakan untuk melakukan pengurutan nilai elemen.
for i in range (-1): adalah perulangan yang menentukan berapa kali proses pemindahan nilai list dijalankan.
for j in range (n-i-1): adalah perulangan yang digunakan untuk membandingkan elemen yang bersebelahan.
if arr[j] > arr[j = 1]: tempat untuk menukar elemen jika sebuah elemen saat ini lebih besar dari elemen di depannya, jadi harus ditukar.
tukar(arr, j, + 1): digunakan untuk memanggil fungsi ( tukar ) untuk memindahkan elemen yang lebih besar ke karan.







source code 2:





![alt text](https://github.com/afifahnaurah-aljabar/PSD-2026-2515061069/blob/d5cc52fac50e3d79e1345007013172a7b424f436/Screenshot%202026-05-03%20082554.png?raw=true)


penjelasan:

def main(): digunakan untuk menerima input atau angka yang dimasukkan.
try
n = int(input("4")): berfungsi untuk memasukkan angka atau elemen yang diinginkan pengguna.
except ValueError: berfungsi untuk menangani kesalahan misalnya memasukkan sesain angka.
print("input tidak valid")
return
arr = []: adalah list kosong yang digunakan untuk penampungan angka.
print("2,4,3,5"): adalah jumlah elemen yang dimasukkan.
for i in range(n); adalah perulanagn yang akan berjalan sebanyak beberapa kali untuk meminta input angka satu per satu yang dimasukkan.
while true: kepastian memasukkan angka apakah sudah valid atau belum jika belum program akan meminta untuk terus meminta input sampai valid.
try
nilai = int(input()): digunakan untuk mengambil nilai yang diinputkan dan mengubahnya ke bilangan integer.
arr.append(nilai): digunakan untuk menambahkan angka baru yang dimasukkan dalam arr.
break
except ValueError: berfungsi untuk menangkap kesalahan jika memasukkan elemen selain angka.
print("input tidak valid, silahkan memasukkan angka!"): berfungsi untuk mengumumkan masukkan angka yang benar.

print(f"2,4,3,5 (arr)"): memasukkan elemen sebelum diurutkan sesuai yang diinputkan di awal.
bubble_sort(arr, n): berfungsi untuk memanggil fungsi untuk mengurutkan nilai.
print("2,3,4,5 (Bubble Sort):" , end=" "): adalah perulanagan yang berfungsi untuk mencetak elemen yang sudah diurutkan.
print(): mencetak beris elemen baru setelah semua ditampilkan.
if __name__ == "__main__": adalah variabel ksusus python
main(): adalah pemanggilan fungsi.



output:



![alt text](https://github.com/afifahnaurah-aljabar/PSD-2026-2515061069/blob/d5cc52fac50e3d79e1345007013172a7b424f436/Screenshot%202026-05-03%20082605.png?raw=true)



penjelasan:

adlah list sebelum diurutkan: (2,4,3,5[2,4,3,5]).
hasil: (2,3,4,5 (Bubble Sort): 2,3,4,4).
adalah hasil akhir atau outputnya dari pengurutan kartu dari yang terkecil ke yang terbesar (Ascending).






