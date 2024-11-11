import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from datetime import datetime
import os

# Fungsi untuk memuat data pengguna dari file CSV
def load_users():
    if os.path.exists("users.csv"):
        return pd.read_csv("users.csv").set_index("username").to_dict("index")
    else:
        return {}

# Fungsi untuk menyimpan data pengguna ke file CSV
def save_users(users):
    users_df = pd.DataFrame(users).T.reset_index()
    users_df.columns = ["username", "password"]
    users_df.to_csv("users.csv", index=False)

# Fungsi untuk halaman login
def login_page():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")
    
    # Verifikasi login
    if login_button:
        if username in st.session_state["users"] and st.session_state["users"][username] == password:
            st.session_state["authenticated"] = True
            st.session_state["page"] = "Main"
            st.success("Login berhasil!")
        else:
            st.error("Username atau password salah")

# Fungsi untuk halaman register
def register_page():
    st.title("Register")
    Nama = st.text_input("Nama")
    username = st.text_input("Username")
    Jabatan = st.text_input("Jabatan")
    password = st.text_input("Password", type="password")
    register_button = st.button("Register")
    
    # Contoh penyimpanan data username dan password di session (untuk demo)
    if register_button:
        if username and password:
            st.session_state["users"][username] = password
            st.success("Register berhasil! Silakan login.")
            st.session_state["page"] = "Login"
        else:
            st.error("Username dan password harus diisi!")

