# 🏗️ Construction Safety Detection – YOLOv12 + Streamlit  
Proyek ini adalah sistem *Object Detection* untuk mendeteksi pekerja konstruksi dan mengevaluasi kelengkapan APD (Alat Pelindung Diri) seperti **helmet**, **vest**, dan kategori **no-vest** atau **no-helmet**.

Model dilatih menggunakan **YOLOv12** dan aplikasi dibangun dengan **Streamlit** sehingga pengguna dapat mengunggah gambar dan langsung melihat hasil deteksi beserta *safety analysis*-nya.

---

## 🚀 Features

### 🔍 **1. Object Detection (YOLOv12)**
Model dapat mendeteksi objek:
- `person`
- `helmet`
- `vest`
- `no-vest`
- `no-helmet`

### 🔢 **2. Object Counting**
Aplikasi otomatis menghitung:
- Total pekerja
- Jumlah pekerja memakai helmet
- Jumlah pekerja memakai vest
- Jumlah pekerja *tanpa* vest
- Jumlah pekerja *tanpa* helmet

### ⚠️ **3. Safety Compliance Analysis**
Aplikasi memberikan evaluasi keselamatan:
- Jika ada pekerja tidak memakai APD → ditampilkan sebagai **ERROR alert**
- Jika semua lengkap → ditampilkan **SUCCESS alert**

### 🖥️ **4. Streamlit Web App**
- Upload gambar
- Deteksi otomatis
- Hasil visualisasi dengan bounding box
- Output *counting* dan analisis keselamatan

---

## 📁 Project Structure

├── Streamlit.py # Main streamlit app
├── requirements.txt # Dependencies
├── weights/
│ ├── best.pt # Model terbaik
│ └── last.pt (opsional)
└── README.md # Documentation

yaml
Copy code

---

## 🧠 Model Information

- **Framework** : Ultralytics YOLOv12  
- **Epoch Training** : 50 (best result at ~epoch 21)  
- **Dataset** : Construction Safety (Helmet, Vest, No-Vest, No-Helmet, Person)

---

## 🛠️ Installation

Clone repo:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run Streamlit app:

bash
Copy code
streamlit run Streamlit.py
