from typing import Any, Dict

import streamlit as st

from models import FEMALE, MALE


def radios() -> Dict[str, Any]:
    sex = st.radio("Sex", [MALE, FEMALE], index=None)
    return {
        "sex": sex,
    }
