#!/bin/bash

# Lancer l'application Streamlit avec le bon port pour Azure
streamlit run app.py --server.port=8000 --server.enableCORS=false