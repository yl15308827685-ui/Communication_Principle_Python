"""
=============================================================
Communication Principle Python SDK

analysis.py

Signal Analysis Module

Python
------
3.9+

Version
-------
2.0.0
=============================================================
"""

from __future__ import annotations

from typing import Union

import numpy as np

from .models import (
    Signal,
    Spectrum,
    SignalStatistics,
    AnalysisResult,
)


ArrayLike = Union[
    Signal,
    np.ndarray,
    list,
    tuple,
]


# ============================================================
# Analyzer
# ============================================================

class Analyzer:
    """
    Signal analysis toolbox.
    """

    def __init__(self):
        pass

    # --------------------------------------------------------

    @staticmethod
    def _to_array(
        signal: ArrayLike
    ) -> np.ndarray:
        """
        Convert supported input types to numpy array.
        """

        if isinstance(signal, Signal):
            return signal.value

        return np.asarray(
            signal,
            dtype=float
        )

    # --------------------------------------------------------

    def rms(
        self,
        signal: ArrayLike
    ) -> float:
        """
        Root Mean Square.
        """

        x = self._to_array(signal)

        if x.size == 0:
            return 0.0

        return float(
            np.sqrt(
                np.mean(
                    x ** 2
                )
            )
        )

    # --------------------------------------------------------

    def mean(
        self,
        signal: ArrayLike
    ) -> float:

        x = self._to_array(signal)

        return float(
            np.mean(x)
        )

    # --------------------------------------------------------

    def variance(
        self,
        signal: ArrayLike
    ) -> float:

        x = self._to_array(signal)

        return float(
            np.var(x)
        )

    # --------------------------------------------------------

    def std(
        self,
        signal: ArrayLike
    ) -> float:

        x = self._to_array(signal)

        return float(
            np.std(x)
        )
    # --------------------------------------------------------

    def peak(
        self,
        signal: ArrayLike
    ) -> float:

        x = self._to_array(signal)

        if x.size == 0:
            return 0.0

        return float(
            np.max(
                np.abs(x)
            )
        )

    # --------------------------------------------------------

    def peak_to_peak(
        self,
        signal: ArrayLike
    ) -> float:

        x = self._to_array(signal)

        if x.size == 0:
            return 0.0

        return float(
            np.ptp(x)
        )

    # --------------------------------------------------------

    def energy(
        self,
        signal: ArrayLike
    ) -> float:

        x = self._to_array(signal)

        return float(
            np.sum(
                x ** 2
            )
        )

    # --------------------------------------------------------

    def power(
        self,
        signal: ArrayLike
    ) -> float:

        x = self._to_array(signal)

        if x.size == 0:
            return 0.0

        return float(
            np.mean(
                x ** 2
            )
        )

    # --------------------------------------------------------

    def statistics(
        self,
        signal: ArrayLike
    ) -> SignalStatistics:
        """
        Calculate common statistics.
        """

        x = self._to_array(signal)

        return SignalStatistics(

            mean=self.mean(x),

            rms=self.rms(x),

            variance=self.variance(x),

            std=self.std(x),

            peak=self.peak(x),

            peak_to_peak=self.peak_to_peak(x),

            energy=self.energy(x),

            power=self.power(x),
        )

    # --------------------------------------------------------

    def compare(
        self,
        reference: ArrayLike,
        target: ArrayLike
    ) -> AnalysisResult:
        """
        Compare two signals.
        """

        x = self._to_array(reference)

        y = self._to_array(target)

        if len(x) != len(y):

            raise ValueError(
                "Signal length mismatch."
            )

        error = x - y

        mae = np.mean(
            np.abs(error)
        )

        mse = np.mean(
            error ** 2
        )

        rmse = np.sqrt(
            mse
        )

        if np.std(x) == 0 or np.std(y) == 0:

            corr = 0.0

        else:

            corr = np.corrcoef(
                x,
                y
            )[0, 1]

        return AnalysisResult(

            mae=float(mae),

            mse=float(mse),

            rmse=float(rmse),

            correlation=float(corr),
        )
    # --------------------------------------------------------

    def fft(
        self,
        signal: ArrayLike,
        sampling_rate: float
    ) -> Spectrum:
        """
        Fast Fourier Transform.
        """

        x = self._to_array(signal)

        n = len(x)

        if n == 0:
            raise ValueError(
                "Signal is empty."
            )

        spectrum = np.fft.rfft(x)

        frequency = np.fft.rfftfreq(
            n,
            d=1.0 / sampling_rate
        )

        magnitude = np.abs(spectrum)

        phase = np.angle(spectrum)

        return Spectrum(

            frequency=frequency,

            magnitude=magnitude,

            phase=phase,
        )

    # --------------------------------------------------------

    def ifft(
        self,
        spectrum: Spectrum
    ) -> np.ndarray:
        """
        Inverse FFT.
        """

        return np.fft.irfft(
            spectrum.magnitude *
            np.exp(
                1j * spectrum.phase
            )
        )

    # --------------------------------------------------------

    def dominant_frequency(
        self,
        signal: ArrayLike,
        sampling_rate: float
    ) -> float:
        """
        Estimate dominant frequency.
        """

        spec = self.fft(
            signal,
            sampling_rate
        )

        index = np.argmax(
            spec.magnitude
        )

        return float(
            spec.frequency[index]
        )

    # --------------------------------------------------------

    def spectrum_power(
        self,
        signal: ArrayLike
    ) -> np.ndarray:
        """
        Power spectrum.
        """

        x = self._to_array(signal)

        return np.abs(
            np.fft.rfft(x)
        ) ** 2

    # --------------------------------------------------------

    def spectrum_db(
        self,
        signal: ArrayLike
    ) -> np.ndarray:
        """
        Spectrum in dB.
        """

        power = self.spectrum_power(
            signal
        )

        power = np.maximum(
            power,
            1e-12
        )

        return 10.0 * np.log10(
            power
        )

