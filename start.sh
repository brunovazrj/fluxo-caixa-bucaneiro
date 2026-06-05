#!/bin/bash

# Script para iniciar o gerenciador do dashboard
# Uso: bash start.sh (ou ./start.sh se der permissão)

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Verifica se Python 3 está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado. Instale em: https://www.python.org"
    exit 1
fi

# Executa o script Python
python3 manage.py
