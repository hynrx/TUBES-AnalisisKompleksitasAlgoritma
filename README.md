# Analisis Kompleksitas Algoritma: FPB Iteratif vs Rekursif

Program ini adalah aplikasi visualisasi interaktif berbasis **Python** dan **Streamlit** untuk membandingkan performa (*running time*) antara algoritma **Euclidean Iteratif** dan **Euclidean Rekursif** dalam mencari Faktor Persekutuan Terbesar (FPB).

Aplikasi ini dirancang khusus untuk menganalisis perilaku algoritma pada tiga kondisi: **Best Case**, **Average Case**, dan **Worst Case**.

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
* **Karakteristik:** Kode lebih ringkas, namun memiliki *overhead* memori untuk manajemen *stack frames*. Rentan terhadap *Stack Overflow* pada input yang sangat ekstrim.
* **Kompleksitas Waktu:** $O(\log(\min(a, b)))$
* **Implementasi Python:**
    ```python
    if b == 0: return a
    return fpb_rekursif(b, a % b)
    ```

---

## 🚀 Fitur Unggulan

### 1. Skenario Pengujian (Test Cases)
Program ini mendukung 3 skenario uji untuk analisis mendalam:
* **Average Case (Random):** Input berupa angka acak. Menggambarkan penggunaan sehari-hari.
* **Worst Case (Fibonacci):** Input berupa deret Fibonacci berurutan. Memaksa algoritma melakukan langkah pembagian terbanyak (berdasarkan Teorema Lamé).
* **Best Case (Kelipatan):** Input dimana angka satu adalah kelipatan angka lainnya. Algoritma selesai dalam 1-2 langkah modulus.

### 2. Visualisasi & Data
* **Grafik Line Chart:** Membandingkan tren kenaikan waktu seiring bertambahnya jumlah data.
* **Tabel Data:** Menampilkan detail hasil waktu iteratif vs rekursif untuk setiap ukuran data.
* **Presisi Tinggi:** Pengukuran waktu ditampilkan hingga **6 angka di belakang koma** (mikro-detik) untuk akurasi maksimal.

### 3. Analisis Dinamis
* Menampilkan metrik rata-rata waktu dan selisih performa.
* Memberikan kesimpulan otomatis dan penjelasan teknis berdasarkan skenario yang sedang dijalankan.

---

## 🛠️ Cara Instalasi dan Menjalankan

Pastikan sudah menginstal **Python**.

### 1. Instalasi Library
Buka terminal/CMD dan jalankan perintah berikut untuk menginstal dependensi yang dibutuhkan:

```pip install streamlit pandas matplotlib```

```python -m streamlit run aka.py```
