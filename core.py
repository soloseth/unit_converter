conversions = {
    ("kg", "lb"): 2.20462,
    ("lb", "kg"): 0.453592,
    ("oz", "ml"): 29.5735,
    ("ml", "oz"): 1/29.5735,
    ("m", "ft"): 3.28084,
    ("ft", "m"): 1/3.28084,
}

conversions_in_time = {
    "ns": 1e-9,
    "us": 1e-6,
    "ms": 1e-3,
    "s": 1,
    "min": 60,
    "h": 3600,
    "d": 86400,
    "w": 604800,
    "mo": 2629800,  # 30.44 days
    "yr": 31557600,  # 365.25 days
}

for from_unit, from_factor in conversions_in_time.items():
    for to_unit, to_factor in conversions_in_time.items():
        conversions[(from_unit, to_unit)] = from_factor / to_factor

def convert(value: float, from_unit: str, to_unit: str) -> float:
    key = (from_unit.lower(), to_unit.lower())

    if key not in conversions:
        raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported.")

    return value * conversions[key]