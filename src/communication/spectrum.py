"""
==========================================================
Communication_Principle_Python

File:
    spectrum.py

Version:
    1.2.0

Description:
    Spectrum Analysis Module

Python:
    >=3.9

==========================================================
"""

from __future__ import annotations

from typing import Optional


import numpy as np

from .models import Signal
from .models import Spectrum


# ==========================================================
# Spectrum Analyzer
# ==========================================================

class SpectrumAnalyzer:
    """
    Frequency-domain spectrum analyzer.

    This class provides FFT-based spectrum analysis
    for communication signals.

    Examples
    --------

    >>> from communication import SignalGenerator
    >>> generator = SignalGenerator()
    >>> signal = generator.sine()
    >>> analyzer = SpectrumAnalyzer()
    >>> spectrum = analyzer.fft(signal)
    >>> print(spectrum.peak_frequency)
    """

    def __init__(
        self,
        fft_points: Optional[int] = None,
    ):
        """
        Parameters
        ----------
        fft_points
            FFT length.
            If None, signal length is used.
        """

        self.fft_points = fft_points

    # ======================================================
    # FFT
    # ======================================================

    def fft(
        self,
        signal: Signal,
    ) -> Spectrum:
        """
        Compute FFT spectrum.

        Parameters
        ----------
        signal
            Input signal.

        Returns
        -------
        Spectrum
        """

        return fft(
            signal,
            fft_points=self.fft_points,
        )

    # ======================================================
    # IFFT
    # ======================================================

    def ifft(
        self,
        spectrum: Spectrum,
    ) -> Signal:
        """
        Compute inverse FFT.

        Parameters
        ----------
        spectrum
            Input spectrum.

        Returns
        -------
        Signal
        """

        return ifft(spectrum)

# ==========================================================
# FFT
# ==========================================================

def fft(
    signal: Signal,
    fft_points: Optional[int] = None,
) -> Spectrum:
    """
    Compute Fast Fourier Transform.

    Parameters
    ----------
    signal
        Input signal.

    fft_points
        FFT length.
        If None, use the signal length.

    Returns
    -------
    Spectrum
    """

    complex_value = _fft(
        signal,
        fft_points=fft_points,
    )

    return _build_spectrum(

        complex_value=complex_value,

        sampling_rate=signal.sampling_rate,
    )

# ==========================================================
# IFFT
# ==========================================================

def ifft(
    spectrum: Spectrum,
) -> Signal:
    """
    Compute inverse Fast Fourier Transform.

    Parameters
    ----------
    spectrum
        Input spectrum.

    Returns
    -------
    Signal
        Time-domain signal reconstructed from the spectrum.
    """

    if not isinstance(spectrum, Spectrum):
        raise TypeError(
            "spectrum must be a Spectrum object."
        )

    value = np.fft.ifft(
        spectrum.complex_value
    )

    return Signal(

        value=np.real(value),

        sampling_rate=spectrum.sampling_rate,

        name="Reconstructed Signal",
    )

# ==========================================================
# Internal Utilities
# ==========================================================

def _build_spectrum(
    complex_value: np.ndarray,
    sampling_rate: float,
) -> Spectrum:
    """
    Build a Spectrum object from FFT complex values.

    Parameters
    ----------
    complex_value
        FFT complex spectrum.

    sampling_rate
        Sampling frequency.

    Returns
    -------
    Spectrum
    """

    complex_value = np.asarray(
        complex_value,
        dtype=complex,
    )

    n = len(complex_value)

    frequency = np.fft.fftfreq(
        n,
        d=1.0 / sampling_rate,
    )

    magnitude = np.abs(
        complex_value
    )

    phase = np.angle(
        complex_value
    )

    return Spectrum(

        frequency=frequency,

        magnitude=magnitude,

        phase=phase,

        complex_value=complex_value,

        sampling_rate=sampling_rate,
    )

# ==========================================================
# Internal FFT
# ==========================================================

