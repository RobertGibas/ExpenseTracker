# Expense Tracker

Aplikacja do śledzenia wydatków napisana w Django z integracją Keycloak do uwierzytelniania.

## 🚀 Funkcjonalności

- ✅ **Uwierzytelnianie** - Integracja z Keycloak (OIDC)
- ✅ **Zarządzanie wydatkami** - Dodawanie, edycja, usuwanie wydatków
- ✅ **Kategorie** - Organizacja wydatków według kategorii
- ✅ **Filtrowanie** - Filtrowanie według daty i kategorii
- ✅ **Podsumowania** - Statystyki wydatków według kategorii
- ✅ **Responsywny UI** - Bootstrap 5 z nowoczesnym interfejsem
- ✅ **Paginacja** - Wyświetlanie wydatków na stronach

## 🛠️ Technologie

- **Backend**: Django 5.0
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **Baza danych**: SQLite (development), PostgreSQL (production ready)
- **Uwierzytelnianie**: Keycloak + django-allauth
- **Containerization**: Docker + Docker Compose

## 📋 Wymagania

- Python 3.8+
- Docker i Docker Compose (dla Keycloak)
- Git

## 🚀 Instalacja i uruchomienie

### 1. Klonowanie repozytorium

```bash
git clone <repository-url>
cd expense-tracker
```

### 2. Instalacja zależności

```bash
pip install -r requirements.txt
```

### 3. Uruchomienie Keycloak

```bash
docker-compose up -d
```

### 4. Konfiguracja Keycloak

Postępuj zgodnie z instrukcjami w pliku [KEYCLOAK_SETUP.md](KEYCLOAK_SETUP.md)

### 5. Migracje bazy danych

```bash
python manage.py migrate
```

### 6. Utworzenie superusera (opcjonalne)

```bash
python manage.py createsuperuser
```

### 7. Uruchomienie serwera deweloperskiego

```bash
python manage.py runserver
```

Aplikacja będzie dostępna pod adresem: http://127.0.0.1:8000

## 📁 Struktura projektu

```
expense-tracker/
├── expense_tracker/          # Główne ustawienia Django
│   ├── settings.py           # Konfiguracja aplikacji
│   ├── urls.py              # Główne URL-e
│   └── ...
├── expenses/                 # Aplikacja wydatków
│   ├── models/              # Modele danych
│   │   ├── expense.py       # Model wydatku
│   │   └── category.py      # Model kategorii
│   ├── views.py             # Widoki
│   ├── forms.py             # Formularze
│   ├── urls.py              # URL-e aplikacji
│   └── ...
├── templates/               # Szablony HTML
│   ├── base.html           # Szablon bazowy
│   ├── expenses/           # Szablony wydatków
│   └── account/            # Szablony uwierzytelniania
├── docker-compose.yml      # Konfiguracja Keycloak
└── requirements.txt        # Zależności Python
```

## 🔧 Konfiguracja

### Zmienne środowiskowe

Dla produkcji zalecane jest użycie zmiennych środowiskowych:

```bash
export SECRET_KEY="your-secret-key"
export DEBUG=False
export ALLOWED_HOSTS="yourdomain.com,www.yourdomain.com"
```

### Baza danych

Domyślnie używana jest SQLite. Dla produkcji zalecana jest PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'expense_tracker',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🧪 Testowanie

```bash
python manage.py test
```

## 📊 Workflow Git

Projekt używa Git Flow z następującymi branchami:

- **main** - kod produkcyjny
- **develop** - kod deweloperski
- **feature/*** - nowe funkcjonalności
- **hotfix/*** - szybkie poprawki

### Przykładowe komendy:

```bash
# Praca na nowej funkcjonalności
git checkout develop
git checkout -b feature/new-feature
# ... rozwój funkcjonalności ...
git checkout develop
git merge feature/new-feature
git push origin develop

# Wersja produkcyjna
git checkout main
git merge develop
git tag v1.0.0
git push origin main --tags
```

## 🚀 Deployment

### Docker

```bash
# Build
docker build -t expense-tracker .

# Run
docker run -p 8000:8000 expense-tracker
```

### Heroku

```bash
# Instalacja Heroku CLI
# Utworzenie aplikacji
heroku create your-app-name

# Konfiguracja zmiennych środowiskowych
heroku config:set SECRET_KEY="your-secret-key"
heroku config:set DEBUG=False

# Deployment
git push heroku main
```

## 🤝 Wkład w projekt

1. Fork repozytorium
2. Utwórz branch dla nowej funkcjonalności (`git checkout -b feature/amazing-feature`)
3. Commit zmian (`git commit -m 'Add amazing feature'`)
4. Push do brancha (`git push origin feature/amazing-feature`)
5. Otwórz Pull Request

## 📝 Licencja

Ten projekt jest licencjonowany na licencji MIT - zobacz plik [LICENSE](LICENSE) dla szczegółów.

## 📞 Kontakt

Jeśli masz pytania lub sugestie, otwórz issue lub skontaktuj się z autorem.

---

**Uwaga**: To jest projekt deweloperski. Przed użyciem w produkcji upewnij się, że wszystkie ustawienia bezpieczeństwa są odpowiednio skonfigurowane.
