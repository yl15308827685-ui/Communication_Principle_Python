"""
==========================================================
Communication_Principle_Python

File:
    analysis.py

Version:
    1.0.0

Description:
    Signal Analysis Module

Python:
    >=3.9

==========================================================
"""

from __future__ import annotations

from typing import Optional

import numpy as np

from .models import Signal
from .models import SignalStatistics
from .models import AnalysisResult


# ==========================================================
# Signal Analyzer
# ==========================================================

class SignalAnalyzer:
    """
    Time-domain signal analyzer.

    This class provides statistical analysis
    for communication signals.

    Examples
    --------

    >>> analyzer = SignalAnalyzer()

    >>> statistics = analyzer.analyze(signal)
    """

    def analyze(
        self,
        signal: Signal,
    ) -> SignalStatistics:
        """
        Analyze a signal.

        Parameters
        ----------
        signal
            Input signal.

        Returns
        -------
        SignalStatistics
        """

        return analyze(signal)

    def compare(
        self,
        signal1: Signal,
        signal2: Signal,
    ) -> AnalysisResult:
        """
        Compare two signals.

        Parameters
        ----------
        signal1
            First signal.

        signal2
            Second signal.

        Returns
        -------
        AnalysisResult
        """

        return compare(
            signal1,
            signal2,
        )


# ==========================================================
# Internal Helper
# ==========================================================

def _check_signal(
    signal: Signal,
) -> None:
    """
    Validate Signal object.
    """

    if not isinstance(
        signal,
        Signal,
    ):

        raise TypeError(
            "signal must be a Signal object."
        )

    if signal.samples == 0:

        raise ValueError(
            "empty signal."
        )


# ==========================================================
# Mean
# ==========================================================

def mean(
    signal: Signal,
) -> float:
    """
    Calculate signal mean.
    """

    _check_signal(signal)

    return float(
        np.mean(
            signal.value
        )
    )


# ==========================================================
# Maximum
# ==========================================================

def maximum(
    signal: Signal,
) -> float:
    """
    Calculate maximum value.
    """

    _check_signal(signal)

    return float(
        np.max(
            signal.value
        )
    )


# ==========================================================
# Minimum
# ==========================================================

def minimum(
    signal: Signal,
) -> float:
    """
    Calculate minimum value.
    """

    _check_signal(signal)

    return float(
        np.min(
            signal.value
        )
    )


# ==========================================================
# RMS
# ==========================================================

def rms(
    signal: Signal,
) -> float:
    """
    Calculate RMS value.
    """

    _check_signal(signal)

    return float(

        np.sqrt(

            np.mean(

                signal.value ** 2

            )

        )

    )


# ==========================================================
# Variance
# ==========================================================

def variance(
    signal: Signal,
) -> float:
    """
    Calculate variance.
    """

    _check_signal(signal)

    return float(

        np.var(

            signal.value

        )

    )


# ==========================================================
# Standard Deviation
# ==========================================================

def standard_deviation(
    signal: Signal,
) -> float:
    """
    Calculate standard deviation.
    """

    _check_signal(signal)

    return float(

        np.std(

            signal.value

        )

    )
# ==========================================================
# Peak-to-Peak
# ==========================================================

def peak_to_peak(
    signal: Signal,
) -> float:
    """
    Calculate peak-to-peak value.

    Parameters
    ----------
    signal
        Input signal.

    Returns
    -------
    float
        Peak-to-peak value.
    """

    _check_signal(signal)

    return float(

        np.ptp(

            signal.value

        )

    )


# ==========================================================
# Crest Factor
# ==========================================================

def crest_factor(
    signal: Signal,
) -> float:
    """
    Calculate crest factor.

    Crest Factor = Peak / RMS

    Parameters
    ----------
    signal
        Input signal.

    Returns
    -------
    float
        Crest factor.
    """

    _check_signal(signal)

    rms_value = rms(signal)

    if rms_value == 0:

        return 0.0

    peak = np.max(

        np.abs(

            signal.value

        )

    )

    return float(

        peak / rms_value

    )


# ==========================================================
# Energy
# ==========================================================

def energy(
    signal: Signal,
) -> float:
    """
    Calculate signal energy.

    Parameters
    ----------
    signal
        Input signal.

    Returns
    -------
    float
        Signal energy.
    """

    _check_signal(signal)

    return float(

        np.sum(

            signal.value ** 2

        )

    )


# ==========================================================
# Average Power
# ==========================================================

def average_power(
    signal: Signal,
) -> float:
    """
    Calculate average power.

    Parameters
    ----------
    signal
        Input signal.

    Returns
    -------
    float
        Average power.
    """

    _check_signal(signal)

    return float(

        np.mean(

            signal.value ** 2

        )

    )


