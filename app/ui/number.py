from typing import Any, Dict

import streamlit as st


def numbers() -> Dict[str, Any]:
    age = st.number_input("Age (years)", min_value=1, max_value=100, value=30)
    alk_phosphate = st.number_input("Alkaline Phosphate (IU/L)", min_value=30, max_value=250, value=100)
    sgot = st.number_input("SGOT (IU/L)", min_value=5, max_value=500, value=100)
    protime = st.number_input("Prothrombin Time (seconds)", min_value=5, max_value=100, value=50)
    bilirubin = st.slider("Bilirubin (mg/dL)", min_value=0.1, max_value=5.0, value=2.5)
    albumin = st.slider("Albumin (g/dL)", min_value=2.0, max_value=6.0, value=4.0)

    return {
        "age": age,
        "bilirubin": bilirubin,
        "alk_phosphate": alk_phosphate,
        "sgot": sgot,
        "albumin": albumin,
        "protime": protime,
    }
