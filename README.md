```

![CI](https://github.com/fqhtmpt/qa-automation-project/actions/workflows/ci.yml/badge.svg)

```

# ✅ QA Automation Project

Proyek ini berisi script otomatisasi pengujian (**UI Test Automation**) untuk fitur login pada website [SauceDemo](https://www.saucedemo.com/) menggunakan **Python**, **Selenium**, dan **PyTest**.

---

## 🔧 Teknologi yang Digunakan

- Python 3
- Selenium WebDriver
- PyTest
- PyTest HTML Report

```

## 📁 Struktur Folder

qa-automation-project/
├── pages/
│   └── login_page.py           # Page Object untuk halaman login
│
├── tests/
│   └── test_login.py           # Berisi script pengujian login
│
├── reports/
│   └── report.html             # Hasil laporan pengujian dalam format HTML
│
├── utils/                      # (opsional) Fungsi bantu jika ada
├── requirements.txt            # Dependency untuk project
└── README.md                   # Dokumentasi project

```

## ✅ Skenario Pengujian

- [✔️] Login dengan **username & password yang benar**
- [✔️] Login dengan **username & password yang salah** (validasi error)
- [✔️] Login dengan username & password yang benar
- [✔️] Login dengan username & password yang salah (validasi error)
- [✔️] Kombinasi input kosong, spasi, dan karakter aneh
- [✔️] Input panjang ekstrem (300+ karakter)


---

## 🚀 Cara Menjalankan Tes

1. Install semua dependency yang dibutuhkan:
   ```bash
   pip install -r requirements.txt
