from typing import Any, Dict

import streamlit as st


def checkboxes() -> Dict[str, Any]:
    st.markdown('<small>Medications:</small>', unsafe_allow_html=True)
    steroid = st.checkbox("Steroid")
    antivirals = st.checkbox("Antivirals")

    st.markdown('<small>Symptoms:</small>', unsafe_allow_html=True)
    fatigue = st.checkbox("Fatigue")
    malaise = st.checkbox("Malaise")
    anorexia = st.checkbox("Anorexia")
    liver_big = st.checkbox("Liver Big")
    liver_firm = st.checkbox("Liver Firm")
    spleen_palpable = st.checkbox("Spleen Palpable")
    spiders = st.checkbox("Spiders")
    ascites = st.checkbox("Ascites")
    varices = st.checkbox("Varices")
    histology = st.checkbox("Histology")

    return {
        "steroid": steroid,
        "antivirals": antivirals,
        "fatigue": fatigue,
        "malaise": malaise,
        "anorexia": anorexia,
        "liver_big": liver_big,
        "liver_firm": liver_firm,
        "spleen_palpable": spleen_palpable,
        "spiders": spiders,
        "ascites": ascites,
        "varices": varices,
        "histology": histology,
    }