def _fft(
    signal: Signal,
    fft_points: Optional[int] = None,
) -> np.ndarray:
    """
    Compute FFT and return complex spectrum only.

    This internal function is used by other spectrum
    processing utilities.

    Parameters
    ----------
    signal
        Input signal.

    fft_points
        FFT length.

    Returns
    -------
    numpy.ndarray
        Complex FFT spectrum.
    """

    if not isinstance(signal, Signal):
        raise TypeError(
            "signal must be a Signal object."
        )

    n = fft_points

    if n is None:
        n = signal.samples

    if n <= 0:
        raise ValueError(
            "fft_points must be positive."
        )

    return np.fft.fft(
        signal.value,
        n=n,
    )

# ==========================================================
# Frequency Axis
# ==========================================================

def frequency_axis(
    sampling_rate: float,
    fft_points: int,
) -> np.ndarray:
    """
    Generate FFT frequency axis.

    Parameters
    ----------
    sampling_rate
        Sampling frequency.

    fft_points
        FFT length.

    Returns
    -------
    numpy.ndarray
        Frequency axis.
    """

    if sampling_rate <= 0:

        raise ValueError(
            "sampling_rate must be positive."
        )

    if fft_points <= 0:

        raise ValueError(
            "fft_points must be positive."
        )

    return np.fft.fftfreq(

        fft_points,

        d=1.0 / sampling_rate,

    )


# ==========================================================
# FFT Resolution
# ==========================================================

def frequency_resolution(
    sampling_rate: float,
    fft_points: int,
) -> float:
    """
    Calculate FFT frequency resolution.

    Parameters
    ----------
    sampling_rate
        Sampling frequency.

    fft_points
        FFT length.

    Returns
    -------
    float
        Frequency resolution (Hz).
    """

    if sampling_rate <= 0:

        raise ValueError(
            "sampling_rate must be positive."
        )

    if fft_points <= 0:

        raise ValueError(
            "fft_points must be positive."
        )

    return sampling_rate / fft_points


# ==========================================================
# Nyquist Frequency
# ==========================================================

def nyquist_frequency(
    sampling_rate: float,
) -> float:
    """
    Calculate Nyquist frequency.

    Parameters
    ----------
    sampling_rate
        Sampling frequency.

    Returns
    -------
    float
        Nyquist frequency.
    """

    if sampling_rate <= 0:

        raise ValueError(
            "sampling_rate must be positive."
        )

    return sampling_rate / 2.0

# ==========================================================
# FFT Shift
# ==========================================================

def fftshift(
    spectrum: Spectrum,
) -> Spectrum:
    """
    Shift the zero-frequency component to the center.

    Parameters
    ----------
    spectrum
        Input spectrum.

    Returns
    -------
    Spectrum
        Shifted spectrum.
    """

    if not isinstance(spectrum, Spectrum):

        raise TypeError(
            "spectrum must be a Spectrum object."
        )

    return Spectrum(

        frequency=np.fft.fftshift(
            spectrum.frequency
        ),

        magnitude=np.fft.fftshift(
            spectrum.magnitude
        ),

        phase=np.fft.fftshift(
            spectrum.phase
        ),

        complex_value=np.fft.fftshift(
            spectrum.complex_value
        ),

        sampling_rate=spectrum.sampling_rate,
    )


# ==========================================================
# Inverse FFT Shift
# ==========================================================

def ifftshift(
    spectrum: Spectrum,
) -> Spectrum:
    """
    Undo fftshift().

    Parameters
    ----------
    spectrum
        Shifted spectrum.

    Returns
    -------
    Spectrum
    """

    if not isinstance(spectrum, Spectrum):

        raise TypeError(
            "spectrum must be a Spectrum object."
        )

    return Spectrum(

        frequency=np.fft.ifftshift(
            spectrum.frequency
        ),

        magnitude=np.fft.ifftshift(
            spectrum.magnitude
        ),

        phase=np.fft.ifftshift(
            spectrum.phase
        ),

        complex_value=np.fft.ifftshift(
            spectrum.complex_value
        ),

        sampling_rate=spectrum.sampling_rate,
    )

# ==========================================================
# Single-Side Spectrum
# ==========================================================

