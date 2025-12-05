import time
from pathlib import Path

import joblib
import streamlit as st
from models import Feature
from ui import checkboxes, numbers, radios
from utils import preprocess


def main() -> None:
    st.title("Hepatitis Classifier")
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
        with st.status("Please wait...") as status:
            time.sleep(3)
            prediction = model.predict([preprocessed_feature])
            if all(prediction):
                st.success("Survival likely. Keep up the good health!")
            else:
                st.warning("Risk of death. Please consult a medical professional.")
            status.update(label="Done!", state="complete", expanded=True)


if __name__ == "__main__":
    main()
