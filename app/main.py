import joblib
import streamlit as st

from app.models.feature import Feature
from app.utils.pipeline import preprocess


def main():
    st.title("Machine Learning Coursework")
    st.info("ID: 19248")

    model = joblib.load("model/model.pkl")

    age = st.number_input("Age", min_value=1, value=30)
    bilirubin = st.number_input("Bilirubin", min_value=0.0, value=1.0)
    alk_phosphate = st.number_input("Alk Phosphate", min_value=0.0, value=100.0)
    sgot = st.number_input("SGOT", min_value=0.0, value=30.0)
    albumin = st.number_input("Albumin", min_value=0.0, value=3.5)
    protime = st.number_input("Protime", min_value=0.0, value=12.0)

    sex = st.radio("Sex", ["Male", "Female"], index=None)

    steroid = st.checkbox("Steroid")
    antivirals = st.checkbox("Antivirals")
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

    feature = Feature(
        age=age,
        bilirubin=bilirubin,
        alk_phosphate=alk_phosphate,
        sgot=sgot,
        albumin=albumin,
        protime=protime,
        sex=sex,
        steroid=steroid,
        antivirals=antivirals,
        fatigue=fatigue,
        malaise=malaise,
        anorexia=anorexia,
        liver_big=liver_big,
        liver_firm=liver_firm,
        spleen_palpable=spleen_palpable,
        spiders=spiders,
        ascites=ascites,
        varices=varices,
        histology=histology,
    )

    if st.button("Predict"):
        preprocessed_feature = preprocess(feature)
        prediction = model.predict([preprocessed_feature])

        st.success(f"Prediction: {prediction[0]}")


if __name__ == "__main__":
    main()
