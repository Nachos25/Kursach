# Perforator — демо-магазин техніки

Темна тема, каталог з брендами/категоріями, сторінки товарів, профіль і (мок) реєстрація/вхід. Бекенд — FastAPI + SQLite + JWT (для реального режиму), фронтенд — React + Vite + Tailwind.

## Швидкий старт (Windows PowerShell)

1) Бекенд

```powershell
cd .\backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r .\requirements.txt

# створити/оновити таблиці та дані (описи + фото)
python -c "from app.seed import run; run()"

# запустити API (127.0.0.1:8000)
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

2) Фронтенд

```powershell
cd .\frontend
npm i
# dev-сервер фронта на 127.0.0.1:5175
npx vite . --host 127.0.0.1 --port 5175 --strictPort
```

Відкрийте `http://127.0.0.1:5175`.

## Що є

- Каталог: категорії, бренди, пошук, картки з ціною/знижкою
- Сторінка товару: зображення, короткий опис, повний опис
- Бренди та промо-блоки на головній
- Профіль користувача
- Мок-автентифікація на фронтенді
- Зображення товарів: підтримка локальних файлів і зовнішніх URL (через бекенд)

## Мок-логін/реєстрація

Фронтенд працює без справжнього бекенду авторизації:

- Реєстрація: зберігає користувача в `localStorage` і одразу ставить токен `demo-token` (перенаправляє на головну).
- Вхід: якщо локальний користувач збігається — ставиться `demo-token`. Є фолбек `admin / admin`.
- Профіль/Замовлення: якщо токен `demo-token`, дані беруться локально, без запиту до бекенду.

Хочете реальний режим — використовуйте бекенд‑ендпойнти з JWT (див. нижче) і приберіть мок‑код у `LoginPage.tsx`/`RegisterPage.tsx`.

## API (корисне для реального режиму)

Базова адреса: `http://127.0.0.1:8000/api` (Swagger: `http://127.0.0.1:8000/docs`)

- Каталог
  - `GET /brands` — бренди
  - `GET /categories` — категорії
  - `GET /products?q=&category=&brand=&limit=&offset=` — товари
  - `GET /products/{slug}` — товар
- Замовлення
  - `POST /orders` — створити (потрібен Bearer‑токен)
  - `GET /orders` — мої замовлення (токен)
- Аутентифікація (реальна)
  - `POST /auth/register` — реєстрація (username + пароль; email опціональний)
  - `POST /auth/login` — логін (OAuth2 password)
  - `GET /auth/me` — профіль + замовлення (токен)
  - `POST /auth/instant?username=...&password=...` — спрощена реєстрація з миттєвою видачею токена
- Статичні зображення та проксі
  - `GET /images/{filename}` — віддає локальний файл з кореня репозиторію
  - `GET /proxy?url={absolute_image_url}` — завантажує зовнішнє зображення та віддає його через бекенд

## Зображення: як це працює

- Якщо у товарі `image_url` — це абсолютний URL (починається з `http`), фронтенд звертається до бекенда на `GET /api/proxy?url=...`.
- Якщо `image_url` — це ім'я файлу (наприклад, `632446348.png`), фронтенд завантажує його з `GET /api/images/{filename}`.
- Локальні файли зображень зберігаються у корені репозиторію (поруч із `backend/` та `frontend/`). Бекенд безпечно віддає тільки файли з дозволеними розширеннями.

## Важливо

- Фронт звертається до бекенду на `http://127.0.0.1:8000/api`. За потреби можна задати `VITE_API_URL`.
- Для зображень використовується два шляхи: локальні файли через `/api/images/{filename}` та зовнішні посилання через проксі `/api/proxy?url=...`.
- Якщо картинок не видно або кеш зберіг старий код — оновіть сторінку з Ctrl+F5.

## Де правити логіку мока

- `frontend/src/pages/RegisterPage.tsx` — мок‑реєстрація (запис користувача до `localStorage` + виставлення токена)
- `frontend/src/pages/LoginPage.tsx` — мок‑логін (перевірка локального користувача або `admin/admin`)
- `frontend/src/lib/auth.ts` — `getLocalUser`/`setLocalUser`, робота з токеном
- `frontend/src/pages/ProfilePage.tsx` та `OrdersPage.tsx` — якщо токен `demo-token`, дані беруться локально

## Сід даних

`backend/app/seed.py` — бренди/категорії/товари з описами та зображеннями. Тепер підтримуються:
- локальні файли в корені репозиторію (в `image_url` вказується лише ім'я файлу, напр. `94187712-700x700.png`);
- зовнішні посилання (повний `https://...` URL).

Щоб застосувати зміни у сиді, виконайте:

```powershell
cd .\backend
.\.venv\Scripts\Activate.ps1
python -m app.seed
```

## Типові проблеми

- “Failed to fetch” на реєстрації: у мок‑режимі не повинно виникати. Якщо вмикаєте реальний режим — перевіряйте, що фронт звертається на `127.0.0.1:8000`, а не `localhost`.
- “Неавторизовано” на `/profile`: у мок‑режимі токен має бути `demo-token`. Просто перереєструйтесь/увійдіть (або `admin/admin`).

# Ябко+ Tech Store

Повноцінний демо-магазин техніки із темною темою, схожий за стилем на скріншот. Бекенд — Python FastAPI + SQLite + JWT, фронтенд — React + Vite + Tailwind.

## Швидкий старт (Windows PowerShell)

1) Запуск бекенда

```powershell
cd .\backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r .\requirements.txt

# 1-й раз — створити таблиці та залити демо-дані
python -c "from app.seed import run; run()"

# запустити API
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

API стане доступним на `http://localhost:8000`, документація — `http://localhost:8000/docs`.

2) Запуск фронтенда

```powershell
cd .\frontend
npm i
npm run dev
```

Веб застосунок відкриється на `http://localhost:5175`. За замовчуванням фронт звертається до бекенду `http://localhost:8000/api`.

## Структура

- `backend/app` — FastAPI застосунок: моделі, схеми, роутери (`auth`, `products`, `orders`), `seed.py` для демо-даних
- `frontend/src` — React застосунок: сторінки (`Login`, `Register`, `Catalog`, `Product`, `Orders`), компоненти (`Sidebar`, `Hero`, `BrandRow`, `ProductCard`)

## Облікові записи

- Зареєструйтесь на сторінці "Реєстрація" — логін видасть JWT.

## Налаштування

Змінні в `backend/app/config.py` (секрет, строк життя токена, URL SQLite).

## Prod-поради

- Замінити `secret_key` та зберігати у змінних оточення
- Використати Postgres + Alembic міграції
- Додати платежі, кошик на фронті та адмінку




