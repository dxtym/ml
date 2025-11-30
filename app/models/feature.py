from dataclasses import dataclass


@dataclass
class Feature:
    age: int
    bilirubin: float
    alk_phosphate: float
    sgot: float
    albumin: float
    protime: float
    sex: str
    steroid: bool
    antivirals: bool
    fatigue: bool
    malaise: bool
    anorexia: bool
    liver_big: bool
    liver_firm: bool
    spleen_palpable: bool
    spiders: bool
    ascites: bool
    varices: bool
    histology: bool
