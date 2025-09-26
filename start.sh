#!/bin/bash
# Este script arranca la app en Render usando Gunicorn con UvicornWorker
gunicorn app:app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT --workers 1 --timeout 60
