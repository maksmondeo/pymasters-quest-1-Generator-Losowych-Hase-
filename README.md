# 🔐 Generator Losowych Haseł (QUEST #1)

Prosty konsolowy generator haseł w Pythonie, działający z linii poleceń. Umożliwia tworzenie bezpiecznych haseł na podstawie preferencji użytkownika.

## ✨ Funkcje

- Generowanie losowych haseł o zadanej długości
- Opcjonalnie: dodawanie cyfr i znaków specjalnych
- Tryb hasła łatwego do zapamiętania (np. `kot-1234-dom`)
- Obsługa wielu haseł w jednej sesji
- Intuicyjna interakcja tekstowa

## 🛠️ Wymagania

- Python 3.10+
- [Poetry](https://python-poetry.org/docs/)

## 📦 Instalacja

1. Zainstaluj Poetry (jeśli jeszcze nie masz):

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Sklonuj repozytorium:

   ```bash
   git clone https://github.com/twoj-login/generator-hasel.git
   cd generator-hasel
   ```

3. Zainstaluj zależności

   ```bash
   poetry install
   ```

4. Uruchomienie
   ```bash
   poetry run python generator_hasel/main.py
   ```
