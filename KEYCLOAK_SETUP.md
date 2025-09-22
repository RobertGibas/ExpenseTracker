# Konfiguracja Keycloak dla Expense Tracker

## Opcja 1: Docker (zalecana)

### 1) Uruchom Docker Desktop
- Zainstaluj Docker Desktop z https://www.docker.com/products/docker-desktop
- Uruchom Docker Desktop i poczekaj aż będzie gotowy

### 2) Uruchom Keycloak
```powershell
docker-compose up -d
```

### 3) Sprawdź czy działa
- Otwórz przeglądarkę: http://localhost:8080
- Powinieneś zobaczyć stronę logowania Keycloak

## Opcja 2: Bezpośrednie pobranie

### 1) Pobierz Keycloak
- Idź na: https://www.keycloak.org/downloads
- Pobierz "Keycloak 23.0" (ZIP)
- Rozpakuj do katalogu (np. C:\keycloak)

### 2) Uruchom Keycloak
```powershell
cd C:\keycloak
bin\kc.bat start-dev --http-port=8080
```

## Konfiguracja Keycloak

### 1) Wejdź na panel admina
- URL: http://localhost:8080/admin
- Login: `admin`
- Hasło: `admin123`

### 2) Utwórz nowy Realm
1. Kliknij dropdown w lewym górnym rogu (Master)
2. Kliknij "Create Realm"
3. Name: `expense-tracker`
4. Enabled: ON
5. Kliknij "Create"

### 3) Utwórz klienta aplikacji
1. W lewym menu: "Clients" → "Create"
2. Client ID: `expense-tracker-app`
3. Client Protocol: `openid-connect`
4. Root URL: `http://127.0.0.1:8000`
5. Kliknij "Save"

### 4) Skonfiguruj klienta
W zakładce "Settings":
- Access Type: `confidential`
- Standard Flow Enabled: ON
- Direct Access Grants Enabled: ON
- Valid Redirect URIs: `http://127.0.0.1:8000/accounts/openid_connect/keycloak/login/callback/`
- Web Origins: `http://127.0.0.1:8000`
- Kliknij "Save"

### 5) Skopiuj Client Secret
1. W zakładce "Credentials"
2. Skopiuj "Secret"
3. Wklej do `expense_tracker/settings.py` w linii 161:
   ```python
   'secret': 'WKLEJ_TUTAJ_SECRET',
   ```

### 6) Utwórz użytkownika testowego
1. W lewym menu: "Users" → "Add user"
2. Username: `testuser`
3. Email: `test@example.com`
4. First Name: `Test`
5. Last Name: `User`
6. Email Verified: ON
7. Enabled: ON
8. Kliknij "Save"

9. W zakładce "Credentials":
   - Kliknij "Set Password"
   - Password: `testpass123`
   - Temporary: OFF
   - Kliknij "Save"

## Test aplikacji

1. Uruchom Django:
```powershell
python manage.py runserver
```

2. Wejdź na: http://127.0.0.1:8000/accounts/login/
3. Kliknij "Zaloguj przez Keycloak"
4. Zaloguj się jako `testuser` / `testpass123`
5. Powinieneś zostać przekierowany z powrotem do aplikacji

## Rozwiązywanie problemów

### Keycloak nie uruchamia się
- Sprawdź czy port 8080 jest wolny
- Uruchom jako administrator

### Błąd "Invalid redirect URI"
- Sprawdź czy URL w Keycloak dokładnie pasuje do Django
- Upewnij się, że nie ma `/` na końcu

### Błąd "Client secret mismatch"
- Skopiuj dokładnie secret z Keycloak
- Sprawdź czy nie ma dodatkowych spacji

