# Vibe Coding Knowledge Base

Статическая база знаний по вайб-кодингу: практические советы, QA-проверки, шаблоны промптов и примеры файлов `CLAUDE.md`.

## Сайт

После включения GitHub Pages сайт доступен по адресу:

`https://henadzipaliukhovich.github.io/vibecoding-knowledge-base/`

## Локальный запуск

```bash
python3 -m http.server 8000
```

Откройте `http://localhost:8000`.

## Обновление

```bash
git add .
git commit -m "Update knowledge base"
git push
```

Публикация запускается автоматически после push в `main`. Повторный деплой без изменения файлов: **Actions → Deploy GitHub Pages → Run workflow**.

## Структура

- `index.html` — сайт
- `CLAUDE.md` — правила для AI-агента
- `artifacts/` — переиспользуемые промпты, чек-листы и примеры
- `.github/workflows/deploy-pages.yml` — автоматический деплой
