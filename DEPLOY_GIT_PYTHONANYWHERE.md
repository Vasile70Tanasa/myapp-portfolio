# 🚀 Deploy pe PythonAnywhere prin Git - Ghid Complet

## 📋 Pași pentru Deploy

### Faza 1: Pregătire Cod Local (ACASA)

#### 1.1. Commit toate modificările

```powershell
# Verifică ce modificări ai
git status

# Adaugă toate modificările
git add .

# Commit cu mesaj descriptiv
git commit -m "Update: modern design, OpenAI chatbot, responsive layout, improved mobile UX"

# Push pe GitHub
git push origin main
```

**Notă:** Dacă ai erori la push, verifică branch-ul:
```powershell
git branch  # Vezi ce branch ești
# Dacă ești pe 'master' în loc de 'main':
git push origin master
```

---

### Faza 2: Setup pe PythonAnywhere (PRIMA DATĂ)

#### 2.1. Conectează-te la PythonAnywhere

1. Mergi la https://www.pythonanywhere.com/
2. Loghează-te în contul tău
3. Deschide **Bash Console**

#### 2.2. Clonează repository-ul (dacă nu ai deja codul)

```bash
cd /home/Vasile70Tanasa
git clone https://github.com/Vasile70Tanasa/myapp-portfolio.git portfolio
cd portfolio
```

**SAU** dacă ai deja codul vechi:

```bash
cd /home/Vasile70Tanasa/portfolio
git init
git remote add origin https://github.com/Vasile70Tanasa/myapp-portfolio.git
git pull origin main --allow-unrelated-histories
```

---

### Faza 3: Configurare PythonAnywhere

#### 3.1. Instalează dependențe

```bash
cd /home/Vasile70Tanasa/portfolio
pip3.10 install --user -r requirements.txt
```

**Pachete importante:**
- `openai>=1.40.0` (pentru chatbot)
- `python-dotenv==1.0.0` (pentru .env)
- `Django` (deja în requirements.txt)

#### 3.2. Configurează Environment Variables

**Opțiunea A: Environment Variables (RECOMANDAT)**

1. Mergi la **Web tab** în PythonAnywhere
2. Scroll la **"Environment variables"**
3. Adaugă:
   - **Name:** `OPENAI_API_KEY`
   - **Value:** `sk-your-actual-key-here`
   
   - **Name:** `SECRET_KEY`
   - **Value:** Generează unul nou:
     ```bash
     python3.10 -c "import secrets; print(secrets.token_urlsafe(50))"
     ```

**Opțiunea B: Fișier .env**

```bash
cd /home/Vasile70Tanasa/portfolio
nano .env
```

Adaugă:
```
OPENAI_API_KEY=sk-your-actual-key-here
SECRET_KEY=your-generated-secret-key-here
```

#### 3.3. Verifică settings.py

Verifică că `settings.py` detectează automat PythonAnywhere:

```python
# Detectare automată PythonAnywhere
import os
ON_PYTHONANYWHERE = os.environ.get('PYTHONANYWHERE_DOMAIN', '').endswith('.pythonanywhere.com')

# Debug mode
if ON_PYTHONANYWHERE:
    DEBUG = False
else:
    DEBUG = True
```

Dacă nu detectează corect, verifică:
```bash
echo $PYTHONANYWHERE_DOMAIN
```

#### 3.4. Creează baza de date

```bash
cd /home/Vasile70Tanasa/portfolio
python3.10 manage.py migrate
```

#### 3.5. Colectează static files

```bash
python3.10 manage.py collectstatic --noinput
```

---

### Faza 4: Configurează Web App

#### 4.1. Creează Web App (dacă nu există)

1. Mergi la **Web tab**
2. Click **"Add a new web app"**
3. Selectează **Manual configuration**
4. Selectează **Python 3.10**

#### 4.2. Configurează WSGI file

1. Click pe link-ul către WSGI file
2. Editează și setează:

