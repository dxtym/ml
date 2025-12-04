from typing import Any, Dict

import streamlit as st


def numbers() -> Dict[str, Any]:
    age = st.number_input("Age", min_value=1, max_value=100, value=30)
    bilirubin = st.slider("Bilirubin", min_value=0.0, value=1.0)
    alk_phosphate = st.slider("Alk Phosphate", min_value=0.0, value=100.0)
    sgot = st.slider("SGOT", min_value=0.0, value=30.0)
    albumin = st.slider("Albumin", min_value=0.0, value=3.5)
    protime = st.number_input("Protime", min_value=0.0, value=12.0)

    return {
        "age": age,
        "bilirubin": bilirubin,
        "alk_phosphate": alk_phosphate,
        "sgot": sgot,
        "albumin": albumin,
        "protime": protime,
    }
