# ADR 0003 — API Style & Error Model

## Context
API для сутності Product, дотримання REST і OpenAPI.

## Decision
- REST style (GET, POST, PUT/PATCH, DELETE)
- Стандартний формат помилки `ErrorResponse`:
```json
{
  "error": "ValidationError",
  "code": "TITLE_REQUIRED",
  "details": [{"field": "title", "message": "Title is required"}]
}
