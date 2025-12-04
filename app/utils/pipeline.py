from typing import List

from models.entity import FEMALE, MALE
from models.feature import Feature


def _calculate_symptom_score(symptoms: List[bool]) -> float:
    return sum(1 for symptom in symptoms if symptom)

def _standard_scale(values: List[float]) -> List[float]:
    if not values:
        return values
    mean = sum(values) / len(values)
    std_dev = (sum((x - mean) ** 2 for x in values) / len(values)) ** 0.5
    return [(x - mean) / std_dev if std_dev != 0 else 0 for x in values]

def _convert_cat(category: str, categories: List[str]) -> int:
    for i, cat in enumerate(categories):
        if category == cat:
            return i
    return -1

def _convert_bool(value: bool) -> float:
    return 1 if value else 0

def preprocess(feature: Feature) -> List[float]:
    processed = []

    processed.append(feature.age)

    processed.extend(_standard_scale([
        feature.bilirubin,
        feature.alk_phosphate,
        feature.sgot,
        feature.albumin,
        feature.protime
    ]))

    processed.append(_convert_cat(feature.sex, [FEMALE, MALE]))

    processed.extend(map(_convert_bool, [
        feature.steroid,
        feature.antivirals,
        feature.fatigue,
        feature.malaise,
        feature.anorexia,
        feature.liver_big,
        feature.liver_firm,
        feature.spleen_palpable,
        feature.spiders,
        feature.ascites,
        feature.varices,
        feature.histology
    ]))

    processed.append(_calculate_symptom_score([
        feature.fatigue,
        feature.malaise,
        feature.anorexia,
        feature.liver_big,
        feature.liver_firm,
        feature.spleen_palpable,
        feature.spiders,
        feature.ascites,
        feature.varices
    ]))

    return processed
