#! /bin/bash

if [[ -z "$VIRTUAL_ENV" ]]; then
    python3 -m venv venv
    source venv/bin/activate
    
    if [[ -e "./requirements.txt" ]]; then
        pip install -r requirements.txt
    fi
fi