# ==========================================================
# Analyze
# ==========================================================

def analyze(
    signal: Signal,
) -> SignalStatistics:
    """
    Analyze a signal.

    Parameters
    ----------
    signal
        Input signal.

    Returns
    -------
    SignalStatistics
        Signal statistics.
    """

    _check_signal(signal)

    return SignalStatistics(

        mean=mean(signal),

        rms=rms(signal),

        variance=variance(signal),

        std=standard_deviation(signal),

        peak=maximum(signal),

        peak_to_peak=peak_to_peak(signal),

        energy=energy(signal),

        power=average_power(signal),

    )

# ==========================================================
# Mean Absolute Error
# ==========================================================

def mae(
    signal1: Signal,
    signal2: Signal,
) -> float:
    """
    Calculate Mean Absolute Error (MAE).

    Parameters
    ----------
    signal1
        First signal.

    signal2
        Second signal.

    Returns
    -------
    float
        Mean absolute error.
    """

    _check_signal(signal1)
    _check_signal(signal2)

    if signal1.samples != signal2.samples:

        raise ValueError(
            "signal length mismatch."
        )

    return float(

        np.mean(

            np.abs(

                signal1.value -
                signal2.value

            )

        )

    )


# ==========================================================
# Mean Squared Error
# ==========================================================

def mse(
    signal1: Signal,
    signal2: Signal,
) -> float:
    """
    Calculate Mean Squared Error (MSE).
    """

    _check_signal(signal1)
    _check_signal(signal2)

    if signal1.samples != signal2.samples:

        raise ValueError(
            "signal length mismatch."
        )

    return float(

        np.mean(

            (

                signal1.value -
                signal2.value

            ) ** 2

        )

    )


# ==========================================================
# Root Mean Squared Error
# ==========================================================

def rmse(
    signal1: Signal,
    signal2: Signal,
) -> float:
    """
    Calculate Root Mean Squared Error (RMSE).
    """

    return float(

        np.sqrt(

            mse(
                signal1,
                signal2,
            )

        )

    )


# ==========================================================
# Correlation
# ==========================================================

def correlation(
    signal1: Signal,
    signal2: Signal,
) -> float:
    """
    Calculate Pearson correlation coefficient.
    """

    _check_signal(signal1)
    _check_signal(signal2)
    if np.std(signal1.value) == 0:
        return 0.0

    if np.std(signal2.value) == 0:
        return 0.0

    if signal1.samples != signal2.samples:

        raise ValueError(
            "signal length mismatch."
        )

    coefficient = np.corrcoef(

        signal1.value,

        signal2.value,

    )[0, 1]

    return float(
        coefficient
    )


# ==========================================================
# Auto Correlation
# ==========================================================

def auto_correlation(
    signal: Signal,
) -> np.ndarray:
    """
    Calculate auto correlation.
    Returns
    -------
    numpy.ndarray
    Correlation sequence.
    """

    _check_signal(signal)

    return np.correlate(

        signal.value,

        signal.value,

        mode="full",

    )


# ==========================================================
# Cross Correlation
# ==========================================================

def cross_correlation(
    signal1: Signal,
    signal2: Signal,
) -> np.ndarray:
    """
    Calculate cross correlation.
    Returns
    -------
    numpy.ndarray
      Correlation sequence.
    """

    _check_signal(signal1)
    _check_signal(signal2)
    if signal1.samples != signal2.samples:
        raise ValueError(
            "signal length mismatch."
        )

    return np.correlate(

        signal1.value,

        signal2.value,

        mode="full",

    )


# ==========================================================
# Compare
# ==========================================================

def compare(
    signal1: Signal,
    signal2: Signal,
) -> AnalysisResult:
    """
    Compare two signals.

    Parameters
    ----------
    signal1
        First signal.

    signal2
        Second signal.

    Returns
    -------
    AnalysisResult
    """

    return AnalysisResult(

        mae=mae(
            signal1,
            signal2,
        ),

        mse=mse(
            signal1,
            signal2,
        ),

        rmse=rmse(
            signal1,
            signal2,
        ),

        correlation=correlation(
            signal1,
            signal2,
        ),

    )


# ==========================================================
# Public API
# ==========================================================

__all__ = [

    "SignalAnalyzer",

    "analyze",
    "compare",

    "mean",
    "maximum",
    "minimum",

    "rms",

    "variance",
    "standard_deviation",

    "peak_to_peak",
    "crest_factor",

    "energy",
    "average_power",

    "mae",
    "mse",
    "rmse",

    "correlation",

    "auto_correlation",
    "cross_correlation",
]

