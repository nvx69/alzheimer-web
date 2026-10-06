@echo off
cd /d "%~dp0"
echo Installing/checking dependencies...
python -m pip install -r requirements.txt
echo.
echo Starting Alzheimer website...
echo On this PC: http://127.0.0.1:5000
echo From another PC on the same Wi-Fi, use this PC's IPv4 address, e.g. http://192.168.1.10:5000
echo.
python app.py
pause
