@echo off
chcp 65001 >nul
title Dashboard Wisata Lampung
color 0B

echo.
echo ============================================================
echo            DASHBOARD WISATA LAMPUNG
echo            Streamlit dan Plotly
echo ============================================================
echo.

cd /d "%~dp0"

where python >nul 2>nul
if errorlevel 1 (
    echo Python belum terdeteksi di perangkat ini.
    echo Silakan instal Python terlebih dahulu, lalu jalankan kembali file ini.
    pause
    exit /b
)

echo Menginstal library yang dibutuhkan...
python -m pip install --upgrade pip >nul
python -m pip install -r requirements.txt

echo.
echo Menjalankan dashboard...
echo.
echo Dashboard akan terbuka di browser.
echo Local   : http://localhost:8501
echo Network : http://IP-KOMPUTER-ANDA:8501
echo.
echo Tekan Ctrl + C untuk menghentikan server.
echo ============================================================
echo.

python -m streamlit run app.py --server.address 0.0.0.0 --server.port 8501 --browser.gatherUsageStats false

pause