def single_side(
    spectrum: Spectrum,
) -> Spectrum:
    """
    Convert a double-side spectrum to a single-side spectrum.

    Parameters
    ----------
    spectrum
        Double-side spectrum.

    Returns
    -------
    Spectrum
        Single-side spectrum.
    """

    if not isinstance(spectrum, Spectrum):

        raise TypeError(
            "spectrum must be a Spectrum object."
        )

    n = spectrum.bins

    if n < 2:

        return spectrum.copy()

    half = n // 2 + 1

    frequency = spectrum.frequency[:half].copy()

    magnitude = spectrum.magnitude[:half].copy()

    phase = spectrum.phase[:half].copy()

    complex_value = spectrum.complex_value[:half].copy()

    if half > 2:

        magnitude[1:-1] *= 2.0

        complex_value[1:-1] *= 2.0

    return Spectrum(

        frequency=frequency,

        magnitude=magnitude,

        phase=phase,

        complex_value=complex_value,

        sampling_rate=spectrum.sampling_rate,
    )

# ==========================================================
# Double-Side Spectrum
# ==========================================================

def double_side(
    spectrum: Spectrum,
) -> Spectrum:
    """
    Convert a spectrum to double-side form.

    Parameters
    ----------
    spectrum
        Input spectrum.

    Returns
    -------
    Spectrum
        Double-side spectrum.
    """

    if not isinstance(spectrum, Spectrum):

        raise TypeError(
            "spectrum must be a Spectrum object."
        )

    # Already a double-side spectrum
    if np.any(
        spectrum.frequency < 0
    ):
        return spectrum.copy()

    frequency = spectrum.frequency

    magnitude = spectrum.magnitude

    phase = spectrum.phase

    complex_value = spectrum.complex_value

    if len(frequency) < 2:
        return spectrum.copy()

    frequency_negative = -frequency[-2:0:-1]

    magnitude_negative = (
        magnitude[-2:0:-1] / 2.0
    )

    phase_negative = (
        -phase[-2:0:-1]
    )

    complex_negative = np.conj(
        complex_value[-2:0:-1] / 2.0
    )

    frequency = np.concatenate(

        (
            frequency_negative,

            frequency,
        )

    )

    magnitude = np.concatenate(

        (
            magnitude_negative,

            magnitude,
        )

    )

    phase = np.concatenate(

        (
            phase_negative,

            phase,
        )

    )

    complex_value = np.concatenate(

        (
            complex_negative,

            complex_value,
        )

    )

    return Spectrum(

        frequency=frequency,

        magnitude=magnitude,

        phase=phase,

        complex_value=complex_value,

        sampling_rate=spectrum.sampling_rate,
    )

# ==========================================================
# Amplitude Spectrum
# ==========================================================

def amplitude_spectrum(
    spectrum: Spectrum,
) -> Spectrum:
    """
    Get amplitude spectrum.

    Parameters
    ----------
    spectrum
        Input spectrum.

    Returns
    -------
    Spectrum
        Amplitude spectrum.
    """

    if not isinstance(
        spectrum,
        Spectrum,
    ):

        raise TypeError(
            "spectrum must be a Spectrum object."
        )

    return Spectrum(

        frequency=spectrum.frequency.copy(),

        magnitude=spectrum.magnitude.copy(),

        phase=np.zeros_like(
            spectrum.phase
        ),

        complex_value=spectrum.magnitude.astype(
            complex
        ),

        sampling_rate=spectrum.sampling_rate,
    )

# ==========================================================
# Power Spectrum
# ==========================================================

def power_spectrum(
    spectrum: Spectrum,
    normalize: bool = False,
) -> Spectrum:
    """
    Compute the power spectrum.

    Parameters
    ----------
    spectrum
        Input spectrum.

    normalize
        Whether to normalize by FFT length.

    Returns
    -------
    Spectrum
        Power spectrum.
    """

    if not isinstance(
        spectrum,
        Spectrum,
    ):

        raise TypeError(
            "spectrum must be a Spectrum object."
        )

    power = (
        np.abs(
            spectrum.complex_value
        ) ** 2
    )

    if normalize:

        n = len(
            spectrum.complex_value
        )

        if n > 0:

            power = power / n

    return Spectrum(

        frequency=spectrum.frequency.copy(),

        magnitude=power,

        phase=np.zeros_like(
            spectrum.phase
        ),

        complex_value=power.astype(
            complex
        ),

        sampling_rate=spectrum.sampling_rate,
    )

