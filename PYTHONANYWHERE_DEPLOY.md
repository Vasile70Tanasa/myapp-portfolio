# Ghid Deploy pe PythonAnywhere - Actualizare Cod

## 📋 Pași pentru actualizarea codului pe PythonAnywhere

### 1. Pregătire cod pentru producție

#### A. Actualizează settings.py pentru producție

Trebuie să modifici `settings.py` să detecteze automat dacă rulează pe PythonAnywhere:

```python
# Detectare automată PythonAnywhere
import os
ON_PYTHONANYWHERE = os.environ.get('PYTHONANYWHERE_DOMAIN', '').endswith('.pythonanywhere.com')

# Debug mode
if ON_PYTHONANYWHERE:
    DEBUG = False
else:
    DEBUG = True  # Development local

# Secret Key
if ON_PYTHONANYWHERE:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-key-change-in-production')
else:
    SECRET_KEY = "django-insecure-x(b^d1_90*3v&6sn&hd*lm07r3-1v=pmw^jza!$4n2m5#wgt*b"

# Allowed Hosts
if ON_PYTHONANYWHERE:
    ALLOWED_HOSTS = ['Vasile70Tanasa.eu.pythonanywhere.com', 'www.Vasile70Tanasa.eu.pythonanywhere.com']
else:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']
```

---

### 2. Upload cod pe PythonAnywhere

#### Opțiunea A: Upload manual (cel mai simplu)

1. **Conectează-te la PythonAnywhere**
   - Mergi la https://www.pythonanywhere.com/
   - Loghează-te în contul tău

2. **Deschide Files tab**
   - Click pe "Files" în meniul de sus

3. **Navighează la directorul proiectului**
   - De obicei: `/home/Vasile70Tanasa/portfolio/` sau `/home/Vasile70Tanasa/mysite/`

4. **Upload fișiere modificate:**
   - Click pe "Upload a file"
   - Upload fișierele modificate:
     - `pages/static/CSS/general.css`
     - `pages/static/CSS/chatbot.css`
     - `pages/static/CSS/rest.css`
     - `projects/static/styles/projects.css`
     - `pages/templates/pages/home.html`
     - `projects/templates/projects/project_index.html`
     - `projects/templates/projects/project_detail.html`
     - `pages/views.py`
     - `projects/views.py`
     - `personal_portfolio/settings.py`
     - `requirements.txt`
     - `pages/static/CV.pdf` (noul CV)
   - Sau upload întreg folder-ul `pages/` și `projects/`

#### Opțiunea B: Git (dacă ai Git configurat)

1. **În consolă PythonAnywhere:**
```bash
cd /home/Vasile70Tanasa/portfolio
git pull origin main  # sau master, sau branch-ul tău
```

---

### 3. Instalează dependențe noi

1. **Deschide Bash Console** în PythonAnywhere
2. **Activează virtual environment** (dacă ai):
```bash
source /home/Vasile70Tanasa/.virtualenvs/portfolio/bin/activate
# sau
source /home/Vasile70Tanasa/portfolio/venv/bin/activate
```

3. **Instalează pachete noi:**
```bash
cd /home/Vasile70Tanasa/portfolio
pip3.10 install --user -r requirements.txt
```

**Pachete noi de instalat:**
- `openai>=1.40.0` (pentru chatbot)
- `python-dotenv==1.0.0` (pentru .env)

---

### 4. Configurează Environment Variables

1. **Mergi la Web tab** în PythonAnywhere
2. **Scroll la "Environment variables"**
3. **Adaugă variabilele:**
   - `OPENAI_API_KEY` = `sk-your-actual-key-here`
   - `SECRET_KEY` = `generate-a-new-secret-key-here` (folosește un generator online)

**Sau creează fișier `.env` în root:**
```bash
cd /home/Vasile70Tanasa/portfolio
nano .env
```

Adaugă:
```
OPENAI_API_KEY=sk-your-key-here
SECRET_KEY=your-secret-key-here
```

---

### 5. Colectează Static Files

```bash
cd /home/Vasile70Tanasa/portfolio
python3.10 manage.py collectstatic --noinput
```

Aceasta va copia toate fișierele statice în folderul `staticfiles/`.

---

### 6. Rulează Migrații (dacă ai schimbări în modele)

```bash
python3.10 manage.py migrate
```

---

### 7. Configurează Web App

1. **Mergi la Web tab**
2. **Verifică configurarea:**
   - **Source code**: `/home/Vasile70Tanasa/portfolio`
   - **Working directory**: `/home/Vasile70Tanasa/portfolio`
   - **WSGI file**: `/home/Vasile70Tanasa/portfolio/personal_portfolio/wsgi.py`

3. **Verifică Static files mapping:**
   - `/static/` → `/home/Vasile70Tanasa/portfolio/staticfiles/`
   - `/media/` → `/home/Vasile70Tanasa/portfolio/uploads/`

---

### 8. Reload Web App

1. **Click pe butonul verde "Reload"** în Web tab
2. **Așteaptă câteva secunde**
3. **Accesează site-ul**: `https://Vasile70Tanasa.eu.pythonanywhere.com`

---

## ✅ Checklist Final

- [ ] Cod actualizat uploadat
- [ ] Dependențe instalate (`openai`, `python-dotenv`)
- [ ] Environment variables setate (`OPENAI_API_KEY`, `SECRET_KEY`)
- [ ] `collectstatic` rulat
- [ ] `migrate` rulat (dacă e necesar)
- [ ] Web app configurat corect
- [ ] Web app reloadat
- [ ] Site testat în browser

---

## 🐛 Troubleshooting

### Eroare: "Module not found"
- Verifică că ai instalat toate pachetele: `pip3.10 install --user -r requirements.txt`

### Static files nu se încarcă
- Verifică că ai rulat `collectstatic`
- Verifică Static files mapping în Web tab

### Chatbot nu funcționează
- Verifică că `OPENAI_API_KEY` este setat în Environment variables
- Verifică logs în Web tab pentru erori

### Site-ul arată vechi
- Clear browser cache (Ctrl+Shift+Delete)
- Sau adaugă `?v=2` la URL pentru forțare refresh

---

## 📝 Note Importante

- **Nu commit** `.env` sau `SECRET_KEY` în Git
- **Folosește environment variables** pentru chei sensibile
- **Testează local** înainte de deploy
- **Backup** codul vechi înainte de actualizare

