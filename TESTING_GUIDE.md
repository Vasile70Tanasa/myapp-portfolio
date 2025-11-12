# Ghid de Testare Locală - Portfolio Django

## 📋 Pași pentru testare locală

### 1. Activează Virtual Environment

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 2. Instalează Dependențele

```bash
pip install -r requirements.txt
```

### 3. Verifică Migrațiile

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Creează un Superuser (opțional, pentru admin)

```bash
python manage.py createsuperuser
```

### 5. Colectează Static Files (pentru testare)

```bash
python manage.py collectstatic --noinput
```

### 6. Rulează Serverul de Dezvoltare

```bash
python manage.py runserver
```

Serverul va rula pe: **http://127.0.0.1:8000/** sau **http://localhost:8000/**

---

## 🧪 Ce să testezi

### ✅ Funcționalități de bază:
- [ ] Home page se încarcă corect
- [ ] Toate butoanele funcționează (CV, Motivation, Projects)
- [ ] Pagina de proiecte se afișează
- [ ] Detaliile proiectelor se deschid corect
- [ ] Link-urile către proiecte funcționează
- [ ] Chatbot-ul răspunde (dacă ai Rasa server pornit)

### 📱 Testare Responsive:

#### Pe Desktop:
- [ ] Design-ul arată modern și profesional
- [ ] Animațiile funcționează
- [ ] Hover effects funcționează

#### Pe Tablet (redimensionează browser-ul la ~768px):
- [ ] Layout-ul se adaptează corect
- [ ] Textul este lizibil
- [ ] Butoanele sunt accesibile

#### Pe Mobile (redimensionează browser-ul la ~480px):
- [ ] Header-ul se stivuiește vertical
- [ ] Grid-ul de proiecte devine o singură coloană
- [ ] Textul este lizibil fără zoom
- [ ] Butoanele sunt suficient de mari pentru touch
- [ ] Chatbot-ul se adaptează la ecran mic

### 🌐 Testare în Browser-uri diferite:
- [ ] Chrome/Edge
- [ ] Firefox
- [ ] Safari (dacă ai Mac)

### 🔍 Testare DevTools (F12):
- [ ] Nu există erori în Console
- [ ] Static files se încarcă corect (CSS, JS, imagini)
- [ ] Network tab: verifică că toate resursele se încarcă

---

## 📱 Testare pe Dispozitiv Real (Mobile)

### Opțiunea 1: Network Local
1. Găsește IP-ul local al computerului:
   - Windows: `ipconfig` (caută IPv4 Address)
   - Linux/Mac: `ifconfig` sau `ip addr`

2. Rulează serverul cu IP-ul tău:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

3. Pe telefon (același WiFi), accesează:
   ```
   http://IP_TU:8000
   ```
   Exemplu: `http://192.168.1.100:8000`

### Opțiunea 2: Chrome DevTools Device Mode
1. Deschide Chrome DevTools (F12)
2. Click pe iconița de device (Toggle device toolbar)
3. Selectează un device (iPhone, Samsung, etc.)
4. Testează direct în browser

---

## 🐛 Probleme comune și soluții

### Static files nu se încarcă:
```bash
python manage.py collectstatic
```

### Eroare "DisallowedHost":
Verifică că `ALLOWED_HOSTS` include `'localhost'` și `'127.0.0.1'`

### Port deja folosit:
```bash
python manage.py runserver 8001
```

### Migrații neaplicate:
```bash
python manage.py migrate
```

---

## ✅ Checklist înainte de Deploy

- [ ] Toate testele de mai sus trec
- [ ] Nu există erori în console
- [ ] Static files colectate (`python manage.py collectstatic`)
- [ ] Migrațiile sunt aplicate
- [ ] `DEBUG = False` în producție (în settings.py)
- [ ] `SECRET_KEY` este setat prin variabilă de mediu în producție
- [ ] `ALLOWED_HOSTS` include domeniul de producție

---

## 🚀 Comenzi rapide

```bash
# Activate venv + Run server (Windows PowerShell)
.\venv\Scripts\Activate.ps1; python manage.py runserver

# Activate venv + Run server (Linux/Mac)
source venv/bin/activate && python manage.py runserver
```

---

## 📝 Note

- Serverul de dezvoltare Django NU este pentru producție
- Pentru testare pe mobile real, asigură-te că telefonul și computerul sunt pe același WiFi
- Dacă ai firewall activ, poate trebui să permiți conexiuni pe portul 8000

