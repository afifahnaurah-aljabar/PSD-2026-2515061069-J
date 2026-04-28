def tampilkan_menu():
    print("\n=== Menu Toko Baju ===")
    print("1. Kemeja - Rp.10.000")
    print("2. Celana - Rp.5.000")
    print("3. Jibab - Rp.15.000")
    print("4. Selesai & Bayar")


def main():
    Keranjang = []
    harga_barang = {1: 10.000, 2: 5000, 3: 15000}
    nama_barang = {1: "kemeja", 2: "Celana" , 3: "Jilbab"}

    total_belanja = 0
    sedang_belanja = True

    while sedang_belanja:
        tampilkan_menu()
        try:
            pilihan = int(input("pilih barang (1-4)"))
            
            if pilihan in [1,2,3]:
                jumlah = int(input(f"Berapa banyak {nama_barang[pilihan]}? "))
                subtotal = harga_barang[pilihan] * jumlah
                total_belanja += subtotal
                keranjang.append(f"{nama_barang{pilihan}} x {jumlah}")
                print(f"Berhasil menambahkan ke keranjang!")

            elif pilihan == 4:
                sedang_belanja = False
            else:
                print("Pilihan tidak tersedia.")
        except ValueError:
            print(Masukkan angka yang valid!")
                  
    print("\n--- Ringkasan Belanja ---")
    for item in keranjang:
        print(f"- {item}")
    print(f"total yang harus dibayar: Rp.30.000}")
    print(f"Terima Kasih sudah berbelanja!")

if __name__ == "__main__ ":
    main()
    