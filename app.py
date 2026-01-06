import streamlit as st
from datetime import date
import time

# ================== KONFIGURASI HALAMAN ==================
st.set_page_config(
    page_title="Pengembalian Alat Praktikum",
    layout="centered"
)

# ================== STYLE / BACKGROUND ==================
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #ff758c, #ff7eb3);
    }

    h1, h2, h3 {
        color: white;
        text-align: center;
    }

    label {
        color: white !important;
        font-weight: bold;
    }

    .card {
        background-color: rgba(255,255,255,0.18);
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 20px;
    }

    .stButton > button {
        background-color: white;
        color: #ff758c;
        border-radius: 10px;
        height: 45px;
        width: 100%;
        font-size: 16px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ================== SESSION STATE ==================
if "step" not in st.session_state:
    st.session_state.step = 1

if "data" not in st.session_state:
    st.session_state.data = {}

# ================== DAFTAR ALAT ==================
alat_list = [
    "Pipet tetes",
    "Gelas beaker (50, 100, 250, 500, 1000 mL)",
    "Gelas ukur (5, 10, 50, 100 mL)",
    "Labu takar (5, 10, 25, 50, 100 mL)",
    "Cawan petri",
    "Buret (Mikro, Semi-Mikro, Makro)",
    "Kasa Asbes",
    "Bunsen",
    "Tabung reaksi (Biasa, Ulir)",
    "Corong kaca",
    "Penjepit kayu",
    "Batang pengaduk",
    "Kaki tiga"
]

# ================== STEP 1 ==================
if st.session_state.step == 1:
    st.title("Form Peminjaman Alat Praktikum")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    nama = st.text_input("Nama")
    kelompok = st.text_input("Kelompok")
    tanggal = st.date_input("Tanggal", value=date.today())
    judul = st.text_input("Judul Praktik")
    matkul = st.text_input("Mata Kuliah")

    st.subheader("Pilih Alat yang Digunakan")
    alat_dipilih = []
    for alat in alat_list:
        if st.checkbox(alat):
            alat_dipilih.append(alat)

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Lanjutkan"):
        if not nama or not kelompok or not judul or not matkul or not alat_dipilih:
            st.warning("⚠️ Semua data wajib diisi")
        else:
            st.session_state.data = {
                "nama": nama,
                "kelompok": kelompok,
                "tanggal": tanggal,
                "judul": judul,
                "matkul": matkul,
                "alat": alat_dipilih
            }
            st.session_state.step = 2
            st.rerun()

# ================== STEP 2 ==================
elif st.session_state.step == 2:
    st.title("Resume Konfirmasi")

    d = st.session_state.data

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write(f"**Nama:** {d['nama']}")
    st.write(f"**Kelompok:** {d['kelompok']}")
    st.write(f"**Tanggal:** {d['tanggal']}")
    st.write(f"**Judul Praktik:** {d['judul']}")
    st.write(f"**Mata Kuliah:** {d['matkul']}")

    st.subheader("Alat yang Dipinjam:")
    for a in d["alat"]:
        st.write(f"- {a}")

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Lanjutkan"):
        st.session_state.step = 3
        st.rerun()

# ================== STEP 3 ==================
elif st.session_state.step == 3:
    st.title("Bukti Dokumentasi Pengembalian Alat")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    foto = st.file_uploader(
        "Upload foto pengembalian alat",
        type=["jpg", "jpeg", "png"]
    )

    if foto:
        st.image(foto, use_container_width=True)

        if st.button("Konfirmasi Pengembalian"):
            st.session_state.step = 4
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ================== STEP 4 ==================
elif st.session_state.step == 4:
    st.title("Status Pengembalian")

    with st.spinner("Memverifikasi pengembalian alat..."):
        time.sleep(2)

    st.success("✅ Pengembalian terkonfirmasi!")
    st.balloons()
