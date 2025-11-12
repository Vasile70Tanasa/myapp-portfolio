# 🚀 Ghid Complet: Deploy Django Portfolio pe PythonAnywhere

## 📋 Cuprins
1. [Pregătire Inițială](#pregătire-inițială)
2. [Configurare PythonAnywhere](#configurare-pythonanywhere)
3. [Deploy Cod](#deploy-cod)
4. [Configurare Web App](#configurare-web-app)
5. [Configurare Static Files](#configurare-static-files)
6. [Configurare Environment Variables](#configurare-environment-variables)
7. [Testare și Verificare](#testare-și-verificare)
8. [Actualizări Viitoare](#actualizări-viitoare)
9. [Troubleshooting](#troubleshooting)

---

## 1. Pregătire Inițială

### 1.1 Verifică Codul Local

Asigură-te că:
- ✅ Codul funcționează local
- ✅ Toate dependențele sunt în `requirements.txt`
- ✅ `settings.py` detectează automat PythonAnywhere
- ✅ `ALLOWED_HOSTS` include domeniul tău PythonAnywhere

### 1.2 Verifică Structura Proiectului

```
portfolio/
├── manage.py
├── requirements.txt
├── personal_portfolio/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── pages/
│   ├── views.py
│   ├── urls.py
│   ├── static/
│   └── templates/
├── projects/
│   ├── views.py
│   ├── urls.py
│   └── static/
└── staticfiles/  (va fi generat de collectstatic)
```

---

## 2. Configurare PythonAnywhere

### 2.1 Creare Cont PythonAnywhere

1. Mergi la https://www.pythonanywhere.com/
2. Creează un cont (free tier este suficient pentru început)
3. Loghează-te în dashboard

### 2.2 Deschide Consola Bash

1. Click pe tab-ul **"Consoles"** din meniul de sus
2. Click pe **"Bash"** pentru a deschide o consolă nouă
3. Sau folosește consola existentă

### 2.3 Clonează Repository-ul Git

```bash
# Navighează la directorul home
cd ~

# Clonează repository-ul (înlocuiește cu URL-ul tău Git)
git clone https://github.com/Vasile70Tanasa/myapp-portfolio.git portfolio

# Sau dacă ai deja folderul, navighează în el
cd ~/portfolio
```

**Dacă nu folosești Git:**
- Poți uploada manual fișierele prin tab-ul **"Files"**
- Sau folosește SFTP pentru upload în masă

### 2.4 Creează Virtual Environment (Recomandat)

```bash
# Navighează în directorul proiectului
cd ~/portfolio

# Creează virtual environment
python3.10 -m venv venv

# Activează virtual environment
source venv/bin/activate

# Verifică că e activat (ar trebui să vezi (venv) în prompt)
which python  # Ar trebui să arate că folosește venv
```

**Notă:** PythonAnywhere folosește Python 3.10 pentru free accounts.

---

## 3. Deploy Cod

### 3.1 Instalează Dependențe

```bash
# Asigură-te că ești în directorul proiectului
cd ~/portfolio

# Activează virtual environment (dacă nu e deja activat)
source venv/bin/activate

# Instalează toate dependențele
pip install --user -r requirements.txt
```

**Dependențe importante:**
- `Django==4.1.6`
- `openai>=1.40.0` (pentru chatbot)
- `python-dotenv==1.0.0` (pentru environment variables)
- `gunicorn==21.2.0` (pentru WSGI)

### 3.2 Verifică Instalarea

```bash
# Verifică că Django este instalat
python manage.py --version

# Ar trebui să vezi: 4.1.6
```

---

## 4. Configurare Web App

### 4.1 Creează Web App

1. Mergi la tab-ul **"Web"** din dashboard
2. Click pe **"Create a new web app"**
3. Alege **"Manual configuration"**
4. Selectează **"Python 3.10"**
5. Click **"Next"**

### 4.2 Configurează WSGI File

1. În tab-ul **"Web"**, scroll la secțiunea **"WSGI configuration file"**
2. Click pe link-ul către fișierul WSGI
3. Șterge tot conținutul și adaugă:

```python
# +++++++++++ DJANGO +++++++++++
# To use your own Django app use code like this:
import os
import sys

# Assuming your Django settings file is at '/home/Vasile70Tanasa/portfolio/personal_portfolio/settings.py'
path = '/home/Vasile70Tanasa/portfolio'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'personal_portfolio.settings'

# Then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**IMPORTANT:** Înlocuiește `Vasile70Tanasa` cu username-ul tău PythonAnywhere!

4. Salvează fișierul (Ctrl+S sau butonul Save)

### 4.3 Configurează Source Code și Working Directory

În tab-ul **"Web"**, în secțiunea **"Code"**:

- **Source code:** `/home/Vasile70Tanasa/portfolio`
- **Working directory:** `/home/Vasile70Tanasa/portfolio`

**IMPORTANT:** Înlocuiește `Vasile70Tanasa` cu username-ul tău!

---

## 5. Configurare Static Files

### 5.1 Rulează collectstatic

```bash
# În consolă Bash
cd ~/portfolio
source venv/bin/activate  # dacă folosești venv
python manage.py collectstatic --noinput
```

Aceasta va crea folderul `staticfiles/` cu toate fișierele statice.

### 5.2 Configurează Static Files Mapping

În tab-ul **"Web"**, scroll la secțiunea **"Static files"**:

1. Click pe **"Add a new static files mapping"**
2. **URL:** `/static/`
3. **Directory:** `/home/Vasile70Tanasa/portfolio/staticfiles`

**IMPORTANT:** Înlocuiește `Vasile70Tanasa` cu username-ul tău!

### 5.3 Configurează Media Files (dacă ai)

1. Click pe **"Add a new static files mapping"**
2. **URL:** `/media/`
3. **Directory:** `/home/Vasile70Tanasa/portfolio/uploads`

---

## 6. Configurare Environment Variables

### 6.1 Setează Variabile în Web Tab (Recomandat)

În tab-ul **"Web"**, scroll la secțiunea **"Environment variables"**:

1. Click pe **"Add a new environment variable"**
2. Adaugă:
   - **Name:** `SECRET_KEY`
   - **Value:** `[generează-o-cheie-secretă-puternică]`

3. Click pe **"Add a new environment variable"** din nou
4. Adaugă:
   - **Name:** `OPENAI_API_KEY`
   - **Value:** `sk-your-openai-api-key-here` (dacă ai)

**Cum generezi SECRET_KEY:**
```python
# În consolă Python
python
>>> from django.core.management.utils import get_random_secret_key
>>> print(get_random_secret_key())
```

### 6.2 Sau Creează Fișier .env (Alternativă)

```bash
# În consolă Bash
cd ~/portfolio
nano .env
```

Adaugă:
```
SECRET_KEY=your-secret-key-here
OPENAI_API_KEY=sk-your-openai-api-key-here
```

Salvează: `Ctrl+O`, `Enter`, `Ctrl+X`

**IMPORTANT:** Asigură-te că `.env` este în `.gitignore` și nu este commitat în Git!

---

## 7. Testare și Verificare

### 7.1 Rulează Migrații

```bash
cd ~/portfolio
source venv/bin/activate  # dacă folosești venv
python manage.py migrate
```

### 7.2 Creează Superuser (pentru admin)

```bash
python manage.py createsuperuser
```

Urmează instrucțiunile pentru a crea un cont admin.

### 7.3 Reload Web App

1. Mergi la tab-ul **"Web"**
2. Scroll la secțiunea **"Reload"**
3. Click pe butonul mare verde **"Reload"**
4. Așteaptă câteva secunde

### 7.4 Verifică Site-ul

Deschide în browser:
- `https://Vasile70Tanasa.eu.pythonanywhere.com`

**IMPORTANT:** Înlocuiește `Vasile70Tanasa` cu username-ul tău!

### 7.5 Verifică Logs (dacă sunt erori)

În tab-ul **"Web"**, scroll la secțiunea **"Error log"**:
- Click pe link pentru a vedea erorile (dacă există)

---

## 8. Actualizări Viitoare

### 8.1 Workflow pentru Actualizări

#### Opțiunea A: Folosind Git (Recomandat)

```bash
# În consolă Bash pe PythonAnywhere
cd ~/portfolio
git pull origin main

# Activează venv (dacă folosești)
source venv/bin/activate

# Instalează dependențe noi (dacă există)
pip install --user -r requirements.txt

# Rulează migrații (dacă ai schimbări în modele)
python manage.py migrate

# Colectează static files (dacă ai schimbări în CSS/JS)
python manage.py collectstatic --noinput

# Reload web app din tab-ul Web
```

#### Opțiunea B: Upload Manual

1. Upload fișierele modificate prin tab-ul **"Files"**
2. Rulează comenzile de mai sus (migrate, collectstatic)
3. Reload web app

### 8.2 Checklist pentru Fiecare Actualizare

- [ ] Cod actualizat (git pull sau upload manual)
- [ ] Dependențe noi instalate (dacă există)
- [ ] Migrații rulate (dacă ai schimbări în modele)
- [ ] Static files colectate (dacă ai schimbări în CSS/JS)
- [ ] Web app reloadat
- [ ] Site testat în browser

---

## 9. Troubleshooting

### 9.1 Eroare: "Module not found"

**Cauză:** Pachetele nu sunt instalate sau virtual environment nu este activat.

**Soluție:**
```bash
cd ~/portfolio
source venv/bin/activate  # dacă folosești venv
pip install --user -r requirements.txt
```

### 9.2 Eroare: "DisallowedHost"

**Cauză:** `ALLOWED_HOSTS` nu include domeniul tău.

**Soluție:** Verifică în `settings.py` că include:
```python
ALLOWED_HOSTS = ['Vasile70Tanasa.eu.pythonanywhere.com', 'www.Vasile70Tanasa.eu.pythonanywhere.com']
```

### 9.3 Static Files nu se încarcă

**Cauză:** Static files mapping nu este configurat corect sau `collectstatic` nu a fost rulat.

**Soluție:**
1. Verifică Static files mapping în Web tab:
   - `/static/` → `/home/Vasile70Tanasa/portfolio/staticfiles`
2. Rulează:
```bash
python manage.py collectstatic --noinput
```

### 9.4 Chatbot nu funcționează

**Cauză:** `OPENAI_API_KEY` nu este setat sau nu este corect.

**Soluție:**
1. Verifică Environment variables în Web tab
2. Verifică logs în Web tab pentru erori
3. Dacă nu ai API key, chatbot-ul va folosi versiunea simplă (pattern matching)

### 9.5 Eroare: "SECRET_KEY not set"

**Cauză:** `SECRET_KEY` nu este setat în environment variables.

**Soluție:**
1. Adaugă `SECRET_KEY` în Environment variables din Web tab
2. Sau creează fișier `.env` cu `SECRET_KEY`

### 9.6 Site-ul arată vechi (cache)

**Soluție:**
1. Clear browser cache: `Ctrl+Shift+Delete`
2. Sau adaugă `?v=2` la URL pentru forțare refresh
3. Sau folosește incognito mode pentru testare

### 9.7 Eroare: "No module named 'dotenv'"

**Cauză:** `python-dotenv` nu este instalat.

**Soluție:**
```bash
pip install --user python-dotenv
```

### 9.8 Eroare 500 Internal Server Error

**Soluție:**
1. Verifică Error log în Web tab
2. Verifică că toate dependențele sunt instalate
3. Verifică că `SECRET_KEY` este setat
4. Verifică că `ALLOWED_HOSTS` include domeniul tău

---

## 📝 Note Importante

### Securitate

- ✅ **NU commit** `.env` sau `SECRET_KEY` în Git
- ✅ **Folosește environment variables** pentru chei sensibile
- ✅ **DEBUG = False** în producție (deja configurat automat)
- ✅ **SECRET_KEY** diferit pentru producție

### Best Practices

- ✅ **Testează local** înainte de deploy
- ✅ **Backup** codul vechi înainte de actualizare
- ✅ **Folosește Git** pentru version control
- ✅ **Documentează** schimbările importante

### Limitări Free Tier

- ⚠️ **1 web app** activă
- ⚠️ **512 MB** storage
- ⚠️ **100,000 requests/day**
- ⚠️ **No custom domains** (doar `.pythonanywhere.com`)

---

## 🎯 Quick Reference

### Comenzi Esențiale

```bash
# Navigare
cd ~/portfolio

# Activează venv
source venv/bin/activate

# Instalează dependențe
pip install --user -r requirements.txt

# Migrații
python manage.py migrate

# Colectează static files
python manage.py collectstatic --noinput

# Creează superuser
python manage.py createsuperuser

# Verifică configurare
python manage.py check
```

### Path-uri Importante

- **Source code:** `/home/Vasile70Tanasa/portfolio`
- **WSGI file:** `/home/Vasile70Tanasa/portfolio/personal_portfolio/wsgi.py`
- **Static files:** `/home/Vasile70Tanasa/portfolio/staticfiles`
- **Media files:** `/home/Vasile70Tanasa/portfolio/uploads`

**IMPORTANT:** Înlocuiește `Vasile70Tanasa` cu username-ul tău PythonAnywhere!

---

## ✅ Checklist Final Deploy

- [ ] Cont PythonAnywhere creat
- [ ] Repository clonat sau cod uploadat
- [ ] Virtual environment creat și activat
- [ ] Dependențe instalate
- [ ] Web app creat și configurat
- [ ] WSGI file configurat corect
- [ ] Static files mapping configurat
- [ ] Environment variables setate (SECRET_KEY, OPENAI_API_KEY)
- [ ] Migrații rulate
- [ ] collectstatic rulat
- [ ] Web app reloadat
- [ ] Site accesat și testat
- [ ] Admin panel funcționează
- [ ] Static files se încarcă corect
- [ ] Chatbot funcționează (dacă ai API key)

---

## 🆘 Suport

Dacă întâmpini probleme:

1. **Verifică Error log** în Web tab
2. **Verifică Server log** în Web tab
3. **Verifică că toate pașii** din checklist sunt completați
4. **Consultă documentația Django:** https://docs.djangoproject.com/
5. **Consultă documentația PythonAnywhere:** https://help.pythonanywhere.com/

---

**Succes cu deploy-ul! 🚀**

