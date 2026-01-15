import streamlit as st

# 1. Fungsi untuk Panel Login
def login():
    st.title("🔐 Login Ruas Studio")
    st.subheader("Sistem Kendali SMK Nasional")
    
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Masuk")
        
        if submit:
            # Bapak bisa ganti username & password di bawah ini
            if username == "admin" and password == "smk123":
                st.session_state["authenticated"] = True
                st.rerun()
            else:
                st.error("Username atau Password salah!")

# 2. Cek apakah user sudah login atau belum
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()
else:
    # --- HALAMAN UTAMA (Dashboard yang tadi) ---
    st.sidebar.button("Log Out", on_click=lambda: st.session_state.update({"authenticated": False}))
    
    st.title("🛡️ DASHBOARD KENDALI")
    st.success(f"Selamat Datang, Administrator")
    
    col1, col2 = st.columns(2)
    col1.metric("Dana BOS", "Rp 125jt")
    col2.metric("Pengeluaran", "Rp 12.5jt")
    
    st.write("### Laporan Masuk")
    st.info("Belum ada laporan baru hari ini.")