#!/bin/bash

DB_PATH="$HOME/database_tonyooi.db"

# Fungsi mengambil kata dari database
get_tonyooi() {
    grep "$1" "$DB_PATH" | cut -d '|' -f 3 | xargs
}

# Load istilah dari database
T_SUCCESS=$(get_tonyooi "Success")
T_FAILED=$(get_tonyooi "Failed")
T_PROCESS=$(get_tonyooi "Processing")
T_TABIQ=$(get_tonyooi "Permission")
T_ERROR=$(get_tonyooi "Error")

tonyooi_header() {
    echo -e "\e[34m[$T_PROCESS...]\e[0m Memulai alur sistem..."
    sleep 0.5
}

# Eksekusi Perintah
if [ -z "$1" ]; then
    echo "Guna: tonyooi [perintah]"
    exit 1
fi

# Cek Sudo
if [[ "$1" == "sudo" || "$1" == "apt" || "$1" == "fdisk" ]]; then
    echo -e "\e[33m$T_TABIQ...\e[0m (Meminta izin akses)"
fi

tonyooi_header
$@

# Cek Status Akhir
if [ $? -eq 0 ]; then
    echo -e "\n\e[32m------------------------------------------"
    echo -e "STATUS: $T_SUCCESS"
    echo -e "PESAN : Perintah soq selesai (Done)."
    echo -e "------------------------------------------\e[0m"
else
    echo -e "\n\e[31m------------------------------------------"
    echo -e "STATUS: $T_FAILED"
    echo -e "PESAN : $T_ERROR (Periksa kembali)."
    echo -e "------------------------------------------\e[0m"
fi


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
