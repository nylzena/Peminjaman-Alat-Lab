import streamlit as st
from datetime import date
import time

st.set_page_config(page_title=brown "Pengembalian Alat Praktikum")

if "step" not in st.session_state:
    st.session_state.step = 1
if "data" not in st.session_state:
    st.session_state.data = {}

alat_list = [
    "Pipet tetes",
    "Gelas beaker 50 mL,
    "Gelas beaker 50 mL, 100, 250, 500, 1000 mL)",
    "Gelas ukur (5, 10, 50, 100 mL)",
    "Labu takar (5, 10, 25, 50, 100 mL)",
    "Cawan petri",
    "Buret (Mikro, Semi-Mikro, Makro)",
    "Kasa Asbes",
    "Bunsen",
    "Tabung reaksi (Biasa, Ulir)",
    "Corong Kaca",
    "Penjepit Kayu",
    "Batang Pengaduk",
    "Kaki tiga"
]

if st.session_state.step == 1:
    st.title("Form Peminjaman Alat Praktikum")

    nama = st.text_input("Nama")
    kelompok = st.text_input("Kelompok")
    tanggal = st.date_input("Tanggal", value=date.today())
    judul = st.text_input("Judul Praktik")
    matkul = st.text_input("Mata Kuliah")

    st.subheader("Pilih Alat")
    alat_dipilih = [a for a in alat_list if st.checkbox(a)]

    if st.button("Lanjutkan"):
        if not all([nama, kelompok, judul, matkul, alat_dipilih]):
            st.warning("Semua wajib diisi")
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

elif st.session_state.step == 2:
    st.title("Resume")

    d = st.session_state.data
    st.write("Nama:", d["nama"])
    st.write("Kelompok:", d["kelompok"])
    st.write("Judul:", d["judul"])
    st.write("Mata Kuliah:", d["matkul"])

    st.subheader("Alat Dipinjam")
    for a in d["alat"]:
        st.write("-", a)

    if st.button("Lanjutkan"):
        st.session_state.step = 3
        st.rerun()

elif st.session_state.step == 3:
    st.title("Upload Bukti Pengembalian")
    foto = st.file_uploader("Upload foto", type=["jpg", "png", "jpeg"])

    if foto:
        st.image(foto)
        if st.button("Konfirmasi"):
            st.session_state.step = 4
            st.rerun()

elif st.session_state.step == 4:
    with st.spinner("Memproses..."):
        time.sleep(2)
    st.success("✅ Pengembalian terkonfirmasi!")
    st.balloons()
