# 🚀 Ghid Rapid: Actualizare Cod pe PythonAnywhere

## 📦 Ce trebuie să faci:

### 1. **Upload Cod Modificat**

#### Opțiunea A: Upload Manual (Cel mai simplu)

1. **Loghează-te** pe https://www.pythonanywhere.com/
2. **Mergi la Files tab**
3. **Navighează** la `/home/Vasile70Tanasa/portfolio/` (sau unde ai proiectul)
4. **Upload următoarele fișiere/foldere:**

**Foldere complete (mai ușor):**
- `pages/` (întreg folder-ul)
- `projects/` (întreg folder-ul)
- `personal_portfolio/` (întreg folder-ul)
- `templates/` (dacă ai modificat)

**Sau fișiere individuale:**
- `requirements.txt`
- `pages/static/CV.pdf` (noul CV)
- `personal_portfolio/settings.py` (actualizat pentru producție)

---

### 2. **Instalează Pachete Noi**

1. **Deschide Bash Console** în PythonAnywhere
2. **Rulează:**
```bash
cd /home/Vasile70Tanasa/portfolio
pip3.10 install --user openai python-dotenv
```

Sau instalează toate:
```bash
pip3.10 install --user -r requirements.txt
```

---

### 3. **Configurează Environment Variables**

1. **Mergi la Web tab**
2. **Scroll la "Environment variables"**
3. **Adaugă:**
   - **Name**: `OPENAI_API_KEY`
   - **Value**: `sk-your-actual-key-here`
   
   - **Name**: `SECRET_KEY`  
   - **Value**: Generează unul nou (folosește: https://djecrety.ir/ sau `python -c "import secrets; print(secrets.token_urlsafe(50))"`)

---

### 4. **Colectează Static Files**

În **Bash Console**:
```bash
cd /home/Vasile70Tanasa/portfolio
python3.10 manage.py collectstatic --noinput
```

---

### 5. **Reload Web App**

1. **Mergi la Web tab**
2. **Click pe butonul verde "Reload"**
3. **Așteaptă 10-20 secunde**
4. **Testează site-ul**: https://Vasile70Tanasa.eu.pythonanywhere.com

---

## ✅ Checklist Rapid

- [ ] Upload cod modificat
- [ ] Instalat `openai` și `python-dotenv`
- [ ] Setat `OPENAI_API_KEY` în Environment variables
- [ ] Setat `SECRET_KEY` în Environment variables
- [ ] Rulat `collectstatic`
- [ ] Reload web app
- [ ] Testat site-ul

---

## 🎯 Fișiere Modificate (pentru referință)

Dacă vrei să uploadezi doar ce s-a schimbat:

**CSS (design nou):**
- `pages/static/CSS/general.css`
- `pages/static/CSS/chatbot.css`
- `pages/static/CSS/rest.css`
- `projects/static/styles/projects.css`

**Templates (responsive):**
- `pages/templates/pages/home.html`
- `projects/templates/projects/project_index.html`
- `projects/templates/projects/project_detail.html`

**Backend:**
- `pages/views.py` (chatbot OpenAI)
- `projects/views.py` (error handling)
- `personal_portfolio/settings.py` (detectare PythonAnywhere)

**Dependențe:**
- `requirements.txt` (openai, python-dotenv)

**Fișiere statice:**
- `pages/static/CV.pdf` (noul CV)

---

## 🐛 Dacă ceva nu funcționează:

1. **Verifică logs** în Web tab → "Error log"
2. **Verifică** că toate pachetele sunt instalate
3. **Verifică** environment variables sunt setate corect
4. **Clear browser cache** și reîncarcă

---

## 💡 Sfat

Cel mai simplu: **Upload întreg folder-ul `pages/` și `projects/`** - asta acoperă toate modificările!

