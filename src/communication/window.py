"""
============================================================
Communication_Principle_Python

Window Functions

Version
-------
1.0.0

Description
-----------
Standard DSP window functions.

Author
------
Communication_Principle_Python Textbook Project
============================================================
"""

from __future__ import annotations

import numpy as np

from .models import Signal

__all__ = [

    "rectangular",

    "hann",

    "hamming",

    "blackman",

    "apply_window",

]

# ============================================================
# Rectangular Window
# ============================================================

def rectangular(
    length: int,
) -> np.ndarray:
    """
    Generate rectangular window.
    """

    return np.ones(
        length,
        dtype=float,
    )

# ============================================================
# Hann Window
# ============================================================

def hann(
    length: int,
) -> np.ndarray:
    """
    Generate Hann window.
    """

    return np.hanning(
        length,
    )

# ============================================================
# Hamming Window
# ============================================================

def hamming(
    length: int,
) -> np.ndarray:
    """
    Generate Hamming window.
    """

    return np.hamming(
        length,
    )

# ============================================================
# Blackman Window
# ============================================================

def blackman(
    length: int,
) -> np.ndarray:
    """
    Generate Blackman window.
    """

    return np.blackman(
        length,
    )

# ============================================================
# Window Dispatcher
# ============================================================

def _get_window(
    name: str,
    length: int,
) -> np.ndarray:
    """
    Return window coefficients.
    """

    name = name.lower()

    if name == "rectangular":

        return rectangular(length)

    if name == "hann":

        return hann(length)

    if name == "hamming":

        return hamming(length)

    if name == "blackman":

        return blackman(length)

    raise ValueError(

        f"Unsupported window: {name}"

    )

# ============================================================
# Apply Window
# ============================================================

def apply_window(
    signal: Signal,
    window: str = "hann",
) -> Signal:
    """
    Apply a window function to a signal.

    Parameters
    ----------
    signal : Signal
        Input signal.

    window : str
        Window type.

        Supported:

        - rectangular
        - hann
        - hamming
        - blackman

    Returns
    -------
    Signal
        Windowed signal.
    """

    coefficients = _get_window(

        window,

        len(signal),

    )

    result = signal.copy()

    result.value = result.value * coefficients

    result.name = f"{signal.name} [{window}]"

    result.info["window"] = window

    return result

# ============================================================
# Supported Windows
# ============================================================

def supported_windows() -> list[str]:
    """
    Return supported window names.
    """

    return [

        "rectangular",

        "hann",

        "hamming",

        "blackman",

    ]

# ============================================================
# Self Test
# ============================================================

if __name__ == "__main__":

    from .config import DEFAULT_CONFIG

    from .signals import SignalGenerator

    generator = SignalGenerator(

        DEFAULT_CONFIG,

    )

    signal = generator.sine()

    for window in supported_windows():

        new_signal = apply_window(

            signal,

            window,

        )

        print(

            window,

            len(new_signal),

            new_signal.info["window"],

        )

