#!/bin/bash

# --- Glosarium Tonyooi ---
# Sooq / Soq      : Sudah / Selesai
# Ginaaq          : Belum
# Kena / Kena'    : Benar / Berhasil
# Heq             : Tidak / Bukan
# Ulih            : Bisa / Lagi (Coba lagi)
# Tabiq           : Permisi / Maaf (Biasanya untuk akses root/sudo)
# Jakaq           : Silahkan
# Ngara           : Nama / Keterangan
# Meeq            : Ada
# Takaq           : Milik / Punya

# Fungsi Pesan Sukses
tonyooi_kena() {
    echo -e "\n\e[32m[SOOQ]\e[0m ------------------------------------"
    echo -e "Status: \e[1mKena' Beneh!\e[0m (Berhasil)"
    echo -e "Pesan : Perintah soq selesai dijalankan."
    echo -e "\e[32m------------------------------------------\e[0m"
}

# Fungsi Pesan Gagal
tonyooi_heq() {
    echo -e "\n\e[31m[HEQ KENA]\e[0m --------------------------------"
    echo -e "Status: \e[1mHeq Kena'\e[0m (Gagal)"
    echo -e "Pesan : Me-it ara masalah. Ulih ulang jakaq."
    echo -e "\e[31m------------------------------------------\e[0m"
}

# Fungsi untuk Sudo/Root (Tabiq)
tonyooi_tabiq() {
    echo -e "\e[33mTabiq...\e[0m (Permisi, butuh akses admin)"
}

# Logika Utama
if [ -z "$1" ]; then
    echo "--- Tonyooi Linux Wrapper ---"
    echo "Guna: tonyooi [perintah]"
    echo "Contoh: tonyooi lscpu"
    exit 1
fi

# Cek jika perintah membutuhkan sudo (seperti install atau fdisk)
if [[ "$1" == "install" || "$1" == "fdisk" || "$1" == "mount" ]]; then
    tonyooi_tabiq
    
    if [ "$1" == "install" ]; then
        shift # hapus argumen 'install'
        sudo apt update && sudo apt install $@ -y
    else
        sudo $@
    fi
else
    # Jalankan perintah biasa (lscpu, lsblk, dsb)
    $@
fi

# Cek hasil akhir (exit status)
if [ $? -eq 0 ]; then
    tonyooi_kena
else
    tonyooi_heq
fi
