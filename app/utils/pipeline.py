from typing import List

from app.models.entity import FEMALE, MALE
from app.models.feature import Feature


def calculate_symptom_score(symptoms: List[bool]) -> float:
    return sum(1 for symptom in symptoms if symptom)

def standard_scale(values: List[float]) -> List[float]:
    if not values:
        return values
    mean = sum(values) / len(values)
    std_dev = (sum((x - mean) ** 2 for x in values) / len(values)) ** 0.5
    return [(x - mean) / std_dev if std_dev != 0 else 0 for x in values]

def convert_cat(category: str, categories: List[str]) -> int:
    print(categories)
    print(category)
    for i, cat in enumerate(categories):
        if category == cat:
            return i
    return -1

def convert_bool(value: bool) -> float:
    return 1 if value else 0

def preprocess(feature: Feature) -> List[float]:
    processed = []

    processed.append(feature.age)

    processed.extend(standard_scale([
        feature.bilirubin,
        feature.alk_phosphate,
        feature.sgot,
        feature.albumin,
        feature.protime
    ]))

    processed.append(convert_cat(feature.sex, [FEMALE, MALE]))

    processed.extend(map(convert_bool, [
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

    processed.append(calculate_symptom_score([
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
