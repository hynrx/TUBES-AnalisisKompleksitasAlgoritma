# Analisis Kompleksitas Algoritma: FPB Iteratif vs Rekursif

Program ini adalah aplikasi visualisasi interaktif berbasis **Python** dan **Streamlit** untuk membandingkan performa (*running time*) antara algoritma **Euclidean Iteratif** dan **Euclidean Rekursif** dalam mencari Faktor Persekutuan Terbesar (FPB).

Aplikasi ini menguji kedua algoritma menggunakan sekumpulan data acak (*random integers*) dengan ukuran input yang dapat dikonfigurasi secara dinamis oleh pengguna untuk melihat tren efisiensi waktu.

## 👥 Anggota Kelompok

| Nama | NIM |
| :--- | :--- |
| **Hisyam Nurdiatmoko** | 103112400049 |
| **Mohammad Reyhan Aretha Fatin** | 103112400078 |
| **Muhammad Faris Rachmadi** | 103112400079 |

---

## 🔍 Algoritma yang Dianalisis

### 1. Euclidean Iteratif
Menggunakan pendekatan perulangan (`while loop`) untuk mencari sisa bagi hingga mencapai 0.
* **Karakteristik:** Efisien memori, stabil, dan tidak menambah tumpukan pemanggilan fungsi (*call stack*).
* **Kompleksitas Waktu:** $O(\log(\min(a, b)))$
* **Implementasi Python:**
    ```python
    while b != 0:
        a, b = b, a % b
    return a
    ```

### 2. Euclidean Rekursif
Menggunakan pendekatan pemanggilan fungsi diri sendiri (*self-reference*).
* **Karakteristik:** Kode lebih ringkas, namun memiliki *overhead* memori untuk manajemen *stack frames*.
* **Catatan Teknis:** Program ini mengatur `sys.setrecursionlimit(20000)` untuk menangani input besar tanpa *crash*.
* **Kompleksitas Waktu:** $O(\log(\min(a, b)))$
* **Implementasi Python:**
    ```python
    if b == 0: return a
    return fpb_rekursif(b, a % b)
    ```

---

## 🚀 Fitur Unggulan

### 1. Pengaturan Input Dinamis (Sidebar)
Pengguna memiliki kontrol penuh terhadap parameter pengujian melalui sidebar:
* **Maksimal Jumlah Data:** Menentukan batas atas jumlah pasangan angka yang akan diuji (contoh: 5000 pasang).
* **Kelipatan (Step):** Menentukan interval kenaikan jumlah data (contoh: diuji setiap kelipatan 500).
* **Besar Angka (Range):** Menentukan batas nilai acak yang dibangkitkan (contoh: angka antara 1 s.d. 100.000).

### 2. Visualisasi Real-Time
* **Progress Bar:** Menampilkan status jalannya pengujian secara visual.
* **Grafik Line Chart:** Memvisualisasikan perbandingan waktu eksekusi (Iteratif vs Rekursif) seiring bertambahnya ukuran input.
* **Tabel Data:** Menyajikan data mentah waktu eksekusi secara mendetail dalam format tabel.

### 3. Analisis Otomatis
Program secara otomatis menghitung total waktu eksekusi dari seluruh pengujian dan memberikan kesimpulan:
* Menampilkan total akumulasi waktu (detik).
* Memberikan "Winner" (pemenang) antara metode Iteratif atau Rekursif berdasarkan total waktu tercepat.

---

## 🛠️ Cara Instalasi dan Menjalankan

Pastikan sudah menginstal **Python**. Buka terminal/CMD dan jalankan perintah berikut:

```pip install streamlit pandas matplotlib```

```python -m streamlit run aka.py```
