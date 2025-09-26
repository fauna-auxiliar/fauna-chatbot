#!/usr/bin/env bash

# Salir si hay un error
set -e

# Exportar el puerto que Render asigna
export PORT=${PORT:-10000}

# Ejecutar Gunicorn con UvicornWorker para ASGI (FastAPI)
gunicorn app:app \
    -k uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:$PORT \
    --workers 1 \
    --timeout 60
