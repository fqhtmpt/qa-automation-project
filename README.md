![CI](https://github.com/fqhtmpt/qa-automation-project/actions/workflows/ci.yml/badge.svg)

# QA Automation Project

Sebuah project automation testing berbasis Python + Selenium untuk menguji login form dari situs [SauceDemo](https://www.saucedemo.com/).

## ✅ Fitur yang Diotomasi
- Login dengan kredensial valid
- Validasi pesan error login invalid
- Test input ekstrem (karakter khusus, panjang, dll)

## ⚙️ Tech Stack
- Python 3.11
- Selenium WebDriver
- PyTest
- HTML Report (`pytest-html`)
- GitHub Actions CI (badge di atas 👆)

## 📂 Struktur Folder


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

#
## 📄 Cara Menjalankan Test
```bash
pip install -r requirements.txt
pytest tests/ --html=reports/report.html

