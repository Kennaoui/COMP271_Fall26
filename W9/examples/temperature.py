"""A tiny function to check with assert."""

FREEZING_F = 32
SCALE = 9 / 5


def to_fahrenheit(celsius: float) -> float:
    """Return the Fahrenheit value of a Celsius temperature."""
    return celsius * SCALE + FREEZING_F


# Quick checks: silent when they pass, AssertionError when they fail.
assert to_fahrenheit(0) == 32, "water freezes at 32 F"
assert to_fahrenheit(100) == 212, "water boils at 212 F"
assert to_fahrenheit(-40) == -40, "-40 is the same on both scales"
print("All temperature checks passed.")