# ==========================================================
# Phase Spectrum
# ==========================================================

def phase_spectrum(
    spectrum: Spectrum,
    unwrap: bool = False,
) -> Spectrum:
    """
    Compute the phase spectrum.

    Parameters
    ----------
    spectrum
        Input spectrum.

    unwrap
        Whether to unwrap the phase.

    Returns
    -------
    Spectrum
        Phase spectrum.
    """

    if not isinstance(
        spectrum,
        Spectrum,
    ):

        raise TypeError(
            "spectrum must be a Spectrum object."
        )

    phase = spectrum.phase.copy()

    if unwrap:

        phase = np.unwrap(
            phase
        )

    return Spectrum(

        frequency=spectrum.frequency.copy(),

        magnitude=phase,

        phase=phase.copy(),

        complex_value=phase.astype(
            complex
        ),

        sampling_rate=spectrum.sampling_rate,
    )

# ==========================================================
# Convert to Decibel
# ==========================================================

def to_db(
    spectrum: Spectrum,
    mode: str = "amplitude",
    reference: float = 1.0,
    minimum_db: float = -120.0,
) -> Spectrum:

    if not isinstance(
        spectrum,
        Spectrum,
    ):
        ...

    if reference <= 0:
        ...

    if mode not in (
        "amplitude",
        "power",
    ):
        ...

    magnitude = np.maximum(
        spectrum.magnitude,
        np.finfo(float).eps,
    )

    if mode == "amplitude":

        db = 20.0 * np.log10(
            magnitude / reference
        )

    else:

        db = 10.0 * np.log10(
            magnitude / reference
        )

    db = np.maximum(
        db,
        minimum_db,
    )

    return Spectrum(

        frequency=spectrum.frequency.copy(),

        magnitude=db,

        phase=spectrum.phase.copy(),

        complex_value=db.astype(
            complex
        ),

        sampling_rate=spectrum.sampling_rate,
    )



# ==========================================================
# Convert from Decibel
# ==========================================================

def from_db(
    spectrum: Spectrum,
    mode: str = "amplitude",
    reference: float = 1.0,
) -> Spectrum:
    """
    Convert a decibel spectrum back to linear scale.

    Parameters
    ----------
    spectrum
        Input spectrum in dB.

    mode
        "amplitude" or "power".

    reference
        Reference value.

    Returns
    -------
    Spectrum
        Linear spectrum.
    """

    if not isinstance(
        spectrum,
        Spectrum,
    ):

        raise TypeError(
            "spectrum must be a Spectrum object."
        )

    if reference <= 0:

        raise ValueError(
            "reference must be positive."
        )

    if mode not in (
        "amplitude",
        "power",
    ):

        raise ValueError(
            "mode must be "
            "'amplitude' or 'power'."
        )

    db = spectrum.magnitude

    if mode == "amplitude":

        magnitude = (
            reference
            * np.power(
                10.0,
                db / 20.0,
            )
        )

    else:

        magnitude = (
            reference
            * np.power(
                10.0,
                db / 10.0,
            )
        )

    return Spectrum(

        frequency=spectrum.frequency.copy(),

        magnitude=magnitude,

        phase=spectrum.phase.copy(),

        complex_value=magnitude.astype(
            complex
        ),

        sampling_rate=spectrum.sampling_rate,
    )

# ==========================================================
# Magnitude Normalization
# ==========================================================

def normalize_spectrum(
    spectrum: Spectrum,
    reference: Optional[float] = None,
) -> Spectrum:
    """
    Normalize spectrum magnitude.

    Parameters
    ----------
    spectrum
        Input spectrum.

    reference
        Reference magnitude.
        If None, the peak magnitude is used.

    Returns
    -------
    Spectrum
        Normalized spectrum.
    """

    if not isinstance(
        spectrum,
        Spectrum,
    ):

        raise TypeError(
            "spectrum must be a Spectrum object."
        )

    magnitude = spectrum.magnitude.copy()

    if reference is None:

        reference = np.max(
            np.abs(magnitude)
        )

    if reference <= 0:

        raise ValueError(
            "reference must be positive."
        )

    magnitude = magnitude / reference

    complex_value = (
        spectrum.complex_value
        / reference
    )

    return Spectrum(

        frequency=spectrum.frequency.copy(),

        magnitude=magnitude,

        phase=spectrum.phase.copy(),

        complex_value=complex_value,

        sampling_rate=spectrum.sampling_rate,
    )

