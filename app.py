import streamlit as st
import json
import os 
import subprocess
from kedro.framework.context import KedroContext

st.title("Entrer des nombres à additionner")

numbers = st.text_input("Entrez des nombres séparés par des virgules", "1,2,3,4,5")

if st.button("Enregistrer dans Kedro et calculer la somme"):
    number_list = [int(x.strip()) for x in numbers.split(",") if x.strip().isdigit()]
    data = {"numbers": number_list}
    

    # Écriture dans le fichier Kedro
    os.makedirs("data/01_raw", exist_ok=True)
    with open("data/01_raw/input_numbers.json", "w") as f:
        json.dump(data, f)

    st.success("Fichier input_numbers.json enregistré avec succès.")

    # Exécution du pipeline Kedro
    result = subprocess.run(["kedro", "run"], capture_output=True, text=True)

    if result.returncode == 0:
        st.success("Pipeline Kedro exécuté avec succès !")
    else:
        st.error("Erreur lors de l'exécution du pipeline Kedro :")
        st.text(result.stderr)