```python
import os
import sys

# Add your project directory to the sys.path
path = '/home/Vasile70Tanasa/portfolio'
if path not in sys.path:
    sys.path.insert(0, path)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'personal_portfolio.settings'

# Import Django's WSGI handler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

#### 4.3. Configurează Static Files

În **Web tab**, la **Static files**:

- **URL:** `/static/`
- **Directory:** `/home/Vasile70Tanasa/portfolio/staticfiles/`

- **URL:** `/media/`
- **Directory:** `/home/Vasile70Tanasa/portfolio/uploads/`

#### 4.4. Verifică Source code și Working directory

În **Web tab**:
- **Source code:** `/home/Vasile70Tanasa/portfolio`
- **Working directory:** `/home/Vasile70Tanasa/portfolio`

---

### Faza 5: Reload și Testare

#### 5.1. Reload Web App

1. Mergi la **Web tab**
2. Click pe butonul verde **"Reload"**
3. Așteaptă 10-20 secunde

#### 5.2. Testează site-ul

Accesează: `https://Vasile70Tanasa.eu.pythonanywhere.com`

**Verifică:**
- [ ] Home page se încarcă
- [ ] Design-ul arată modern
- [ ] Butonul chatbot apare
- [ ] Chatbotul funcționează
- [ ] Pagina de proiecte funcționează
- [ ] Static files se încarcă (CSS, imagini)

---

## 🔄 Actualizări Viitoare (După Deploy)

### Când vrei să actualizezi codul:

**Local:**
```powershell
# 1. Modifici codul
# 2. Commit
git add .
git commit -m "Descriere modificări"
git push origin main
```

**Pe PythonAnywhere:**
```bash
cd /home/Vasile70Tanasa/portfolio
git pull origin main
python3.10 manage.py collectstatic --noinput
# Apoi click Reload în Web tab
```

**Timp total: ~30 secunde!** ⚡

---

## ✅ Checklist Final

### Înainte de Deploy:
- [ ] Toate modificările sunt commit-uite local
- [ ] Codul este push-at pe GitHub
- [ ] `requirements.txt` este actualizat
- [ ] `settings.py` detectează PythonAnywhere

### Pe PythonAnywhere:
- [ ] Repository-ul este clonat/pull-at
- [ ] Dependențele sunt instalate (`pip3.10 install --user -r requirements.txt`)
- [ ] Environment variables sunt setate (`OPENAI_API_KEY`, `SECRET_KEY`)
- [ ] Migrațiile sunt aplicate (`python3.10 manage.py migrate`)
- [ ] Static files sunt colectate (`python3.10 manage.py collectstatic --noinput`)
- [ ] Web app este configurat corect
- [ ] Web app este reload-at

### După Deploy:
- [ ] Site-ul se încarcă corect
- [ ] Design-ul arată bine
- [ ] Chatbotul funcționează
- [ ] Toate paginile funcționează

---

## 🐛 Troubleshooting

### Eroare: "Module not found"
```bash
pip3.10 install --user -r requirements.txt
```

### Static files nu se încarcă
```bash
python3.10 manage.py collectstatic --noinput
```
Verifică Static files mapping în Web tab.

### Chatbot nu funcționează
- Verifică că `OPENAI_API_KEY` este setat în Environment variables
- Verifică logs în Web tab pentru erori

### Site-ul arată vechi
- Clear browser cache (Ctrl+Shift+Delete)
- Sau adaugă `?v=2` la URL pentru forțare refresh

### Git pull nu funcționează
```bash
# Verifică remote
git remote -v

# Dacă nu există:
git remote add origin https://github.com/Vasile70Tanasa/myapp-portfolio.git

# Pull cu force (dacă ai conflicte)
git pull origin main --allow-unrelated-histories
```

---

## 📝 Note Importante

- **NU commit** `.env` sau `SECRET_KEY` în Git
- **Folosește environment variables** pentru chei sensibile
- **Testează local** înainte de deploy
- **Backup** codul vechi înainte de actualizare (Git face asta automat!)

---

## 🎯 Comenzi Rapide

### Setup inițial:
```bash
cd /home/Vasile70Tanasa
git clone https://github.com/Vasile70Tanasa/myapp-portfolio.git portfolio
cd portfolio
pip3.10 install --user -r requirements.txt
python3.10 manage.py migrate
python3.10 manage.py collectstatic --noinput
```

### Actualizare:
```bash
cd /home/Vasile70Tanasa/portfolio
git pull origin main
python3.10 manage.py collectstatic --noinput
# Apoi Reload în Web tab
```

---

## 🚀 GATA!

După ce urmezi pașii de mai sus, site-ul tău va fi live pe PythonAnywhere! 🎉

