
from pathlib import Path

import joblib
import streamlit as st
from models import Feature
from ui import checkboxes, numbers, radios
from utils import preprocess


def main() -> None:
    st.title("Machine Learning Coursework")
    st.info("ID: 19248")

    path = Path(__file__).resolve()
    model_path = path.parent.parent / "model" / "model.pkl"

    if model_path.exists():
        model = joblib.load(model_path)
    else:
        raise FileNotFoundError(f"Model not found at {model_path}")

    nums = numbers()
    rads = radios()
    checks = checkboxes()

    feature = Feature(
        **nums,
        **rads,
        **checks
    )

    st.divider()
    btn = st.button("Predict")

    if btn:
        preprocessed_feature = preprocess(feature)
        with st.spinner("Please wait..."):
            prediction = model.predict([preprocessed_feature])

        if all(prediction):
            st.success("Survival likely.")
        else:
            st.warning("Risk of death.")


if __name__ == "__main__":
    main()