# ============================================================
# Default Analyzer
# ============================================================

_default_analyzer = Analyzer()

# ============================================================
# Backward Compatibility
# ============================================================

SignalAnalyzer = Analyzer

def analyze(signal: ArrayLike) -> SignalStatistics:
    """
    Analyze signal and return statistics.
    """
    return _default_analyzer.statistics(signal)

def snr(
    reference: ArrayLike,
    target: ArrayLike,
) -> float:
    """
    Signal-to-Noise Ratio (dB).
    """

    x = _default_analyzer._to_array(reference)
    y = _default_analyzer._to_array(target)

    noise = x - y

    signal_power = np.mean(x ** 2)
    noise_power = np.mean(noise ** 2)

    if noise_power <= 1e-20:
        return float("inf")

    return float(
        10.0 * np.log10(signal_power / noise_power)
    )

def psnr(
    reference: ArrayLike,
    target: ArrayLike,
    peak: float = 1.0,
) -> float:
    """
    Peak Signal-to-Noise Ratio (dB).
    """

    x = _default_analyzer._to_array(reference)
    y = _default_analyzer._to_array(target)

    mse = np.mean((x - y) ** 2)

    if mse <= 1e-20:
        return float("inf")

    return float(
        10.0 * np.log10((peak ** 2) / mse)
    )


# ============================================================
# Public API
# ============================================================

def rms(signal: ArrayLike) -> float:
    """
    Root Mean Square.
    """
    return _default_analyzer.rms(signal)


def mean(signal: ArrayLike) -> float:
    """
    Mean value.
    """
    return _default_analyzer.mean(signal)


def variance(signal: ArrayLike) -> float:
    """
    Variance.
    """
    return _default_analyzer.variance(signal)


def std(signal: ArrayLike) -> float:
    """
    Standard deviation.
    """
    return _default_analyzer.std(signal)


def peak(signal: ArrayLike) -> float:
    """
    Peak value.
    """
    return _default_analyzer.peak(signal)


def peak_to_peak(signal: ArrayLike) -> float:
    """
    Peak-to-peak value.
    """
    return _default_analyzer.peak_to_peak(signal)


def energy(signal: ArrayLike) -> float:
    """
    Signal energy.
    """
    return _default_analyzer.energy(signal)


def power(signal: ArrayLike) -> float:
    """
    Average power.
    """
    return _default_analyzer.power(signal)


def statistics(signal: ArrayLike) -> SignalStatistics:
    """
    Signal statistics.
    """
    return _default_analyzer.statistics(signal)


def compare(
    reference: ArrayLike,
    target: ArrayLike,
) -> AnalysisResult:
    """
    Compare two signals.
    """
    return _default_analyzer.compare(
        reference,
        target,
    )


def fft(
    signal: ArrayLike,
    sampling_rate: float,
) -> Spectrum:
    """
    FFT.
    """
    return _default_analyzer.fft(
        signal,
        sampling_rate,
    )


def ifft(
    spectrum: Spectrum,
) -> np.ndarray:
    """
    Inverse FFT.
    """
    return _default_analyzer.ifft(
        spectrum,
    )


def dominant_frequency(
    signal: ArrayLike,
    sampling_rate: float,
) -> float:
    """
    Dominant frequency.
    """
    return _default_analyzer.dominant_frequency(
        signal,
        sampling_rate,
    )


def spectrum_power(
    signal: ArrayLike,
) -> np.ndarray:
    """
    Power spectrum.
    """
    return _default_analyzer.spectrum_power(
        signal,
    )


def spectrum_db(
    signal: ArrayLike,
) -> np.ndarray:
    """
    Spectrum in dB.
    """
    return _default_analyzer.spectrum_db(
        signal,
    )

# ============================================================
# Public Export
# ============================================================

__all__ = [

    "Analyzer",
    "SignalAnalyzer",

    "analyze",

    "rms",
    "mean",
    "variance",
    "std",
    "peak",
    "peak_to_peak",
    "energy",
    "power",

    "statistics",
    "compare",

    "snr",
    "psnr",

    "fft",
    "ifft",
    "dominant_frequency",
    "spectrum_power",
    "spectrum_db",
]



