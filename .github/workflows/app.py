from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)
DB_NAME = "kamus_tunjung.db"

def init_db():
    """Membuat database, tabel, dan memasukkan seluruh data kamus jika belum ada."""
    conn = sqlite3.connect(DB_NAME)
    try:
        cursor = conn.cursor()

        # 1. Membuat tabel kamus
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS kamus_tunjung (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tunjung TEXT NOT NULL,
                indonesia TEXT NOT NULL
            )
        """)

        # Cek apakah tabel sudah berisi data
        cursor.execute("SELECT COUNT(*) FROM kamus_tunjung")
        if cursor.fetchone()[0] == 0:
            # Seluruh data gabungan (Umum, Kerja, Sifat, Panggilan, Programmer)
            all_words = [
            # Kata Umum
            ('Ampaap', 'Cahaya, sinar, terang'), ('Amput', 'Ikut, mengikuti'), ('Ampiitn', 'Alas'),
            ('Ampuun', 'Bersama dengan'), ('Ancar', 'Tari'), ('Ancaatn', 'Guna-guna, pelet'),
            ('Anci', 'Tusuk'), ('Ancur', 'Moncong'), ('Angka', 'Kira-kira, mungkin'),
            ('Angkai', 'Bangkai'), ('Angkuui', 'Rendah hati'), ('Antaakng', 'Guci besar'),
            ('Antaaq', 'Banyak'), ('Antakng', 'Akan, hendak'), ('Anteek', 'Sebabnya'),
            ('Antung', 'Arah, letak, alamat'), ('Aur', 'Sibuk'), ('Bancukng', 'Bensin'),
            ('Bangkukng', 'Bagian atas dari moncong hewan'), ('Bantir', 'Masa akil balik'),
            ('Bantuut', 'Tidak meledak/meletus'), ('Baon', 'Bau, aroma'), ('Baoq', 'Bau, aroma'),
            ('Begontekng', 'Bergantung'), ('Beldookng', 'Parang'), ('Belempai', 'Tidak memakai baju'),
            ('Belengkenat', 'Makanan yang tersangkut di leher'), ('Belengkoot', 'Bengkok'),
            ('Beluntakng', 'Tiang (patung) untuk mengikat hewan kurban'), ('Beniaq', 'Burung elang'),
            ('Benua', 'Kampung'), ('Beor', 'Nama jenis cendawan/jamur'),
            ('Bepempaapm', 'Menutup kemaluan dengan telapak atau jari tangan'), ('Berdoeeq', 'Rapuh (tentang tubuh)'),
            ('Berempai', 'Jalan berduaan'), ('Berempuh', 'Saling berangkulan'), ('Bersinak', 'Beracun'),
            ('Bintakng', 'Bintang'), ('Bion', 'Daging yang masih segar'), ('Bioh', 'Baru saja'),
            ('Bloak', 'Jenis seni suara'), ('Buak', 'Burung hantu'), ('Bueh', 'Satu, tunggal'),
            ('Buncaarbaih', 'Berserakan'), ('Buo', 'Hujan terus-menerus'),
            ('Buookng', 'Menyebutkan atau menanyakan berulang kali'), ('Caor', 'Jenis sarung (untuk perempuan)'),
            ('Cecuaq', 'Gagap'), ('Coang', 'Baskom'), ('Coeq', 'Cobek'),
            ('Dian', 'Kain yang dipilin dan dilumuri lilin madu untuk ritual belian'), ('Diapm', 'Tinggal'),
            ('Encuutn', 'Asap'), ('Encoq', 'Jauh'), ('Engkolakng', 'Tempat berteduh'),
            ('Gae', 'Miliknya'), ('Gaer', 'Khawatir, cemas'), ('Galikngganai', 'Tidur-tiduran'),
            ('Gei siih', 'Jenis rotan'), ('Goar-goer', 'Longgar'), ('Huit', 'Belantik'),
            ('Iatn', 'Sungai'), ('Incuk', 'Tukul'), ('Jait', 'Hampir'), ('Jaut', 'Kabur'),
            ('Jautn', 'Awan'), ('Jemiaq', 'Rumbia'), ('Jie', 'Sejenis guci'),
            ('Juakng', 'Bunga yang dipakai dalam upacara belian'), ('Kae', 'Memang'), ('Kaeet', 'Selalu, biasa'),
            ('Kao', 'Mencuci muka'), ('Kaot', 'Sendok, gayung'), ('Kauuk', 'Jenis kadal yang besar'),
            ('Kear-keor', 'Bergoyang-goyang'), ('Keak-keok', 'Berbelok-belok'), ('Keaskeko', 'Sudah dikerjakan'),
            ('Kekuit', 'Terangkat pada salah satu ujung'), ('Kelikau-kiiu', 'Tidak karuan'), ('Kelikiu', 'Sayap'),
            ('Kelio', 'Pergi menengok ladang'), ('Keliuq', 'Keracunan'), ('Kelauq', 'Jenis buah asam hutan'),
            ('Kelengkikng', 'Lumbung padi'), ('Keluatn', 'Tertimpa'), ('Kerkak', 'Ketiak'),
            ('Kertak', 'Kacang panjang'), ('Kertikng', 'Kering, garing, renyah'), ('Kerwilik', 'Kincir angin'),
            ('Kias', 'Sapu'), ('Kiriu', 'Pinggir'), ('Koih', 'Gesit, rajin'), ('Koreu', 'Musim kemarau berkepanjangan'),
            ('Kuini', 'Nama jenis mangga'), ('Lahtala', 'Yang Maha Esa'), ('Laih', 'Ikan lais'),
            ('Laitn', 'Lain'), ('Laoq', 'Lapar'), ('Lea', 'Bosan'), ('Leeot', 'Jalan panjang'),
            ('Lehuatn', 'Bagian depan'), ('Leler-maer', 'Tak terurus, berantakan'), ('Leoq', 'Sperma'),
            ('Leoon', 'Sperma'), ('Lesoer', 'Menjuntai ke bawah'), ('Loah', 'Mual'), ('Loaaq', 'Lemak'),
            ('Loakng', 'Lubang tugalan'), ('Loan', 'Lemak'), ('Longeeu', 'Menjulang tinggi'),
            ('Loseeu', 'Melebihi batas'), ('Luuok', 'Lubang'), ('Mancak', 'Bisul'), ('Mangkasi', 'Rendah hati'),
            ('Meat', 'Menindih'), ('Meluikng', 'Nama jenis tumbuhan yang bisa dimakan'), ('Mengeliu', 'Melengking'),
            ('Mengeook', 'Keok'), ('Mengoek', 'Suara babi berteriak'), ('Mensigit', 'Masjid'),
            ('Mentiuuq', 'Bunuh diri'), ('Mentaih', 'Susah, sengsara, menderita'), ('Menyelingkui', 'Mengikuti dari belakang'),
            ('Meraiq', 'Melerai'), ('Mio', 'Sadar, siuman'), ('Mioh', 'Menyatukan yang berserakan'),
            ('Neaau', 'Melihat'), ('Nerka', 'Terka'), ('Nerdas', 'Mematikan di tempatnya'),
            ('Nerdaatn', 'Berterus terang'), ('Ngeaak', 'Membuka'), ('Ngenjijiq', 'Menyengir'),
            ('Ngerkokng', 'Berjongkok'), ('Ngeteu', 'Mencelupkan'),
            ('Ngueu', 'Memberi isyarat dengan tangan agar orang lain pergi atau minggir'), ('Nguih', 'Menghajar'),
            ('Nguit', 'Mengungkit, menjungkit'), ('Ngureeu', 'Menggerakkan'),
            ('Nguseu', 'Menghamburkan air keluar dari dalam wadahnya'),
            ('Nguweu', 'Menggerakkan tangan atau galah, dan lain-lain pertanda agar menjauh'),
            ('Pelgaq mai', 'Leluhur'), ('Pemkaar', 'Orang yang berjasa dalam sejarah dan pengembangan kampung'),
            ('Pengampeh', 'Alat pemeras tebu'), ('Perdah', 'Tangkai beliung'), ('Permaq', 'Hitam'),
            ('Perngaaq', 'Pembagian tugas atau pekerjaan'), ('Pucoou', 'Mencelupkan'),
            ('Rakbaar', 'Adat terkait pelanggaran dalam upacara belian atau kematian'), ('Sangkur', 'Cangkul'),
            ('Seloar', 'Celana'), ('Serbanaaq', 'Memberikan nasihat kepada anak kandung/keluarga dekat sebelum meninggal'),
            ('Serkap', 'Alat penangkap ikan di danau yang dangkal'), ('Sermiq', 'Emper'),
            ('Setrongkeng', 'Lampu pompa angin'), ('Tengemperek', 'Diomeli'), ('Terjooq', 'Telanjur'),
            ('Uok', 'Nasi yang bercampur dengan sayur (berkuah)'),
            
            # Kata Kerja
            ('Aur', 'Sibuk'), ('Mulaaq', 'Mulai, memulai'), ('Ngebaak', 'Membuka (pintu, jendela, atau halaman buku)'),
            ('Nginaatn', 'Melihat, menengok, memperhatikan'), ('Katiiq', 'Tertawa'), ('Nangih', 'Menangis'),
            ('Tidur', 'Baring, tidur'), ('Kuman', 'Makan'), ('Mirooq', 'Minum'), ('Bejalan', 'Berjalan'),
            ('Belari', 'Berlari'), ('Nungkat', 'Memanjat'), ('Tepatiiq', 'Melompat'), ('Nulis', 'Menulis'),
            ('Maca', 'Membaca'), ('Ndingit', 'Mendengar'), ('Tulah', 'Membantu, menolong'), ('Ngarat', 'Memotong'),
            ('Nyulaq', 'Menanam'), ('Muat', 'Membuat'), ('Ngeju', 'Memberi'), ('Nyambut', 'Menerima'),
            ('Betiup', 'Bicara, berbicara'), ('Nyangkut', 'Membawa'), ('Guring', 'Baring, merebahkan diri'),
            ('Tekaatn', 'Datang, tiba'),
            
            # Kata Sifat
            ('Mulaat', 'Ganteng, tampan'), ('Amooq', 'Cantik'), ('Gulaat', 'Manis'), ('Pait', 'Pahit'),
            ('Sireet', 'Asin'), ('Kelauu', 'Asam'), ('Legeeu', 'Hambar, tawar'), ('Poat', 'Panas'),
            ('Gereem', 'Dingin'), ('Rayat', 'Besar'), ('Ikiit', 'Kecil'), ('Leeot', 'Panjang'),
            ('Bakaat', 'Pendek'), ('Longeeu', 'Tinggi'), ('Angkuui', 'Rendah, rendah hati'), ('Mooq', 'Jauh'),
            ('Dapeet', 'Dekat'), ('Mioh', 'Bersih'), ('Latak', 'Kotor'), ('Koih', 'Rajin, gesit'),
            ('Pegaale', 'Malas'), ('Gaer', 'Takut, khawatir'), ('Basiit', 'Berani'), ('Gegaat', 'Keras'),
            ('Lomeet', 'Lembut, empuk'), ('Akaat', 'Cepat'), ('Lekeet', 'Lambat'),
            
            # Kata Panggilan
            ('Akuq', 'Akuq, saya'), ('Koq', 'Kamu, engkau'), ('Iye', 'Dia (laki-laki / perempuan)'),
            ('Kamiq', 'Kami'), ('Keti', 'Kalian'), ('Ere', 'Mereka'), ('Uooq', 'Orang'),
            ('Uooq rayat', 'Orang tua'), ('Uooq ikiit', 'Anak-anak'), ('Amai', 'Ayah, bapak'),
            ('Inaq', 'Ibu, mama'), ('Akaq', 'Kakak'), ('Atak', 'Adik'), ('Teteek', 'Kakek'),
            ('Nenek', 'Nenek'), ('Aqaq', 'Paman'), ('Ibuq', 'Bibi'), ('Epot', 'Cucu'),
            ('Kula', 'Keluarga, kerabat'), ('Sawa', 'Suami'), ('Sungen', 'Istri'),
            
            # Kata Programmer
            ('Petamaq', 'Programmer, pengembang perangkat lunak'), ('Ngaq Bajiq', 'Sintaksis, aturan kode'),
            ('pemikir', 'Algoritma'), ('Anyant', 'Basis data, database'), ('Tulisan kode', 'Kode sumber, source code'),
            ('Alat penata tampilan', 'Framework frontend'), ('Mesin pengolah data', 'Framework backend'),
            ('Penyaring kesalahan', 'Debugging, pelacakan bug'), ('Penghubung sistem', 'API (Application Programming Interface)'),
            ('Alat bantu otomatis', 'Kecerdasan buatan, AI copilot'), ('Rumah kode', 'Repositori, Git storage')
        ]
        
            cursor.executemany("INSERT INTO kamus_tunjung (tunjung, indonesia) VALUES (?, ?)", all_words)
            conn.commit()
            print("Database berhasil diinisialisasi dengan data lengkap.")
    finally:
        conn.close()


@app.route('/')
def home():
    """Menampilkan halaman utama kamus (Interface HTML)"""
    return render_template('index.html')

@app.route('/translate')
def translate():
    """
    Endpoint Terjemahan.
    Query parameters:
    - text: Teks kata yang ingin dicari
    - mode: 'tunj_to_id' (default) atau 'id_to_tunj'
    """
    search_text = request.args.get('text', '').strip()
    mode = request.args.get('mode', 'tunj_to_id')
    
    if not search_text:
        return jsonify({"status": "error", "message": "Parameter 'text' tidak boleh kosong."}), 400

    conn = sqlite3.connect(DB_NAME)
    try:
        cursor = conn.cursor()

        if mode == 'tunj_to_id':
            # Menggunakan LIKE agar pencarian fleksibel, atau bisa disesuaikan jadi '=' untuk pencarian pas
            cursor.execute(
                "SELECT tunjung, indonesia FROM kamus_tunjung WHERE LOWER(tunjung) LIKE LOWER(?)", 
                (f"%{search_text}%",)
            )
        elif mode == 'id_to_tunj':
            cursor.execute(
                "SELECT tunjung, indonesia FROM kamus_tunjung WHERE LOWER(indonesia) LIKE LOWER(?)", 
                (f"%{search_text}%",)
            )
        else:
            return jsonify({"status": "error", "message": "Mode tidak valid. Gunakan 'tunj_to_id' atau 'id_to_tunj'."}), 400

        rows = cursor.fetchall()
    finally:
        conn.close()

    if not rows:
        return jsonify({
            "status": "success",
            "results_count": 0,
            "message": "Kata tidak ditemukan dalam kamus.",
            "data": []
        }), 200 # Atau 200 dengan list kosong

    # Membuat response json terstruktur
    results = [{"tunjung": row[0], "indonesia": row[1]} for row in rows]
    
    return jsonify({
        "status": "success",
        "search_query": search_text,
        "mode": mode,
        "results_count": len(results),
        "data": results
    }), 200

if __name__ == '__main__':
    init_db()
    # Jalankan aplikasi pada lokal localhost:5000
    app.run(debug=True, port=5000)
