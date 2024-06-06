import pandas as pd

# Data produk
data_produk = {
    "Nama Produk": [
        "TDS SENSOR METER V1.0 SENSOR PENGUKUR KUALITAS AIR FOR ARDUINO UNO R3",
        "Ds18b20 Modul Sensor Suhu Stainless Steel Probe Suhu Tahan Air",
        "PH-4502C Modul Board Sensor PH Meter With Probe Electrode For Arduino",
        "Relai 4 Channel",
        "Panel Surya Solar Panel 100W Panel Surya Portabel Polikristalin Fleksibel Kendaraan Telepon Fleksibel Kapal Papan Pengisian Darurat",
        "Pompa Peristaltik",
        "Relai 2 channel (opsional)"
    ],
    "Harga (Rp)": [
        88800,
        88400,
        229000,
        19635,
        331000,
        145000,
        21829
    ],
    "Situs": [
        "Shopee",
        "Shopee, Tokopedia",
        "Shopee, Tokopedia",
        "Shopee, Tokopedia",
        "Shopee, Tokopedia",
        "Shopee, Tokopedia",
        "Shopee, Tokopedia"
    ],
    "Link": [
        "https://shopee.co.id/product/122002734/25502736612?gsht=lwnqHg0W2FYOya3H",
        "https://www.tokopedia.com/rekomendasi/9834924435?srsltid=AfmBOork1YKUUm6PsyxlC9GdU7QAzVus1cqgupnB1VNKN8n_YHLYvTBYsPM",
        "https://www.blibli.com/p/ph-4502c-modul-board-sensor-ph-meter-with-probe-electrode-for-arduino/is--DIM-70193-00009-00001?pickupPointCode=PP-3519285&srsltid=AfmBOorU_KDiDl4kt1fJq4CXUnfCCTBAIzou0S4Q-D8KwHuxXRrZAsvhBk0",
        "https://shopee.co.id/product/906610/109616057?gsht=lwnqHg0W2FYOya3H",
        "https://shopee.co.id/product/1054176118/25155929570?gsht=lwnqHg0W2FYOya3H",
        "https://shopee.co.id/product/64269189/5179554495?gsht=lwnqHg0W2FYOya3H",
        "https://shopee.co.id/product/13486297/2660550834?gsht=lwnqHg0W2FYOya3H"
    ]
}

# Membuat DataFrame
df_produk = pd.DataFrame(data_produk)

# Menjumlahkan harga
total_harga = df_produk["Harga (Rp)"].sum()

# Menghitung jumlah barang
jumlah_barang = len(df_produk)

# Menampilkan DataFrame dan hasil penjumlahan
print(df_produk)
print(f"\nTotal Harga: Rp{total_harga:,}")
print(f"Jumlah Barang: {jumlah_barang}")
