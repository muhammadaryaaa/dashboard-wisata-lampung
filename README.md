\# Dashboard Wisata Provinsi Lampung



Dashboard interaktif berbasis Streamlit yang digunakan untuk mengeksplorasi, menganalisis, dan memvisualisasikan data destinasi wisata di Provinsi Lampung, Indonesia.



Aplikasi ini dirancang untuk membantu pengguna memahami informasi mengenai destinasi wisata melalui tampilan dashboard yang interaktif dan mudah digunakan.



\## Demo



Dashboard dapat diakses secara online melalui Streamlit Community Cloud setelah proses deployment selesai.



> Link aplikasi: tambahkan URL Streamlit Anda di bagian ini setelah deployment.



\## Fitur



Dashboard ini menyediakan beberapa fungsi utama untuk membantu eksplorasi data destinasi wisata, di antaranya:



\* Menampilkan data destinasi wisata di Provinsi Lampung

\* Eksplorasi data secara interaktif

\* Penyajian informasi dalam bentuk visualisasi

\* Filter data berdasarkan informasi yang tersedia

\* Penyajian data destinasi dalam tampilan dashboard

\* Pengolahan data menggunakan Python dan Pandas

\* Visualisasi interaktif menggunakan library Python yang digunakan dalam aplikasi



\## Teknologi yang Digunakan



Project ini dikembangkan menggunakan:



\* Python

\* Streamlit

\* Pandas

\* CSV Dataset

\* Library visualisasi Python yang tercantum pada `requirements.txt`



\## Struktur Project



```text

dashboard-wisata-lampung/

│

├── app.py

├── Dataset\_Destinasi\_Wisata\_Provinsi\_Lampung.csv

├── requirements.txt

├── run\_dashboard.bat

│

└── .streamlit/

&#x20;   └── config.toml

```



\## Persyaratan



Sebelum menjalankan aplikasi secara lokal, pastikan komputer telah memiliki:



\* Python 3.x

\* pip

\* Git

\* Browser modern



Disarankan menggunakan virtual environment agar dependency project tidak bercampur dengan project Python lainnya.



\## Instalasi



Clone repository:



```bash

git clone https://github.com/USERNAME/dashboard-wisata-lampung.git

```



Masuk ke direktori project:



```bash

cd dashboard-wisata-lampung

```



Buat virtual environment:



```bash

python -m venv venv

```



Aktifkan virtual environment pada Windows:



```bash

venv\\Scripts\\activate

```



Aktifkan pada Linux atau macOS:



```bash

source venv/bin/activate

```



Install seluruh dependency:



```bash

pip install -r requirements.txt

```



\## Menjalankan Dashboard



Setelah semua dependency terinstall, jalankan:



```bash

streamlit run app.py

```



Setelah perintah dijalankan, Streamlit akan memberikan alamat lokal seperti:



```text

http://localhost:8501

```



Buka alamat tersebut menggunakan browser untuk melihat dashboard.



Pada Windows, project juga menyediakan file:



```text

run\_dashboard.bat

```



File tersebut dapat digunakan untuk menjalankan dashboard dengan lebih praktis apabila konfigurasi lokal sudah sesuai.



\## Cara Menggunakan Dashboard



Setelah dashboard terbuka, pengguna dapat mengeksplorasi informasi destinasi wisata melalui tampilan yang tersedia.



Alur penggunaan secara umum:



1\. Buka halaman dashboard.

2\. Periksa ringkasan informasi yang tersedia.

3\. Gunakan filter yang tersedia untuk memilih data tertentu.

4\. Amati tabel dan visualisasi yang ditampilkan.

5\. Bandingkan informasi antar destinasi atau wilayah sesuai kebutuhan.

6\. Gunakan hasil visualisasi sebagai bahan eksplorasi dan analisis data wisata.



\## Dataset



Dataset yang digunakan dalam aplikasi terdapat pada file:



```text

Dataset\_Destinasi\_Wisata\_Provinsi\_Lampung.csv

```



Dataset tersebut digunakan sebagai sumber data utama untuk menampilkan informasi destinasi wisata pada dashboard.



\## Deployment



Aplikasi dapat di-deploy menggunakan Streamlit Community Cloud.



Tahapan deployment:



1\. Upload seluruh source code ke repository GitHub.

2\. Pastikan `app.py` berada pada root repository.

3\. Pastikan `requirements.txt` tersedia.

4\. Pastikan dataset yang digunakan aplikasi juga tersedia di repository.

5\. Login ke Streamlit Community Cloud menggunakan akun GitHub.

6\. Pilih repository project.

7\. Pilih branch `main`.

8\. Masukkan:



```text

app.py

```



sebagai Main file path.

9\. Jalankan deployment.

10\. Setelah deployment berhasil, aplikasi dapat diakses menggunakan URL Streamlit yang diberikan.



\## Deployment Architecture



```text

GitHub Repository

&#x20;      │

&#x20;      ▼

Streamlit Community Cloud

&#x20;      │

&#x20;      ▼

&#x20;    app.py

&#x20;      │

&#x20;      ▼

Dataset CSV

&#x20;      │

&#x20;      ▼

Interactive Dashboard

```



\## Pengembangan



Untuk melakukan perubahan pada dashboard:



```text

Edit source code

&#x20;     ↓

Test secara lokal

&#x20;     ↓

Commit perubahan

&#x20;     ↓

Push ke GitHub

&#x20;     ↓

Streamlit melakukan deployment ulang

```



Contoh:



```bash

git add .

git commit -m "Update dashboard"

git push origin main

```



\## Troubleshooting



\### ModuleNotFoundError



Jika muncul error seperti:



```text

ModuleNotFoundError: No module named 'nama\_library'

```



pastikan library tersebut tercantum di dalam:



```text

requirements.txt

```



Kemudian lakukan deployment ulang.



\### FileNotFoundError



Jika aplikasi tidak menemukan dataset, periksa lokasi:



```text

Dataset\_Destinasi\_Wisata\_Provinsi\_Lampung.csv

```



dan pastikan path yang digunakan pada `app.py` sesuai dengan struktur repository.



\### Dashboard tidak dapat berjalan



Jalankan aplikasi melalui terminal:



```bash

streamlit run app.py

```



Kemudian periksa pesan error yang muncul.



\## Tujuan Project



Project ini dibuat sebagai media eksplorasi dan visualisasi data destinasi wisata di Provinsi Lampung. Dashboard diharapkan dapat memberikan cara yang lebih mudah untuk memahami informasi wisata melalui pendekatan visual dan interaktif.



\## Kontribusi



Kontribusi terhadap project ini terbuka. Pengguna dapat melakukan fork repository, melakukan perubahan, kemudian mengajukan pull request.



\## Lisensi



Project ini dapat digunakan untuk keperluan pembelajaran, penelitian, pengembangan aplikasi, dan eksplorasi data dengan tetap memperhatikan sumber serta ketentuan penggunaan dataset yang digunakan.



\## Author



\*\*\[Nama Anda]\*\*



GitHub: `https://github.com/muhammadaryaaa`



\## Repository



Source code project:



`https://github.com/muhammadaryaaa/dashboard-wisata-lampung`

