# Chatbot Bapenda API (FastAPI)

API Dashboard to manage chatbot integration for Bapenda Jakarta (2022).  
Supports message routing, agent assignment, and channel configuration (WhatsApp, Telegram, Web, FB).

## Features
- Unified interface for 160+ staff in public engagement
- Message structuring and role-based assignment
- API for human-agent fallback and user query routing

## Tech Stack
- FastAPI
- Python 3
- PostgreSQL (future integration)

## Run Locally
```bash
pip install -r requirements.txt
uvicorn main:app --reload
