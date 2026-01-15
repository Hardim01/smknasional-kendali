import streamlit as st
import pandas as pd

# Konfigurasi Halaman (Agar bagus di HP)
st.set_page_config(page_title="RUAS STUDIO - Dashboard", layout="centered")

# Header dengan Logo (Simulasi)
st.title("🛡️ RUAS STUDiO")
st.subheader("Sistem Kendali Internal Sekolah")
st.markdown("---")

# Ringkasan Angka (Widget Metric)
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Total Dana BOS", value="Rp 125.000.000", delta="+ 5.400.000")
with col2:
    st.metric(label="Pengeluaran Bulan Ini", value="Rp 12.500.000", delta="- 200.000", delta_color="inverse")

st.markdown("---")

# Menu Input Sederhana
st.write("### 📝 Input Laporan Cepat")
nama_staff = st.text_input("Nama Staff/Pelapor")
kegiatan = st.selectbox("Jenis Kegiatan", ["Operasional", "Gaji/Honor", "Sarpras", "Lainnya"])
jumlah = st.number_input("Jumlah Anggaran (Rp)", min_value=0)

if st.button("Kirim Laporan"):
    if nama_staff:
        st.success(f"Laporan {kegiatan} dari {nama_staff} berhasil dikirim ke Kepala Sekolah!")
    else:
        st.warning("Mohon isi nama pelapor.")

# Tabel Pemantauan
st.markdown("---")
st.write("### 📊 Status Anggaran Terkini")
data = {
    "Unit Kerja": ["Sarpras", "Kurikulum", "Kesiswaan", "Humas"],
    "Terserap": ["Rp 45jt", "Rp 20jt", "Rp 15jt", "Rp 10jt"],
    "Sisa": ["Rp 5jt", "Rp 10jt", "Rp 5jt", "Rp 5jt"]
}
df = pd.DataFrame(data)
st.table(df)

st.info("Aplikasi ini berjalan di Jaringan Lokal Sekolah.")