# Analisis Sentimen Ulasan Aplikasi Tokopedia di Google Play Store

## Deskripsi Proyek

Proyek ini bertujuan untuk melakukan analisis sentimen terhadap ulasan (reviews) pengguna aplikasi Tokopedia yang dipublikasikan di Google Play Store. Proses dimulai dari pengumpulan data ulasan secara otomatis (scraping), pemrosesan teks (text preprocessing), hingga membangun model machine learning untuk mengklasifikasikan sentimen ke dalam tiga kategori: **Positif**, **Negatif**, dan **Netral**.

## Fitur Utama

-   **Scraping Data**: Mengambil data ulasan aplikasi langsung dari Google Play Store menggunakan `google-play-scraper`.
-   **Preprocessing Teks**: Membersihkan dan mempersiapkan data teks ulasan melalui beberapa tahapan:
    -   Case Folding (mengubah teks menjadi huruf kecil).
    -   Pembersihan dari karakter yang tidak perlu.
    -   Normalisasi kata (memperbaiki kata slang).
    -   Stopword Removal (menghapus kata-kata umum).
    -   Tokenisasi.
-   **Pelatihan Model**: Membangun dan melatih model deep learning (kemungkinan menggunakan LSTM atau arsitektur sejenis dengan TensorFlow/Keras) untuk klasifikasi sentimen.
-   **Prediksi Sentimen**: Menggunakan model yang telah dilatih untuk memprediksi sentimen dari kalimat atau ulasan baru.

## Alur Kerja Proyek

1.  **Pengumpulan Data**: Menjalankan script `scrape_playstore.py` untuk mengunduh ulasan dari Google Play Store dan menyimpannya dalam format file `.csv`.
2.  **Analisis dan Pemodelan**: Membuka dan menjalankan notebook `sentiment_analysis_tokopedia.ipynb` untuk melakukan pemrosesan data, melatih model, dan menguji prediksi.

## Teknologi yang Digunakan

-   **Python**: Bahasa pemrograman utama.
-   **google-play-scraper**: Untuk mengambil data ulasan dari Google Play Store.
-   **Pandas**: Untuk manipulasi dan analisis data.
-   **NLTK**: Untuk pemrosesan bahasa alami (preprocessing teks).
-   **TensorFlow & Keras**: Untuk membangun dan melatih model deep learning.
-   **Scikit-learn**: Untuk membagi data (train-test split).
-   **Jupyter Notebook**: Untuk analisis interaktif dan dokumentasi.

## Instalasi

Untuk menjalankan proyek ini, ikuti langkah-langkah berikut:

1.  **Clone repositori ini:**
    ```bash
    git clone <URL_REPOSITORI_ANDA>
    cd <NAMA_FOLDER_PROYEK>
    ```

2.  **Buat dan aktifkan virtual environment (direkomendasikan):**
    ```bash
    # Untuk pengguna Windows
    python -m venv venv
    venv\Scripts\activate

    # Untuk pengguna macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instal semua dependensi yang dibutuhkan:**
    ```bash
    pip install pandas google-play-scraper tensorflow nltk scikit-learn jupyter
    ```

4.  **Unduh data NLTK yang diperlukan.** Buka terminal Python atau buat script singkat dan jalankan kode berikut:
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    ```

## Cara Penggunaan

### Langkah 1: Scraping Data Ulasan

Jalankan script `scrape_playstore.py` dari terminal untuk mulai mengumpulkan data.

```bash
python scrape_playstore.py
```

- Script ini akan mengunduh 150.000 ulasan terbaru dari aplikasi Tokopedia (com.tokopedia.tkpd).
- Hasilnya akan disimpan dalam file tokopedia_reviews.csv.
- Anda dapat mengubah ID aplikasi atau jumlah ulasan di dalam file scrape_playstore.py jika diperlukan.

### Langkah 2: Analisis Sentimen dan Pelatihan Model
Pastikan Anda sudah memiliki file tokopedia_reviews.csv dari langkah sebelumnya.

Buka dan jalankan Jupyter Notebook:
```bash
jupyter notebook
```

Dari browser, buka file sentiment_analysis_tokopedia.ipynb.
Jalankan setiap sel di dalam notebook secara berurutan untuk:
- Memuat dan membersihkan data.
- Melakukan preprocessing teks.
- Membagi dataset.
- Melatih model klasifikasi sentimen.
- Mengevaluasi performa model.
- Menguji model dengan kalimat baru.


## Struktur Proyek
```
.
├── scrape_playstore.py           # Script untuk scraping data ulasan
├── sentiment_analysis_tokopedia.ipynb # Notebook untuk analisis dan pemodelan
├── tokopedia_reviews.csv         # File data (dihasilkan setelah menjalankan scraper)
└── README.md                     # File dokumentasi ini
```