# ==========================================================
# Internal Helper
# ==========================================================

def _copy_spectrum(
    spectrum: Spectrum,
    *,
    frequency: Optional[np.ndarray] = None,
    magnitude: Optional[np.ndarray] = None,
    phase: Optional[np.ndarray] = None,
    complex_value: Optional[np.ndarray] = None,
) -> Spectrum:
    """
    Create a copy of a Spectrum object while
    replacing specified fields.

    This is an internal helper used to reduce
    duplicated Spectrum construction code.
    """

    if not isinstance(
        spectrum,
        Spectrum,
    ):

        raise TypeError(
            "spectrum must be a Spectrum object."
        )

    return Spectrum(

        frequency=(
            spectrum.frequency.copy()
            if frequency is None
            else np.asarray(
                frequency,
                dtype=float,
            )
        ),

        magnitude=(
            spectrum.magnitude.copy()
            if magnitude is None
            else np.asarray(
                magnitude,
                dtype=float,
            )
        ),

        phase=(
            spectrum.phase.copy()
            if phase is None
            else np.asarray(
                phase,
                dtype=float,
            )
        ),

        complex_value=(
            spectrum.complex_value.copy()
            if complex_value is None
            else np.asarray(
                complex_value,
                dtype=complex,
            )
        ),

        sampling_rate=spectrum.sampling_rate,
    )

# ==========================================================
# Peak Frequency
# ==========================================================

def peak_frequency(
    spectrum: Spectrum,
) -> float:
    """
    Get the frequency corresponding to the
    maximum spectrum magnitude.

    Parameters
    ----------
    spectrum
        Input spectrum.

    Returns
    -------
    float
        Peak frequency (Hz).
    """

    if not isinstance(
        spectrum,
        Spectrum,
    ):

        raise TypeError(
            "spectrum must be a Spectrum object."
        )

    if spectrum.bins == 0:

        raise ValueError(
            "empty spectrum."
        )

    index = np.argmax(
        spectrum.magnitude
    )

    return float(
        spectrum.frequency[index]
    )


# ==========================================================
# Peak Magnitude
# ==========================================================

def peak_magnitude(
    spectrum: Spectrum,
) -> float:
    """
    Get the maximum spectrum magnitude.

    Parameters
    ----------
    spectrum
        Input spectrum.

    Returns
    -------
    float
        Peak magnitude.
    """

    if not isinstance(
        spectrum,
        Spectrum,
    ):

        raise TypeError(
            "spectrum must be a Spectrum object."
        )

    if spectrum.bins == 0:

        raise ValueError(
            "empty spectrum."
        )

    return float(
        np.max(
            spectrum.magnitude
        )
    )

# ==========================================================
# Dominant Component
# ==========================================================

def dominant_component(
    spectrum: Spectrum,
) -> tuple[float, float]:
    """
    Get the dominant frequency component.

    Parameters
    ----------
    spectrum
        Input spectrum.

    Returns
    -------
    tuple
        (peak_frequency, peak_magnitude)
    """

    if not isinstance(
        spectrum,
        Spectrum,
    ):

        raise TypeError(
            "spectrum must be a Spectrum object."
        )

    if spectrum.bins == 0:

        raise ValueError(
            "empty spectrum."
        )

    index = np.argmax(
        spectrum.magnitude
    )

    return (

        float(
            spectrum.frequency[index]
        ),

        float(
            spectrum.magnitude[index]
        ),

    )


# ==========================================================
# Bandwidth (-3 dB)
# ==========================================================

