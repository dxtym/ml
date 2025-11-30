from typing import Any, Dict

import streamlit as st

from app.models.entity import FEMALE, MALE


def radios() -> Dict[str, Any]:
    sex = st.radio("Sex", [MALE, FEMALE], index=None)
    return {
        "sex": sex,
    }
