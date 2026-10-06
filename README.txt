AI Alzheimer Risk Assessment - Flask Backend

HOW TO RUN ON THIS COMPUTER
1. Install Python 3.10+ if needed.
2. Open this folder in CMD.
3. Run: pip install -r requirements.txt
4. Run: python app.py
5. Open: http://127.0.0.1:5000/

OPEN FROM ANOTHER COMPUTER ON THE SAME WI-FI
1. Run python app.py on the computer hosting the website.
2. Find the host computer IPv4 address with: ipconfig
3. On the other computer open: http://HOST-IP:5000/
   Example: http://192.168.1.10:5000/
4. If Windows Firewall asks, allow Python on Private networks.

ONLINE DEPLOYMENT
This project includes a Procfile and PORT support for Python hosting services such as Render.
Use the build command: pip install -r requirements.txt
Use the start command: gunicorn app:app

IMPORTANT
This is a student-project educational prototype, not a validated medical model or diagnosis.
