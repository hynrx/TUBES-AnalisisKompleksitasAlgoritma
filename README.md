# Analisis Kompleksitas Algoritma: FPB Iteratif vs Rekursif

Program ini adalah aplikasi visualisasi berbasis **Python** dan **Streamlit** yang dirancang untuk membandingkan performa (running time) antara algoritma **Euclidean Iteratif** dan **Euclidean Rekursif** dalam mencari Faktor Persekutuan Terbesar (FPB).

Tujuan utama program ini adalah untuk menganalisis efisiensi waktu eksekusi kedua algoritma ketika dihadapkan pada volume data yang besar.

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
* **Karakteristik:** Efisien memori karena tidak menambah tumpukan pemanggilan fungsi (*call stack*).
* **Implementasi Python:**
    ```python
    while b != 0:
        a, b = b, a % b
    return a
    ```

### 2. Euclidean Rekursif
Menggunakan pendekatan pemanggilan fungsi diri sendiri (*self-reference*).
* **Karakteristik:** Kode lebih ringkas dan matematis, namun memiliki *overhead* waktu dan memori untuk manajemen stack.
* **Implementasi Python:**
    ```python
    if b == 0: return a
    else: return fpb_rekursif(b, a % b)
    ```

---

## 🚀 Fitur Aplikasi

1.  **Pengaturan Dinamis (Sidebar):**
    * User dapat mengatur jumlah data maksimal (input size).
    * User dapat mengatur *step* (kelipatan data).
    * User dapat mengatur range besaran angka random yang diuji.
2.  **Visualisasi Grafik:**
    * Menampilkan *Line Chart* perbandingan waktu eksekusi (Sumbu X: Ukuran Input, Sumbu Y: Waktu).
3.  **Data Table:**
    * Menampilkan data mentah hasil pengujian dalam bentuk tabel Pandas.
4.  **Kesimpulan Otomatis:**
    * Sistem secara otomatis menghitung total waktu dan menentukan algoritma mana yang lebih cepat berdasarkan data real-time.

---

## 🛠️ Cara Instalasi dan Menjalankan

Pastikan sudah menginstal **Python**.

### 1. Instalasi Library
Buka terminal/CMD dan jalankan perintah berikut untuk menginstal dependensi yang dibutuhkan:

```pip install streamlit pandas matplotlib```

```python -m streamlit run aka.py```
