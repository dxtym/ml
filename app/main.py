import joblib
import streamlit as st

from app.models.feature import Feature
from app.ui.checkbox import checkboxes
from app.ui.number import numbers
from app.ui.radio import radios
from app.utils.pipeline import preprocess


def main() -> None:
    st.title("Machine Learning Coursework")
    st.info("ID: 19248")

    model = joblib.load("model/model.pkl")

    nums = numbers()
    rads = radios()
    checks = checkboxes()

    feature = Feature(
        **nums,
        **rads,
        **checks
    )

    if st.button("Predict"):
        preprocessed_feature = preprocess(feature)
        print(preprocessed_feature)
        prediction = model.predict([preprocessed_feature])

        st.success(f"Prediction: {prediction[0]}")


if __name__ == "__main__":
    main()
