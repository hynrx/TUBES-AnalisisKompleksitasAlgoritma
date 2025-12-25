import streamlit as st
import time
import random
import pandas as pd
import sys

sys.setrecursionlimit(20000)
st.set_page_config(page_title="Analisis FPB", layout="wide")

# DEFINISI ALGORITMA & FUNGSI BANTUAN
def fpb_iteratif(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def fpb_rekursif(a, b):
    if b == 0: return a
    return fpb_rekursif(b, a % b)

def get_fibonacci(limit):
    """Membuat list Fibonacci sampai batas limit untuk skenario Worst Case"""
    fibs = [1, 1]
    while (next_val := fibs[-1] + fibs[-2]) <= limit:
        fibs.append(next_val)
    return fibs

st.title("Analisis Kompleksitas FPB Euclidean")

# ANGGOTA KELOMPOK
st.markdown("""
**Anggota Kelompok:**
* **Hisyam Nurdiatmoko** | 103112400049
* **Mohammad Reyhan Aretha Fatin** | 103112400078
* **Muhammad Faris Rachmadi** | 103112400079
""")

st.sidebar.header("Pengaturan")
skenario = st.sidebar.radio("Skenario Uji:", ["Average Case (Random)", "Worst Case (Fibonacci)", "Best Case (Kelipatan)"])
max_data = st.sidebar.number_input("Total Data", value=5000, step=500)
step = st.sidebar.number_input("Kelipatan Data", value=500, step=500)
limit_angka = st.sidebar.slider("Besar Angka", 100, 100000, 10000)

# LOGIKA PENGUJIAN
if st.sidebar.button("Mulai Analisis"):
    results = []
    fib_pool = get_fibonacci(limit_angka) if "Fibonacci" in skenario else []
    with st.spinner("Sedang memproses algoritma..."):
        
        for n in range(step, max_data + 1, step):
            dataset = []

            for _ in range(n):
                if "Fibonacci" in skenario:
                    idx = random.randint(2, len(fib_pool) - 1)
                    dataset.append((fib_pool[idx], fib_pool[idx-1]))
                elif "Kelipatan" in skenario:
                    b = random.randint(1, limit_angka // 5)
                    dataset.append((b * random.randint(2, 5), b))
                else:
                    dataset.append((random.randint(1, limit_angka), random.randint(1, limit_angka)))
            
            #Hitung Waktu Iteratif
            t0 = time.time()
            for a, b in dataset: fpb_iteratif(a, b)
            t_iter = time.time() - t0
            
            #Hitung Waktu Rekursif
            try:
                t0 = time.time()
                for a, b in dataset: fpb_rekursif(a, b)
                t_rekur = time.time() - t0
            except RecursionError:
                t_rekur = None
            
            results.append({"Ukuran Data": n, "Iteratif (s)": t_iter, "Rekursif (s)": t_rekur})

    # VISUALISASI HASIL
    # Membuat DataFrame 
    df = pd.DataFrame(results).set_index("Ukuran Data")
    
    # A. GRAFIK LINE CHART
    st.markdown("---")
    st.subheader("📈 Grafik Perbandingan Waktu Eksekusi")
    st.line_chart(df)
    
    # B. TABEL DATA
    st.subheader("📋 Tabel Data Hasil")
    st.dataframe(df, use_container_width=True)

    # METRIK & KESIMPULAN
    # perhitungan rata rata
    avg_iter = df["Iteratif (s)"].mean()
    # handle jika rekursif error
    if df["Rekursif (s)"].isnull().any():
        avg_rekur = 0
        selisih = 0
    else:
        avg_rekur = df["Rekursif (s)"].mean()
        selisih = avg_rekur - avg_iter
    
    st.markdown("---")
    st.subheader("⏱️ Perbandingan Rata-rata Waktu")
    
    # tampiolan metric
    col1, col2, col3 = st.columns(3)
    col1.metric("Rata-rata Iteratif", f"{avg_iter:.6f} s")
    col2.metric("Rata-rata Rekursif", f"{avg_rekur:.6f} s")
    if avg_rekur > 0:
        col3.metric("Selisih", f"{selisih:.6f} s", delta_color="inverse")
    else:
        col3.metric("Selisih", "Error (Stack Overflow)", delta_color="off")
    # kesimpulan sementara
    st.subheader("Kesimpulan")
    
    if "Fibonacci" in skenario:
        st.warning(f"**Hasil: Rekursif Lebih Lambat (Worst Case).**\nDeret Fibonacci memaksa algoritma bekerja maksimal. Rekursif terbebani oleh manajemen memori (stack), sedangkan Iteratif tetap stabil dan efisien.")
    elif "Kelipatan" in skenario:
        st.success(f"**Hasil: Seimbang (Best Case).**\nAlgoritma selesai hanya dalam 1-2 langkah. Perbedaan waktu sangat kecil (mendekati 0 detik) sehingga kedua metode sama efektifnya.")
    else:
        st.info(f"**Hasil: Iteratif Sedikit Unggul (Average Case).**\nPada data acak, Iteratif menang tipis. Python mengeksekusi *looping* (while) lebih cepat daripada pemanggilan fungsi berulang (rekursi).")