def bandwidth(
    spectrum: Spectrum,
    threshold_db: float = -3.0,
) -> float:
    """
    Calculate bandwidth using a threshold
    relative to the peak magnitude.

    Parameters
    ----------
    spectrum
        Input spectrum.

    threshold_db
        Relative threshold in dB.

    Returns
    -------
    float
        Bandwidth (Hz).
    """

    if not isinstance(
        spectrum,
        Spectrum,
    ):

        raise TypeError(
            "spectrum must be a Spectrum object."
        )

    if spectrum.bins == 0:

        raise ValueError(
            "empty spectrum."
        )

    peak = np.max(
        spectrum.magnitude
    )

    if peak <= 0:

        return 0.0

    threshold = peak * (

        10.0 ** (
            threshold_db / 20.0
        )
    )

    indices = np.where(
        spectrum.magnitude >= threshold
    )[0]

    if len(indices) == 0:

        return 0.0

    frequencies = np.sort(

        spectrum.frequency[
            indices
        ]

    )

    return float(

        frequencies[-1]

        -

        frequencies[0]

    )
    indices = np.where(
        spectrum.magnitude >= threshold
    )[0]

    if len(indices) == 0:
        return 0.0

    frequencies = np.sort(

        spectrum.frequency[
            indices
        ]

    )

    return float(

        frequencies[-1]

        -

        frequencies[0]

    )

# ==========================================================
# Normalize Spectrum
# ==========================================================

def normalize_spectrum(
    spectrum: Spectrum,
) -> Spectrum:
    """
    Normalize spectrum magnitude so that the
    maximum magnitude equals 1.

    Parameters
    ----------
    spectrum
        Input spectrum.

    Returns
    -------
    Spectrum
        Normalized spectrum.
    """

    if not isinstance(
        spectrum,
        Spectrum,
    ):

        raise TypeError(
            "spectrum must be a Spectrum object."
        )

    maximum = np.max(
        np.abs(
            spectrum.magnitude
        )
    )

    if maximum <= 0:

        return _copy_spectrum(
            spectrum,
        )

    magnitude = (
        spectrum.magnitude
        / maximum
    )

    complex_value = (
        spectrum.complex_value
        / maximum
    )

    return _copy_spectrum(

        spectrum,

        magnitude=magnitude,

        complex_value=complex_value,

    )


# ==========================================================
# Spectrum Energy
# ==========================================================

def spectrum_energy(
    spectrum: Spectrum,
) -> float:
    """
    Calculate spectrum energy.

    Parameters
    ----------
    spectrum
        Input spectrum.

    Returns
    -------
    float
        Total spectrum energy.
    """

    if not isinstance(
        spectrum,
        Spectrum,
    ):

        raise TypeError(
            "spectrum must be a Spectrum object."
        )

    return float(

        np.sum(

            np.abs(
                spectrum.complex_value
            ) ** 2

        )

    )


# ==========================================================
# Spectrum Power
# ==========================================================

def spectrum_power(
    spectrum: Spectrum,
) -> float:
    """
    Calculate average spectrum power.

    Parameters
    ----------
    spectrum
        Input spectrum.

    Returns
    -------
    float
        Average spectrum power.
    """

    if not isinstance(
        spectrum,
        Spectrum,
    ):

        raise TypeError(
            "spectrum must be a Spectrum object."
        )

    if spectrum.bins == 0:

        return 0.0

    return float(

        spectrum_energy(
            spectrum
        )

        / spectrum.bins

    )

# ==========================================================
# Public API
# ==========================================================

__all__ = [

    # Analyzer
    "SpectrumAnalyzer",

    # FFT
    "fft",
    "ifft",

    # Frequency
    "frequency_axis",
    "frequency_resolution",
    "nyquist_frequency",

    # FFT Shift
    "fftshift",
    "ifftshift",

    # Spectrum Type
    "single_side",
    "double_side",

    # Analysis
    "amplitude_spectrum",
    "power_spectrum",
    "phase_spectrum",

    # dB
    "to_db",
    "from_db",

    # Statistics
    "normalize_spectrum",
    "peak_frequency",
    "peak_magnitude",
    "dominant_component",
    "bandwidth",
    "spectrum_energy",
    "spectrum_power",
]








