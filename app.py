import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Peminjaman Alat Lab", layout="wide")

# ================= LOAD DATA =================
alat = pd.read_csv("data/alat.csv")
peminjaman = pd.read_csv("data/peminjaman.csv")

# ================= SIDEBAR =================
st.sidebar.title("🔐 Login")

role = st.sidebar.radio("Masuk sebagai:", ["User", "Admin"])
admin_password = "admin123"

if role == "Admin":
    password = st.sidebar.text_input("Password Admin", type="password")
    if password != admin_password:
        st.warning("Password salah")
        st.stop()

menu = st.sidebar.selectbox(
    "Menu",
    ["🏠 Daftar Alat", "📝 Pinjam Alat", "📊 Data Peminjaman"]
)

st.title("🔬 Sistem Peminjaman Alat Laboratorium")

# ================= DAFTAR ALAT =================
if menu == "🏠 Daftar Alat":
    st.subheader("📦 Katalog Alat")
    cols = st.columns(3)

    for idx, row in alat.iterrows():
        with cols[idx % 3]:
            st.markdown(f"### {row['nama']}")
            st.write(row["deskripsi"])
            st.info(f"Stok: {row['stok']}")

# ================= PINJAM ALAT =================
elif menu == "📝 Pinjam Alat":
    st.subheader("🧾 Form Peminjaman")

    nama = st.text_input("Nama Peminjam")
    alat_pilih = st.selectbox("Pilih Alat", alat["nama"])
    jumlah = st.number_input("Jumlah", 1, 10)
    tgl_kembali = st.date_input("Tanggal Kembali", min_value=date.today())

    if st.button("📥 Pinjam"):
        stok = alat.loc[alat["nama"] == alat_pilih, "stok"].values[0]

        if jumlah > stok:
            st.error("Stok tidak mencukupi")
        else:
            # Simpan peminjaman
            data_baru = {
                "nama": nama,
                "alat": alat_pilih,
                "jumlah": jumlah,
                "tanggal_pinjam": date.today(),
                "tanggal_kembali": tgl_kembali
            }

            peminjaman = pd.concat(
                [peminjaman, pd.DataFrame([data_baru])],
                ignore_index=True
            )
            peminjaman.to_csv("data/peminjaman.csv", index=False)

            # Update stok
            alat.loc[alat["nama"] == alat_pilih, "stok"] -= jumlah
            alat.to_csv("data/alat.csv", index=False)

            st.success("✅ Peminjaman berhasil!")

# ================= DATA PEMINJAMAN =================
elif menu == "📊 Data Peminjaman":
    st.subheader("📋 Riwayat Peminjaman")
    st.dataframe(peminjaman)
