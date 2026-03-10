# Panduan Instalasi 🛠️

Ikuti langkah-langkah di bawah ini untuk memasang modul respon Bahasa Tonyooi di sistem Ubuntu atau Debian Anda.

### Prasyarat
* Sistem operasi berbasis Debian (Ubuntu, Linux Mint, Kali, dll).
* Akses `sudo`.

### Langkah 1: Unduh Skrip
Salin perintah di bawah ini untuk membuat file skrip di direktori home Anda:

```bash
cat << 'EOF' > ~/tonyooi_util.sh
#!/bin/bash
# Tonyooi Language Wrapper

tonyooi_success() {
    echo -e "\e[32m----------------------------------------\e[0m"
    echo -e "\e[32mStatus: SOOQ (Selesai/Sudah)\e[0m"
    echo "Kena beneh! Perintah soq dijalankan."
    echo -e "\e[32m----------------------------------------\e[0m"
}

if [ "$1" == "install" ]; then
    sudo apt update && sudo apt install util-linux -y
    tonyooi_success
elif [ -z "$1" ]; then
    echo "Guna: tonyooi [perintah]"
    echo "Contoh: tonyooi lscpu"
else
    $@
    if [ $? -eq 0 ]; then
        tonyooi_success
    else
        echo -e "\e[31mHeq kena (Gagal). Coba ulih (Coba lagi).\e[0m"
    fi
fi
EOF
