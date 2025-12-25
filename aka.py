import streamlit as st
import time
import random
import pandas as pd
import sys

sys.setrecursionlimit(20000)

st.title("Perbandingan FPB")
st.write("Studi Kasus: Perbandingan Algoritma Euclidean Iteratif vs Rekursif")
st.write("Anggota Kelompok:")
st.write("Hisyam Nurdiatmoko | 103112400049")
st.write("Mohammad Reyhan Aretha Fatin | 103112400078")
st.write("Muhammad Faris Rachmadi | 103112400079")

# Algoritma Iteratif
def fpb_iteratif(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Algoritma Rekursif
def fpb_rekursif(a, b):
    if b == 0:
        return a
    else:
        return fpb_rekursif(b, a % b)


# Input user (sidebar)
st.sidebar.header("Pengaturan Test")

jumlah_maks = st.sidebar.number_input("Maksimal Jumlah Data", value=5000, step=100)
step = st.sidebar.number_input("Kelipatan (Step)", value=500, step=100)
range_angka = st.sidebar.slider("Besar Angka", 100, 100000, 10000)
tombol = st.sidebar.button("Mulai Analisis")

# PROSES PERBANDINGAN
if tombol:
    hasil_ukuran = []
    waktu_iteratif = []
    waktu_rekursif = []
    
    st.write("Loadinggg...")
    bar_progress = st.progress(0)

    list_ukuran = range(step, jumlah_maks + 1, step)
    total_loop = len(list_ukuran)

    for i, n in enumerate(list_ukuran):
        data_test = []
        for _ in range(n):
            angka1 = random.randint(1, range_angka)
            angka2 = random.randint(1, range_angka)
            data_test.append((angka1, angka2))
        
        # Cek Waktu Iteratif
        start = time.time()
        for a, b in data_test:
            fpb_iteratif(a, b)
        end = time.time()
        waktu_iteratif.append(end - start)

        # Cek Waktu Rekursif
        start = time.time()
        for a, b in data_test:
            fpb_rekursif(a, b)
        end = time.time()
        waktu_rekursif.append(end - start)

        hasil_ukuran.append(n)
        
        bar_progress.progress((i + 1) / total_loop)

# HASIL
    # DataFrame grafik
    df = pd.DataFrame({
        'Ukuran Input': hasil_ukuran,
        'Iteratif': waktu_iteratif,
        'Rekursif': waktu_rekursif
    })

    df = df.set_index('Ukuran Input')

    st.success("Selesai dengan hasil:")

    # Grafik Running Time
    st.subheader("1. Grafik Perbandingan Waktu")
    st.line_chart(df)
    st.caption("Sumbu X = Jumlah Data, Sumbu Y = Waktu (detik)")

    # Tabel Data
    st.subheader("2. Tabel Detail Data")
    st.dataframe(df)

    # Analisis Singkat
    st.subheader("3. Kesimpulan Sementara")
    
    total_iter = sum(waktu_iteratif)
    total_rekur = sum(waktu_rekursif)

    st.write(f"Total waktu Iteratif: **{total_iter:.4f} detik**")
    st.write(f"Total waktu Rekursif: **{total_rekur:.4f} detik**")

    if total_iter < total_rekur:
        st.info("Hasil: Algoritma **Iteratif** lebih cepat secara keseluruhan.")
    else:
        st.info("Hasil: Algoritma **Rekursif** lebih cepat secara keseluruhan.")
    
    st.write("""
    **Analisis:**
    Meskipun kompleksitas teoritisnya sama-sama Logaritmik, biasanya Iteratif lebih cepat di Python
    karena tidak ada overhead memori untuk pemanggilan fungsi (stack) yang terjadi di Rekursif.
    """)
