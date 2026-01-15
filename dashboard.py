import streamlit as st

# 1. Konfigurasi Akun & Jabatan
# Format: "username": {"password": "pw", "role": "Jabatan"}
users = {
    "kepsek": {"password": "123", "role": "Kepala Sekolah"},
    "kurikulum": {"password": "kur", "role": "Waka Kurikulum"},
    "kesiswaan": {"password": "kes", "role": "Waka Kesiswaan"},
    "sarpras": {"password": "sar", "role": "Waka Sarpras"},
    "hubin": {"password": "hub", "role": "Waka Hubin"},
    "ktu": {"password": "ktu", "role": "Kepala TU (KTU)"},
    "bendahara": {"password": "bos", "role": "Bendahara BOS"},
    "keuangan": {"password": "adm", "role": "Admin Keuangan"},
    "bk": {"password": "bk1", "role": "Guru BK"},
    "laboran": {"password": "lab", "role": "Laboran"},
    "osis": {"password": "osi", "role": "Pembina OSIS"},
    "media": {"password": "med", "role": "Tim Media"},
    "tertib": {"password": "ter", "role": "Tim Ketertiban"}
}

def login():
    st.markdown("<h2 style='text-align: center;'>🔐 LOGIN SISTEM KENDALI</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>SMK NASIONAL - RUAS STUDIO</p>", unsafe_allow_html=True)
    
    with st.container():
        username = st.text_input("Username Jabatan")
        password = st.text_input("Password", type="password")
        if st.button("Masuk ke Sistem", use_container_width=True):
            if username in users and users[username]["password"] == password:
                st.session_state["auth"] = True
                st.session_state["role"] = users[username]["role"]
                st.session_state["user"] = username
                st.rerun()
            else:
                st.error("Username atau Password salah!")

if "auth" not in st.session_state:
    st.session_state["auth"] = False

if not st.session_state["auth"]:
    login()
else:
    # --- HALAMAN SETELAH LOGIN ---
    role = st.session_state["role"]
    
    # Sidebar untuk Profil
    st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
    st.sidebar.title(st.session_state["user"].upper())
    st.sidebar.info(f"Jabatan: **{role}**")
    
    if st.sidebar.button("Keluar Sistem"):
        st.session_state["auth"] = False
        st.rerun()

    # --- TAMPILAN BERDASARKAN JABATAN ---
    st.title(f"🛡️ Panel Kendali: {role}")
    st.write(f"Selamat datang di sistem manajemen SMK Nasional.")

    # 1. Menu Khusus Pimpinan (Kepsek, KTU)
    if role in ["Kepala Sekolah", "Kepala TU (KTU)"]:
        st.subheader("📊 Ringkasan Seluruh Unit")
        col1, col2, col3 = st.columns(3)
        col1.metric("Keuangan", "Aman")
        col2.metric("Absensi Guru", "98%")
        col3.metric("Sarpras", "Terkendali")

    # 2. Menu Keuangan (Bendahara BOS, Admin Keuangan)
    elif role in ["Bendahara BOS", "Admin Keuangan"]:
        st.subheader("💰 Manajemen Anggaran")
        st.date_input("Tanggal Transaksi")
        st.number_input("Jumlah Pengeluaran (Rp)")
        st.file_uploader("Upload Bukti Nota")

    # 3. Menu Kesiswaan & OSIS (Waka Kesiswaan, Pembina OSIS, BK)
    elif role in ["Waka Kesiswaan", "Pembina OSIS", "Guru BK", "Tim Ketertiban"]:
        st.subheader("👥 Kedisiplinan & Siswa")
        st.text_area("Input Laporan Kejadian/Siswa")
        st.selectbox("Tindakan", ["Teguran", "Panggilan Orang Tua", "Selesai"])

    # 4. Menu Sarpras & Laboran
    elif role in ["Waka Sarpras", "Laboran"]:
        st.subheader("📦 Inventaris Barang")
        st.write("Daftar Aset Baru:")
        st.checkbox("Lab Komputer - Aktif")
        st.checkbox("Alat Praktik - Terawat")

    # 5. Menu Umum Lainnya
    else:
        st.subheader("📝 Laporan Kerja Mingguan")
        st.text_input("Kegiatan hari ini")
        st.button("Kirim Laporan")

    st.divider()
    st.caption("RUAS STUDIO © 2026 - Aplikasi Kendali Internal")