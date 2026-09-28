import streamlit as st
import numpy as np

# ==========================================
# KONFIGURASI HALAMAN
# ==========================================

st.set_page_config(
    page_title="Kalkulator Matriks",
    page_icon="🔢",
    layout="centered"
)

# ==========================================
# JUDUL
# ==========================================

st.title("🔢 Kalkulator Matriks")

st.write(
    "Masukkan nilai matriks pada kotak yang tersedia, "
    "kemudian pilih operasi yang ingin dilakukan."
)

st.divider()


# ==========================================
# FUNGSI MEMBUAT INPUT MATRIKS
# ==========================================

def input_matriks(nama, baris, kolom, prefix):

    st.subheader(nama)

    matriks = []

    for i in range(baris):

        kolom_input = st.columns(kolom)

        baris_data = []

        for j in range(kolom):

            nilai = kolom_input[j].number_input(
                f"{nama} [{i+1},{j+1}]",
                value=0.0,
                step=1.0,
                key=f"{prefix}_{i}_{j}"
            )

            baris_data.append(nilai)

        matriks.append(baris_data)

    return np.array(matriks)


# ==========================================
# PILIH OPERASI
# ==========================================

operasi = st.selectbox(
    "Pilih Operasi",
    [
        "Penjumlahan",
        "Pengurangan",
        "Perkalian",
        "Transpose",
        "Determinan",
        "Invers",
        "Rank",
        "Trace"
    ]
)


# ==========================================
# UKURAN MATRIKS A
# ==========================================

st.subheader("Ukuran Matriks A")

col1, col2 = st.columns(2)

with col1:

    baris_a = st.number_input(
        "Baris",
        min_value=1,
        max_value=6,
        value=2,
        step=1
    )

with col2:

    kolom_a = st.number_input(
        "Kolom",
        min_value=1,
        max_value=6,
        value=2,
        step=1
    )


# ==========================================
# INPUT MATRIKS A
# ==========================================

A = input_matriks(
    "Matriks A",
    int(baris_a),
    int(kolom_a),
    "A"
)


# ==========================================
# INPUT MATRIKS B
# ==========================================

B = None

if operasi in [
    "Penjumlahan",
    "Pengurangan",
    "Perkalian"
]:

    st.divider()

    st.subheader("Ukuran Matriks B")

    if operasi == "Perkalian":

        st.info(
            "Untuk A × B, jumlah kolom A "
            "harus sama dengan jumlah baris B."
        )

        baris_b = int(kolom_a)

        kolom_b = st.number_input(
            "Kolom Matriks B",
            min_value=1,
            max_value=6,
            value=2,
            step=1
        )

    else:

        baris_b = int(baris_a)
        kolom_b = int(kolom_a)

    B = input_matriks(
        "Matriks B",
        baris_b,
        int(kolom_b),
        "B"
    )


# ==========================================
# TOMBOL
# ==========================================

st.divider()

col_hitung, col_reset = st.columns(2)

with col_hitung:

    hitung = st.button(
        "🔢 HITUNG",
        type="primary",
        use_container_width=True
    )

with col_reset:

    reset = st.button(
        "🔄 RESET",
        use_container_width=True
    )


# ==========================================
# PERHITUNGAN
# ==========================================

if hitung:

    try:

        # ----------------------------------
        # PENJUMLAHAN
        # ----------------------------------

        if operasi == "Penjumlahan":

            hasil = A + B

            st.success("Penjumlahan berhasil.")

            st.subheader("Hasil A + B")

            st.write(hasil)


        # ----------------------------------
        # PENGURANGAN
        # ----------------------------------

        elif operasi == "Pengurangan":

            hasil = A - B

            st.success("Pengurangan berhasil.")

            st.subheader("Hasil A - B")

            st.write(hasil)


        # ----------------------------------
        # PERKALIAN
        # ----------------------------------

        elif operasi == "Perkalian":

            if A.shape[1] != B.shape[0]:

                st.error(
                    "Perkalian tidak dapat dilakukan. "
                    "Jumlah kolom A harus sama dengan "
                    "jumlah baris B."
                )

            else:

                hasil = A @ B

                st.success("Perkalian berhasil.")

                st.subheader("Hasil A × B")

                st.write(hasil)


        # ----------------------------------
        # TRANSPOSE
        # ----------------------------------

        elif operasi == "Transpose":

            hasil = A.T

            st.success("Transpose berhasil.")

            st.subheader("Transpose Matriks A")

            st.write(hasil)


        # ----------------------------------
        # DETERMINAN
        # ----------------------------------

        elif operasi == "Determinan":

            if baris_a != kolom_a:

                st.error(
                    "Determinan hanya dapat dihitung "
                    "untuk matriks persegi."
                )

            else:

                hasil = np.linalg.det(A)

                st.success("Determinan berhasil dihitung.")

                st.subheader("Determinan Matriks A")

                st.write(
                    f"det(A) = {hasil:.4f}"
                )


        # ----------------------------------
        # INVERS
        # ----------------------------------

        elif operasi == "Invers":

            if baris_a != kolom_a:

                st.error(
                    "Invers hanya dapat dihitung "
                    "untuk matriks persegi."
                )

            else:

                determinan = np.linalg.det(A)

                if abs(determinan) < 1e-10:

                    st.error(
                        "Matriks tidak mempunyai invers "
                        "karena determinannya = 0."
                    )

                else:

                    hasil = np.linalg.inv(A)

                    st.success("Invers berhasil dihitung.")

                    st.subheader("Invers Matriks A")

                    st.write(hasil)


        # ----------------------------------
        # RANK
        # ----------------------------------

        elif operasi == "Rank":

            hasil = np.linalg.matrix_rank(A)

            st.success("Rank berhasil dihitung.")

            st.subheader("Rank Matriks A")

            st.write(
                f"Rank(A) = {hasil}"
            )


        # ----------------------------------
        # TRACE
        # ----------------------------------

        elif operasi == "Trace":

            if baris_a != kolom_a:

                st.error(
                    "Trace hanya dapat dihitung "
                    "untuk matriks persegi."
                )

            else:

                hasil = np.trace(A)

                st.success("Trace berhasil dihitung.")

                st.subheader("Trace Matriks A")

                st.write(
                    f"Tr(A) = {hasil}"
                )


    except Exception as error:

        st.error(
            f"Terjadi kesalahan: {error}"
        )


# ==========================================
# INFORMASI
# ==========================================

st.divider()

st.caption(
    "Dibuat menggunakan Python + Streamlit + NumPy"
)
