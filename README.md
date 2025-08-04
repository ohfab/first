# Context-Based Language Learning App

This repository contains a basic scaffold for a location-aware language learning application.

## Directory Structure

- `backend/` – WSGI application that serves context-specific vocabulary.
- `frontend/` – Placeholder for web-based user interfaces.
- `mobile/` – Placeholder for mobile application code.
- `docs/` – Documentation and project planning materials.
- `tests/` – Test suites for the project.

## Backend Prototype

A minimal WSGI server exposes a `/vocab` endpoint that returns vocabulary for a given context.

```bash
python backend/app.py
# then in another terminal
curl 'http://127.0.0.1:8000/vocab?context=cafe'
```

The vocabulary data is currently hard coded for demo purposes.
