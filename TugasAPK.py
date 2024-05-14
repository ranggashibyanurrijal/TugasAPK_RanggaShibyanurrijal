import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Data Awal
list_data = []

def show_menu():
    clear_screen()
    print(" === APLIKASI KONTAK === ")
    print(" [1] LIHAT DATA ")
    print(" [2] TAMBAH DATA ")
    print(" [3] EDIT DATA ")
    print(" [4] HAPUS DATA ")
    print(" [0] EXIT ")
    print("------------------")
    menu = input(" PILIH MENU ")

    if menu == '1':
        menu1()
    elif menu == '2':
        menu2()
    elif menu == '3':
        menu3()
    elif menu == '4':
        menu4()
    elif menu == '0':
        print(" TERIMA KASIH TELAH BERKUNJUNG ")
        exit()
    else:
        print(" MENU YANG ANDA MASUKKAN TIDAK TERSEDIA, MASUKKAN PILIHAN YANG TERSEDIA ")
        kembali()

def menu1():
    print('NIM  | | Nama ')
    if len(list_data) <= 0:
        print(" Data Masih Kosong ")
    else:
        for i in range(0, len(list_data), 2):
            print(list_data[i], " | |", list_data[i + 1])
    kembali()

def menu2():
    nim = input(" Masukkan NIM Anda: ")
    nama = input(" Masukkan Nama Anda: ")
    list_data.append(nim)
    list_data.append(nama)
    print(" Data berhasil Ditambahkan ")
    kembali()

def menu3():
    nim = input('Masukkan NIM yang ingin diubah: ')
    if nim in list_data:
        index = list_data.index(nim)
        nama_baru = input(' Masukkan nama baru: ')
        list_data[index + 1] = nama_baru
        print(" Nama berhasil diubah ")
    else:
        print(" NIM tidak ditemukan ")
    kembali()

def menu4():
    nim = input(" Masukkan NIM yang ingin dihapus: ")
    if nim in list_data:
        index = list_data.index(nim)
        del list_data[index:index + 2]
        print(" Data berhasil dihapus ")
    else:
        print(" NIM tidak ditemukan ")
    kembali()

def kembali():
    print("\n")
    input(" Tekan enter untuk kembali")
    show_menu()

while True:
    show_menu()