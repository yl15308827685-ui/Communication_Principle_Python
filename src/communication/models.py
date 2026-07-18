"""
=============================================================
Communication Principle Python SDK

models.py

Core Data Models

Python
------
3.9+

Version
-------
2.0.0
=============================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Optional

import numpy as np


# ============================================================
# Signal
# ============================================================

@dataclass
class Signal:
    """
    Time-domain signal.
    """

    value: np.ndarray

    sampling_rate: float

    time: Optional[np.ndarray] = None

    name: str = "Signal"

    unit: str = ""

    info: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):

        self.value = np.asarray(
            self.value,
            dtype=float
        )

        if self.value.ndim != 1:
            raise ValueError(
                "Signal must be one-dimensional."
            )

        if self.sampling_rate <= 0:
            raise ValueError(
                "sampling_rate must be positive."
            )

        if self.time is None:

            self.time = (
                np.arange(
                    len(self.value),
                    dtype=float
                )
                / self.sampling_rate
            )

        else:

            self.time = np.asarray(
                self.time,
                dtype=float
            )

            if len(self.time) != len(self.value):

                raise ValueError(
                    "time and value length mismatch."
                )

    # --------------------------------------------------------

    @property
    def samples(self) -> int:

        return len(self.value)

    # --------------------------------------------------------
    # --------------------------------------------------------

    @property
    def sample_count(self) -> int:
        """
        Backward compatibility.
        """
        return self.samples
    # --------------------------------------------------------

    @property
    def sampling_frequency(self) -> float:
        """
        Backward compatibility.
        """
        return self.sampling_rate

    # --------------------------------------------------------

    @property
    def fs(self) -> float:
        """
        Alias of sampling_rate.
        """
        return self.sampling_rate

    @property
    def duration(self) -> float:

        return self.samples / self.sampling_rate

    # --------------------------------------------------------

    @property
    def dt(self) -> float:

        return 1.0 / self.sampling_rate

    # --------------------------------------------------------

    def copy(self):

        return Signal(

            value=self.value.copy(),

            sampling_rate=self.sampling_rate,

            time=self.time.copy(),

            name=self.name,

            unit=self.unit,

            info=self.info.copy(),
        )

    # --------------------------------------------------------

    def astype(self, dtype):

        return Signal(

            value=self.value.astype(dtype),

            sampling_rate=self.sampling_rate,

            time=self.time.copy(),

            name=self.name,

            unit=self.unit,

            info=self.info.copy(),
        )

    # --------------------------------------------------------

    def __len__(self):

        return self.samples

    # --------------------------------------------------------

    def __iter__(self):

        return iter(self.value)

    # --------------------------------------------------------

    def __getitem__(self, item):

        return self.value[item]

    # --------------------------------------------------------

    def __repr__(self):

        return (

            "Signal("

            f"samples={self.samples}, "

            f"fs={self.sampling_rate:.3f} Hz)"

        )

# ============================================================
# Spectrum
# ============================================================

@dataclass
class Spectrum:
    """
    Frequency-domain spectrum.
    """

    frequency: np.ndarray

    magnitude: np.ndarray

    phase: np.ndarray

    complex_value: np.ndarray

    sampling_rate: float

    def __post_init__(self):

        self.frequency = np.asarray(
            self.frequency,
            dtype=float
        )

        self.magnitude = np.asarray(
            self.magnitude,
            dtype=float
        )

        self.phase = np.asarray(
            self.phase,
            dtype=float
        )

        self.complex_value = np.asarray(
            self.complex_value,
            dtype=complex
        )

        n = len(self.frequency)

        if len(self.magnitude) != n:
            raise ValueError(
                "frequency and magnitude length mismatch."
            )

        if len(self.phase) != n:
            raise ValueError(
                "frequency and phase length mismatch."
            )

        if len(self.complex_value) != n:
            raise ValueError(
                "frequency and complex_value length mismatch."
            )

    # --------------------------------------------------------

    @property
    def bins(self) -> int:

        return len(self.frequency)

    # --------------------------------------------------------

    # --------------------------------------------------------

    @property
    def sample_count(self) -> int:
        """
        Backward compatibility.
        """
        return self.bins

    # --------------------------------------------------------

    @property
    def amplitude(self):
        """
        Backward compatibility.
        """
        return self.magnitude

    # --------------------------------------------------------

    @property
    def sampling_frequency(self) -> float:
        """
        Backward compatibility.
        """
        return self.sampling_rate

    # --------------------------------------------------------

    @property
    def fs(self) -> float:
        """
        Alias of sampling_rate.
        """
        return self.sampling_rate

    @property
    def nyquist(self) -> float:

        return self.sampling_rate / 2.0

    # --------------------------------------------------------

    @property
    def resolution(self) -> float:

        if self.bins < 2:
            return 0.0

        return float(
            self.frequency[1] -
            self.frequency[0]
        )

    # --------------------------------------------------------

    @property
    def peak_index(self) -> int:

        return int(
            np.argmax(self.magnitude)
        )

    # --------------------------------------------------------

    @property
    def peak_frequency(self) -> float:

        return float(
            self.frequency[
                self.peak_index
            ]
        )

    # --------------------------------------------------------

    @property
    def peak_magnitude(self) -> float:

        return float(
            self.magnitude[
                self.peak_index
            ]
        )

    # --------------------------------------------------------

    def copy(self):

        return Spectrum(

            frequency=self.frequency.copy(),

            magnitude=self.magnitude.copy(),

            phase=self.phase.copy(),

            complex_value=self.complex_value.copy(),

            sampling_rate=self.sampling_rate,
        )

    # --------------------------------------------------------

    def __len__(self):

        return self.bins

    # --------------------------------------------------------

    def __getitem__(self, item):

        return self.magnitude[item]

    # --------------------------------------------------------

    def __repr__(self):

        return (

            "Spectrum("

            f"bins={self.bins}, "

            f"peak={self.peak_frequency:.3f} Hz)"

        )

    @property
    def amplitude(self):
        """
        Backward compatibility.
        """
        return self.magnitude

    @property
    def sampling_frequency(self):
        """
        Backward compatibility.
        """
        return self.sampling_rate

    @property
    def fs(self):
        """
        Alias of sampling_rate.
        """
        return self.sampling_rate


# ============================================================
# SignalStatistics
# ============================================================

@dataclass
class SignalStatistics:
    """
    Statistics of a time-domain signal.
    """

    mean: float

    rms: float

    variance: float

    std: float

    peak: float

    peak_to_peak: float

    energy: float

    power: float

    # --------------------------------------------------------

    def as_dict(self):

        return {

            "mean": self.mean,

            "rms": self.rms,

            "variance": self.variance,

            "std": self.std,

            "peak": self.peak,

            "peak_to_peak": self.peak_to_peak,

            "energy": self.energy,

            "power": self.power,

        }

    # --------------------------------------------------------

    def copy(self):

        return SignalStatistics(

            mean=self.mean,

            rms=self.rms,

            variance=self.variance,

            std=self.std,

            peak=self.peak,

            peak_to_peak=self.peak_to_peak,

            energy=self.energy,

            power=self.power,

        )

    # --------------------------------------------------------

    def __repr__(self):

        return (

            "SignalStatistics("

            f"mean={self.mean:.6f}, "

            f"rms={self.rms:.6f}, "

            f"std={self.std:.6f}, "

            f"peak={self.peak:.6f})"

        )


# ============================================================
# AnalysisResult
# ============================================================

@dataclass
class AnalysisResult:
    """
    Comparison result between two signals.
    """

    mae: float

    mse: float

    rmse: float

    correlation: float

    # --------------------------------------------------------

    def as_dict(self):

        return {

            "mae": self.mae,

            "mse": self.mse,

            "rmse": self.rmse,

            "correlation": self.correlation,

        }

    # --------------------------------------------------------

    def copy(self):

        return AnalysisResult(

            mae=self.mae,

            mse=self.mse,

            rmse=self.rmse,

            correlation=self.correlation,

        )

    # --------------------------------------------------------

    def __repr__(self):

        return (

            "AnalysisResult("

            f"mae={self.mae:.6f}, "

            f"rmse={self.rmse:.6f}, "

            f"corr={self.correlation:.6f})"

        )
# ============================================================
# FilterResult
# ============================================================

@dataclass
class FilterResult:
    """
    Result of a digital filter.
    """

    input_signal: Signal

    output_signal: Signal

    filter_name: str = ""

    # --------------------------------------------------------

    @property
    def samples(self) -> int:

        return self.output_signal.samples

    # --------------------------------------------------------

    def copy(self):

        return FilterResult(

            input_signal=self.input_signal.copy(),

            output_signal=self.output_signal.copy(),

            filter_name=self.filter_name,

        )

    # --------------------------------------------------------

    def __repr__(self):

        return (

            "FilterResult("

            f"filter='{self.filter_name}', "

            f"samples={self.samples})"

        )


# ============================================================
# ModulationResult
# ============================================================

@dataclass
class ModulationResult:
    """
    Result of signal modulation.
    """

    baseband: Signal

    carrier: Signal

    modulated: Signal

    modulation: str = ""

    # --------------------------------------------------------

    @property
    def samples(self) -> int:

        return self.modulated.samples

    # --------------------------------------------------------

    def copy(self):

        return ModulationResult(

            baseband=self.baseband.copy(),

            carrier=self.carrier.copy(),

            modulated=self.modulated.copy(),

            modulation=self.modulation,

        )

    # --------------------------------------------------------

    def __repr__(self):

        return (

            "ModulationResult("

            f"type='{self.modulation}', "

            f"samples={self.samples})"

        )

# ============================================================
# ChannelResult
# ============================================================

@dataclass
class ChannelResult:
    """
    Result of channel simulation.
    """

    transmitted: Signal

    received: Signal

    channel: str = ""

    snr: float = 0.0

    # --------------------------------------------------------

    @property
    def samples(self) -> int:

        return self.received.samples

    # --------------------------------------------------------

    def copy(self):

        return ChannelResult(

            transmitted=self.transmitted.copy(),

            received=self.received.copy(),

            channel=self.channel,

            snr=self.snr,

        )

    # --------------------------------------------------------

    def __repr__(self):

        return (

            "ChannelResult("

            f"channel='{self.channel}', "

            f"snr={self.snr:.2f} dB, "

            f"samples={self.samples})"

        )


# ============================================================
# CodingResult
# ============================================================

@dataclass
class CodingResult:
    """
    Result of channel coding.
    """

    input_bits: np.ndarray

    output_bits: np.ndarray

    coding: str = ""

    def __post_init__(self):

        self.input_bits = np.asarray(
            self.input_bits,
            dtype=np.uint8
        )

        self.output_bits = np.asarray(
            self.output_bits,
            dtype=np.uint8
        )

    # --------------------------------------------------------

    @property
    def input_length(self) -> int:

        return len(self.input_bits)

    # --------------------------------------------------------

    @property
    def output_length(self) -> int:

        return len(self.output_bits)

    # --------------------------------------------------------

    @property
    def code_rate(self) -> float:

        if self.output_length == 0:
            return 0.0

        return (
            self.input_length /
            self.output_length
        )

    # --------------------------------------------------------

    def copy(self):

        return CodingResult(

            input_bits=self.input_bits.copy(),

            output_bits=self.output_bits.copy(),

            coding=self.coding,

        )

    # --------------------------------------------------------

    def __repr__(self):

        return (

            "CodingResult("

            f"type='{self.coding}', "

            f"rate={self.code_rate:.3f})"

        )

# ============================================================
# SimulationResult
# ============================================================

@dataclass
class SimulationResult:
    """
    Result of a complete communication simulation.
    """

    signal: Optional[Signal] = None

    spectrum: Optional[Spectrum] = None

    statistics: Optional[SignalStatistics] = None

    analysis: Optional[AnalysisResult] = None

    description: str = ""

    # --------------------------------------------------------

    def copy(self):

        return SimulationResult(

            signal=None if self.signal is None else self.signal.copy(),

            spectrum=None if self.spectrum is None else self.spectrum.copy(),

            statistics=(
                None
                if self.statistics is None
                else self.statistics.copy()
            ),

            analysis=(
                None
                if self.analysis is None
                else self.analysis.copy()
            ),

            description=self.description,

        )

    # --------------------------------------------------------

    def __repr__(self):

        return (

            "SimulationResult("

            f"description='{self.description}')"

        )

# ============================================================
# ResultTable
# ============================================================

@dataclass
class ResultTable:
    """
    Generic tabular result.
    """

    title: str = ""

    headers: list = None

    rows: list = None

    def __post_init__(self):

        if self.headers is None:
            self.headers = []

        if self.rows is None:
            self.rows = []

    def __repr__(self):

        return (
            f"ResultTable("
            f"title='{self.title}', "
            f"rows={len(self.rows)})"
        )


# ============================================================
# FigureInfo
# ============================================================

@dataclass
class FigureInfo:
    """
    Figure metadata.
    """

    title: str = ""

    xlabel: str = ""

    ylabel: str = ""

    filename: str = ""

    dpi: int = 300

    def __repr__(self):

        return (
            f"FigureInfo("
            f"title='{self.title}')"
        )


# ============================================================
# Backward Compatibility
# ============================================================

ExperimentResult = SimulationResult

# ============================================================
# Public Export
# ============================================================

__all__ = [

    "Signal",
    "Spectrum",

    "SignalStatistics",
    "AnalysisResult",

    "FilterResult",
    "ModulationResult",

    "ChannelResult",
    "CodingResult",

    "SimulationResult",
    "ExperimentResult",

    "ResultTable",
    "FigureInfo",
]