# Fungsi untuk halaman utama setelah login
def main_page():
    with st.sidebar:
        selected = option_menu("Navigation", ["Home", "Brand List", "Transaction", "Inventory",
                                              "General Ledger", "Financial Statements", "Logout"],
                               icons=['house', 'list', 'box', 'currency-dollar', 'book', 'graph-up', 'telephone', 'box-arrow-left'],
                               menu_icon="cast", default_index=0)
        st.session_state["selected_menu"] = selected

    # Konten berdasarkan menu yang dipilih
    if selected == "Home":
        st.title("Selamat datang di Marugame2nd")
        st.subheader("Toko Sneakers Shop Semarang")
        st.write("Marugame2nd adalah toko yang menawarkan sepatu bekas berkualitas tinggi dan branded. Mereka mengutamakan produk yang stylish dan terjangkau,serta memiliki koleksi yang bervariasi untuk memenuhi kebutuhan fashion pengunjung. Toko ini aktif di media sosial, seperti Instagram dan TikTok, untuk mempromosikan produk-produk terbaru dan berinteraksi dengan pelanggan. Jika Anda mencari sepatu yang unik dengan harga bersahabat, Marugame2nd bisa menjadi pilihan yang tepat. Untuk informasi lebih lanjut, Anda bisa mengunjungi profil yang tertera dibawah ini.")

        # Menambahkan Deskripsi Toko
        st.write("WhatsApp : [085163228078](https://wa.me/6285163228078)")
        st.write("Instagram : [marugame2nd](https://www.instagram.com/marugame2nd)")
        st.write("Shopee : [marugame2nd_](https://id.shp.ee/igVzcFA)")
        st.write("Tokopedia : [marugame2nd_](https://tokopedia.link/6OSoK1AVeOb)")
        st.write("Alamat : Jl. Taman Sriging, Patemon, Kec. Gn. Pati, Kota Semarang, Jawa Tengah 50228")

        # Konten halaman Home
    elif selected == "Brand List":
        st.title("Brand List")

        # Data contoh untuk Brand List (Ini adalah contoh data, Anda bisa mengganti dengan data asli dari database)
        brands_data = {
            "New Balance": [
                {"Kode": "NB001", "Tipe": "New Balance 530", "Ukuran": "22 - 46"},
                {"Kode": "NB002", "Tipe": "New Balance 990", "Ukuran": "22 - 46"},
                {"Kode": "NB003", "Tipe": "New Balance 991", "Ukuran": "22 - 46"},
                {"Kode": "NB004", "Tipe": "New Balance 1906", "Ukuran": "22 - 46"},
                {"Kode": "NB005", "Tipe": "New Balance 327", "Ukuran": "22 - 46"},
                {"Kode": "NB006", "Tipe": "New Balance 2002R", "Ukuran": "22 - 46"},
            ],
            "Nike": [
                {"Kode": "NK001", "Tipe": "Jordan Low", "Ukuran": "24 - 46"},
                {"Kode": "NK002", "Tipe": "Jordan High", "Ukuran": "24 - 46"},
                {"Kode": "NK003", "Tipe": "Sbdunk", "Ukuran": "24 - 46"},
                {"Kode": "NK004", "Tipe": "Airmax 97", "Ukuran": "24 - 46"},
                {"Kode": "NK005", "Tipe": "Airmax 95", "Ukuran": "24 - 46"},
            ],
            "Adidas": [
                {"Kode": "AD001", "Tipe": "Samba", "Ukuran": "24 - 45",},
                {"Kode": "AD002", "Tipe": "Gazella", "Ukuran": "24 - 45",},
                {"Kode": "AD003", "Tipe": "Spezial", "Ukuran": "24 - 45",},
                {"Kode": "AD004", "Tipe": "Superstar", "Ukuran": "24 - 45"},
            ],
            "Reebook": [
                {"Kode": "RB001", "Tipe": "C85", "Ukuran": "25 - 45", },
            ],
            "Hoka": [
                {"Kode": "HK001", "Tipe": "Challenger Atr 7", "Ukuran": "23 - 46",},
                {"Kode": "HK002", "Tipe": "Rincon 3", "Ukuran": "23 - 46",},
                {"Kode": "HK003", "Tipe": "Speedgoat 5", "Ukuran": "23 - 46",},
            ],
            "Onitsuka Tiger": [
                {"Kode": "OT001", "Tipe": "Tiger Mexico", "Ukuran": "22 - 45",},
                {"Kode": "OT002", "Tipe": "Tokuten", "Ukuran": "22 - 45",},
            ]
        }

        # Fungsi untuk menampilkan daftar merk dan kode barang terkait
        def brand_list_page():

            # Pilih merk dari dropdown list
            brand_selected = st.selectbox("Pilih Merk", options=list(brands_data.keys()))

            # Ambil daftar kode barang untuk merk yang dipilih
            kode_barang_list = brands_data[brand_selected]

            # Menampilkan data dalam bentuk tabel
            df = pd.DataFrame(kode_barang_list)

            # Tampilkan tabel kode barang
            st.dataframe(df)

        # Menampilkan halaman brand list
        brand_list_page()
    
    if selected == "Transaction":
        st.title('Data Transaksi')
        
        # Ensure transactions is initialized as a list
        if 'transactions' not in st.session_state or not isinstance(st.session_state.transactions, list):
            st.session_state.transactions = []

        if 'inventory' not in st.session_state:
            st.session_state.inventory = {
                "New Balance": {"NB001": 100, "NB002": 135, "NB003": 150, "NB004": 115, "NB005": 65, "NB006": 35},
                "Nike": {"NK001": 85, "NK002": 65, "NK003": 150, "NK004": 175, "NK005": 125},
                "Adidas": {"AD001": 185, "AD002": 100, "AD003": 160, "AD004": 155},
                "Reebok": {"RB001": 350},
                "Hoka": {"HK001": 200, "HK002": 150, "HK003": 80},
                "Onitsuka Tiger": {"OT001": 110, "OT002": 140}
            }

        # Form input for new transaction
        nama_merk = st.selectbox('Merk', options=st.session_state.inventory.keys())
        kode_barang = st.selectbox('Kode Barang', options=st.session_state.inventory[nama_merk].keys())
        tanggal = st.date_input('Tanggal')
        jenis_transaksi = st.selectbox('Jenis Transaksi', ['Penjualan', 'Pembelian'])
        jenis_pembayaran = st.selectbox('Jenis Pembayaran', ['Cash', 'Kredit'])
        jumlah = st.number_input('Jumlah Barang', min_value=1, step=1)
        harga_satuan = st.number_input('Harga Satuan', min_value=0.0, step=0.01)
        total = jumlah * harga_satuan

        # Submit button to add a transaction
        submit_button = st.button('Tambah Transaksi')

        # Process when the submit button is clicked
        if submit_button:
            transaksi_baru = {
                'Tanggal': tanggal,
                'Jenis Transaksi': jenis_transaksi,
                'Pembayaran': jenis_pembayaran,
                'Merk': nama_merk,
                'Kode Barang': kode_barang,
                'Jumlah': jumlah,
                'Harga Satuan': harga_satuan,
                'Total': total
            }
            st.session_state.transactions.append(transaksi_baru)

            # Update stock based on transaction type
            if jenis_transaksi == 'Pembelian':
                st.session_state.inventory[nama_merk][kode_barang] += jumlah
            elif jenis_transaksi == 'Penjualan':
                if st.session_state.inventory[nama_merk][kode_barang] >= jumlah:
                    st.session_state.inventory[nama_merk][kode_barang] -= jumlah
                else:
                    st.warning(f"Stok {kode_barang} tidak mencukupi untuk penjualan.")
                    st.session_state.transactions.pop()  # Remove transaction if stock is insufficient

            st.success('Transaksi berhasil ditambahkan dan stok diperbarui!')

        # Display the transactions table if there are any transactions
        if st.session_state.transactions:
            # Convert the transactions to a DataFrame
            df = pd.DataFrame(st.session_state.transactions)

            # Display the transactions table
            st.subheader("Daftar Transaksi")
            st.dataframe(df)

            # Calculate total sales, purchases, and profit/loss
            total_penjualan = df[df['Jenis Transaksi'] == 'Penjualan']['Total'].sum()
            total_pembelian = df[df['Jenis Transaksi'] == 'Pembelian']['Total'].sum()

            # Display total sales and purchases
            st.write(f"**Total Penjualan**: Rp {total_penjualan:,.2f}")
            st.write(f"**Total Pembelian**: Rp {total_pembelian:,.2f}")

            # Calculate profit or loss
            selisih = total_penjualan - total_pembelian
            if selisih > 0:
                st.write(f"**Laba**: Rp {selisih:,.2f}")
            elif selisih < 0:
                st.write(f"**Rugi**: Rp {abs(selisih):,.2f}")
            else:
                st.write("**Keuangan Seimbang**")
        else:
            st.info('Belum ada transaksi. Silakan tambah transaksi baru.')


    elif selected == "Inventory":
        st.title("**Stok Barang Saat Ini**")

        # Inisialisasi inventory dan initial_inventory jika belum ada
        if 'inventory' not in st.session_state:
            st.session_state.inventory = {
                "New Balance": {"NB001": 100, "NB002": 135, "NB003": 150, "NB004": 115, "NB005": 65, "NB006": 35},
                "Nike": {"NK001": 85, "NK002": 65, "NK003": 150, "NK004": 175, "NK005":125},
                "Adidas": {"AD001": 185, "AD002": 100, "AD003": 160, "AD004": 155},
                "Reebook": {"RB001": 350},
                "Hoka": {"HK001": 200, "HK002": 150, "HK003": 80},
                "Onitsuka Tiger": {"OT001": 110, "OT002": 140},
            }

        if 'initial_inventory' not in st.session_state:
            st.session_state.initial_inventory = {
                merk: {kode_barang: stok for kode_barang, stok in items.items()}
                for merk, items in st.session_state.inventory.items()
            }

        # Buat tabel untuk persediaan awal dan persediaan akhir
        for merk, items in st.session_state.inventory.items():
            st.write(f"{merk}")
            
            # Hitung persediaan akhir berdasarkan persediaan awal dan transaksi
            inventory_data = []
            for kode_barang, stok in items.items():
                persediaan_awal = st.session_state.initial_inventory[merk][kode_barang]
                persediaan_akhir = persediaan_awal + stok  # Persediaan akhir

                inventory_data.append({
                    "Kode Barang": kode_barang,
                    "Persediaan Awal": persediaan_awal,
                    "Jumlah Stok": stok,
                    "Persediaan Akhir": persediaan_akhir,
                })

            # Tampilkan tabel persediaan
            df_inventory = pd.DataFrame(inventory_data)
            st.dataframe(df_inventory)

    elif selected == "General Ledger":
        # Judul aplikasi
        st.title('Tabel Pencatatan Transaksi')

        # Fungsi untuk halaman Jurnal Umum dan Buku Besar (General Ledger)
        def general_ledger_page():
            # Check if transactions exist in session_state
            if 'transactions' not in st.session_state or not st.session_state.transactions:
                st.info("Belum ada transaksi yang dicatat.")
                return

            # Create Jurnal Umum from the transactions
            journal_data = []
            for transaksi in st.session_state.transactions:
                if 'Jenis Transaksi' not in transaksi or 'Pembayaran' not in transaksi or 'Total' not in transaksi:
                    st.error("Some required fields are missing in the transaction data.")
                    return

                if transaksi['Jenis Transaksi'] == 'Penjualan':
                    if transaksi['Pembayaran'] == 'Cash':  # Penjualan dengan Cash
                        journal_data.append({
                            "Tanggal": transaksi['Tanggal'],
                            "Akun": "Kas",
                            "Debit": transaksi['Total'],
                            "Kredit": 0
                        })
                        journal_data.append({
                            "Tanggal": transaksi['Tanggal'],
                            "Akun": "Pendapatan Penjualan",
                            "Debit": 0,
                            "Kredit": transaksi['Total']
                        })
                    elif transaksi['Pembayaran'] == 'Kredit':  # Penjualan dengan Kredit
                        journal_data.append({
                            "Tanggal": transaksi['Tanggal'],
                            "Akun": "Piutang Usaha",
                            "Debit": transaksi['Total'],
                            "Kredit": 0
                        })
                        journal_data.append({
                            "Tanggal": transaksi['Tanggal'],
                            "Akun": "Pendapatan Penjualan",
                            "Debit": 0,
                            "Kredit": transaksi['Total']
                        })
                elif transaksi['Jenis Transaksi'] == 'Pembelian':
                    if transaksi['Pembayaran'] == 'Cash':  # Pembelian dengan Cash
                        journal_data.append({
                            "Tanggal": transaksi['Tanggal'],
                            "Akun": "Persediaan",
                            "Debit": transaksi['Total'],
                            "Kredit": 0
                        })
                        journal_data.append({
                            "Tanggal": transaksi['Tanggal'],
                            "Akun": "Kas",
                            "Debit": 0,
                            "Kredit": transaksi['Total']
                        })
                    elif transaksi['Pembayaran'] == 'Kredit':  # Pembelian dengan Kredit
                        journal_data.append({
                            "Tanggal": transaksi['Tanggal'],
                            "Akun": "Persediaan",
                            "Debit": transaksi['Total'],
                            "Kredit": 0
                        })
                        journal_data.append({
                            "Tanggal": transaksi['Tanggal'],
                            "Akun": "Utang Usaha",
                            "Debit": 0,
                            "Kredit": transaksi['Total']
                        })

            # Convert Jurnal Umum to a DataFrame and display it
            st.subheader("Jurnal Umum")
            journal_df = pd.DataFrame(journal_data)
            st.dataframe(journal_df)

            # Create Buku Besar (General Ledger) from the journal_data
            ledger_data = {}
            for entry in journal_data:
                akun = entry['Akun']
                if akun not in ledger_data:
                    ledger_data[akun] = []

                saldo_sebelumnya = ledger_data[akun][-1]["Saldo Akhir"] if ledger_data[akun] else 0
                saldo_akhir = saldo_sebelumnya + entry['Debit'] - entry['Kredit']

                ledger_data[akun].append({
                    "Tanggal": entry['Tanggal'],
                    "Debit": entry['Debit'],
                    "Kredit": entry['Kredit'],
                    "Saldo Akhir": saldo_akhir
                })

            # Display Buku Besar for each account in table format
            st.subheader("Buku Besar")
            for akun, entries in ledger_data.items():
                st.write(f"**Akun: {akun}**")
                df_ledger = pd.DataFrame(entries)
                st.dataframe(df_ledger)

        # Call general_ledger_page to test
        general_ledger_page()

    elif selected == "Financial Statements":
        st.title("Laporan Keuangan")

        if 'transactions' not in st.session_state or not st.session_state.transactions:
            st.info("Belum ada transaksi. Silakan tambah transaksi baru.")
        else:
            # Hitung total pendapatan dan biaya untuk Laporan Laba Rugi
            total_pendapatan = 0
            total_biaya = 0

            # Laporan Perubahan Ekuitas
            laba_bersih = 0

            for transaksi in st.session_state.transactions:
                if transaksi['Jenis Transaksi'] == 'Penjualan':
                    total_pendapatan += transaksi['Total']
                elif transaksi['Jenis Transaksi'] == 'Pembelian':
                    total_biaya += transaksi['Total']

            laba_bersih = total_pendapatan - total_biaya

            # Laporan Laba Rugi
            st.subheader("Laporan Laba Rugi")
            laba_rugi_data = {
                "Pendapatan": total_pendapatan,
                "Biaya": total_biaya,
                "Laba Bersih": laba_bersih
            }

            df_laba_rugi = pd.DataFrame(list(laba_rugi_data.items()), columns=["Akun", "Jumlah"])
            st.dataframe(df_laba_rugi)

            # Laporan Perubahan Ekuitas
            modal_awal = 45000000 
            modal_akhir = modal_awal + laba_bersih

            st.subheader("Laporan Perubahan Ekuitas")
            ekuitas_data = {
                "Modal Awal": modal_awal,
                "Laba Bersih": laba_bersih,
                "Modal Akhir": modal_akhir
            }

            df_ekuitas = pd.DataFrame(list(ekuitas_data.items()), columns=["Akun", "Jumlah"])
            st.dataframe(df_ekuitas)

            # Laporan Posisi Keuangan (Neraca)

            total_kas = 0
            total_piutang = 0
            total_utang = 0
            total_persediaan = 0

            # Menghitung total kas (penjualan cash)
            for transaksi in st.session_state.transactions:
                if transaksi['Jenis Transaksi'] == 'Penjualan' and transaksi['Pembayaran'] == 'Cash':
                    total_kas += transaksi['Total']
                elif transaksi['Jenis Transaksi'] == 'Pembelian' and transaksi['Pembayaran'] == 'Cash':
                    total_kas -= transaksi['Total']

            # Menghitung Piutang Usaha (Penjualan Kredit)
            for transaksi in st.session_state.transactions:
                if transaksi['Jenis Transaksi'] == 'Penjualan' and transaksi['Pembayaran'] == 'Kredit':
                    total_piutang += transaksi['Total']
                elif transaksi['Jenis Transaksi'] == 'Pembelian' and transaksi['Pembayaran'] == 'Kredit':
                    total_utang += transaksi['Total']

            # Persediaan (Stok Barang)
            total_persediaan = sum([sum(items.values()) for items in st.session_state.inventory.values()])

            st.subheader("Laporan Posisi Keuangan (Neraca)")
            neraca_data = {
                "Aset":
                {
                    "Kas": total_kas,
                    "Piutang Usaha": total_piutang,
                    "Persediaan": total_persediaan
                },
                "Kewajiban":
                {
                    "Utang Usaha": total_utang
                },
                "Ekuitas":
                {
                    "Modal Akhir": modal_akhir
                }
            }

            # Membuat tabel untuk Laporan Neraca
            neraca = []
            for kategori, akun_dict in neraca_data.items():
                for akun, jumlah in akun_dict.items():
                    neraca.append([kategori, akun, jumlah])

            df_neraca = pd.DataFrame(neraca, columns=["Kategori", "Akun", "Jumlah"])
            st.dataframe(df_neraca)
        
    elif selected == "Logout":
        # Setel ulang status login dan halaman
         st.session_state.clear()

# Main aplikasi
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "users" not in st.session_state:
    st.session_state["users"] = {}  # Dictionary untuk menyimpan user (sebagai contoh)
if "page" not in st.session_state:
    st.session_state["page"] = "Login"  # Mulai dengan halaman login

# Alur aplikasi berdasarkan status login
if st.session_state["authenticated"]:
    main_page()
else:
    if st.session_state["page"] == "Login":
        login_page()
        st.button("Belum punya akun? Register", on_click=lambda: st.session_state.update({"page": "Register"}))
    elif st.session_state["page"] == "Register":
        register_page()
        st.button("Sudah punya akun? Login", on_click=lambda: st.session_state.update({"page": "Login"}))
