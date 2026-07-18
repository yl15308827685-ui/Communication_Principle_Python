"""
============================================================
Communication_Principle_Python

Experiment 10
Window Functions

Version
-------
3.0.0

Compatible SDK
--------------
Communication_Principle_Python API Freeze v1.0

Description
-----------
Compare the spectrum characteristics of common window
functions using the frozen Communication_Principle_Python SDK.

Author
------
Communication_Principle_Python Textbook Project
============================================================
"""

from __future__ import annotations

from pathlib import Path
from communication.paths import experiment_output_dir
from dataclasses import dataclass

import numpy as np

from communication.config import DEFAULT_CONFIG

from communication.signals import SignalGenerator
from communication.models import Signal

from communication.spectrum import fft

from communication.analysis import analyze

from communication.plotting import (
    plot_signal,
    plot_spectrum,
    plot_compare,
)

from communication.export import (
    export_signal_csv,
    export_spectrum_csv,
    export_statistics_csv,
)

from communication.models import SignalStatistics
from communication.models import Spectrum

statistics: SignalStatistics

spectrum: Spectrum


# ============================================================
# Window Definition
# ============================================================

WINDOW_RECTANGULAR = "Rectangular"
WINDOW_HANN = "Hann"
WINDOW_HAMMING = "Hamming"
WINDOW_BLACKMAN = "Blackman"


# ============================================================
# Experiment Parameters
# ============================================================

from communication.config import ExperimentConfig

CONFIG = ExperimentConfig()

FFT_POINTS = CONFIG.fft_points




# ============================================================
# Window Report
# ============================================================

@dataclass
class WindowReport:

    name: str

    statistics: object

    spectrum: object

    signal: Signal


# ============================================================
# Window Generator
# ============================================================

def create_window(
    name: str,
    length: int,
) -> np.ndarray:
    """
    Create window sequence.

    Parameters
    ----------
    name
        Window type.

    length
        Window length.

    Returns
    -------
    ndarray
    """

    name = name.lower()

    if name == "rectangular":
        return np.ones(length)

    if name == "hann":
        return np.hanning(length)

    if name == "hamming":
        return np.hamming(length)

    if name == "blackman":
        return np.blackman(length)

    raise ValueError(
        f"Unsupported window: {name}"
    )


# ============================================================
# Apply Window
# ============================================================

def apply_window(
    signal: Signal,
    window: np.ndarray,
) -> Signal:
    """
    Multiply Signal by window.

    Returns
    -------
    Signal
    """

    if len(window) != signal.samples:

        raise ValueError(
            "Window length mismatch."
        )

    return Signal(
        value=signal.value * window,
        sampling_rate=signal.sampling_rate,
        time=signal.time.copy(),
        name=f"{signal.name} ({len(window)} samples)",
        unit=signal.unit,
        info=signal.info.copy(),
    )

# ============================================================
# Generate Test Signal
# ============================================================

def generate_test_signal() -> Signal:
    """
    Generate the test sine signal.

    Returns
    -------
    Signal
    """

    generator = SignalGenerator(CONFIG)

    signal = generator.sine(
        amplitude=CONFIG.amplitude,
        frequency=CONFIG.frequency,
        phase=CONFIG.phase,
    )

    signal.name = "Original Signal"

    return signal


# ============================================================
# Run One Window Experiment
# ============================================================

def run_window(
    signal: Signal,
    window_name: str,
) -> WindowReport:
    """
    Run one window experiment.

    Parameters
    ----------
    signal
        Original signal.

    window_name
        Window type.

    Returns
    -------
    WindowReport
    """

    # -----------------------------------------
    # Create Window
    # -----------------------------------------

    window = create_window(
        window_name,
        signal.samples,
    )

    # -----------------------------------------
    # Apply Window
    # -----------------------------------------

    window_signal = apply_window(
        signal,
        window,
    )

    window_signal.name = window_name

    # -----------------------------------------
    # FFT
    # -----------------------------------------

    spectrum = fft(
        window_signal,
    )

    # -----------------------------------------
    # Statistics
    # -----------------------------------------

    statistics = analyze(
        window_signal,
    )

    return WindowReport(
        name=window_name,
        statistics=statistics,
        spectrum=spectrum,
        signal=window_signal,
    )


# ============================================================
# Export Results
# ============================================================

def export_result(
    report: WindowReport,
    output_dir: Path,
) -> None:
    """
    Export CSV files.
    """

    export_signal_csv(
        report.signal,
        output_dir / f"{report.name.lower()}_signal.csv",
    )

    export_spectrum_csv(
        report.spectrum,
        output_dir / f"{report.name.lower()}_spectrum.csv",
    )

    export_statistics_csv(
        report.statistics,
        output_dir / f"{report.name.lower()}_statistics.csv",
    )


# ============================================================
# Draw Figures
# ============================================================

def draw_result(
    original: Signal,
    report: WindowReport,
    output_dir: Path,
) -> None:
    """
    Draw all figures.
    """

    # -----------------------------------------
    # Time-domain comparison
    # -----------------------------------------

    manager = plot_compare(
        original,
        report.signal,
        title=f"{report.name} Window",
        label1="Original",
        label2=report.name,
    )

    manager.save(
        output_dir / f"{report.name.lower()}_time.png",
    )

    manager.close()

    # -----------------------------------------
    # Windowed signal
    # -----------------------------------------

    manager = plot_signal(
        report.signal,
        title=f"{report.name} Windowed Signal",
    )

    manager.save(
        output_dir / f"{report.name.lower()}_signal.png",
    )

    manager.close()

    # -----------------------------------------
    # Spectrum
    # -----------------------------------------

    manager = plot_spectrum(
        report.spectrum,
        title=f"{report.name} Spectrum",
    )

    manager.save(
        output_dir / f"{report.name.lower()}_spectrum.png",
    )

    manager.close()

# ============================================================
# Print Statistics
# ============================================================

def print_report(
    report: WindowReport,
) -> None:
    """
    Print experiment report.
    """

    statistics = report.statistics
    spectrum = report.spectrum

    print("=" * 60)
    print(f"Window : {report.name}")
    print("-" * 60)

    print(f"Mean             : {statistics.mean:.6f}")
    print(f"RMS              : {statistics.rms:.6f}")
    print(f"Variance         : {statistics.variance:.6f}")
    print(f"Standard Dev.    : {statistics.std:.6f}")
    print(f"Peak             : {statistics.peak:.6f}")
    print(f"Peak-to-Peak     : {statistics.peak_to_peak:.6f}")
    print(f"Energy           : {statistics.energy:.6f}")
    print(f"Average Power    : {statistics.power:.6f}")

    print("-" * 60)

    print(f"FFT Bins         : {spectrum.bins}")
    print(f"Frequency Res.   : {spectrum.resolution:.6f} Hz")
    print(f"Nyquist          : {spectrum.nyquist:.6f} Hz")
    print(f"Peak Frequency   : {spectrum.peak_frequency:.6f} Hz")
    print(f"Peak Magnitude   : {spectrum.peak_magnitude:.6f}")

    print("=" * 60)
    print()


# ============================================================
# Main Experiment
# ============================================================

def main() -> None:
    """
    Main experiment.
    """

    output_dir = experiment_output_dir(
        chapter=2,
        experiment="exp10_window_functions",
    )
    print()
    print("=" * 60)
    print("Communication_Principle_Python")
    print("Experiment 10")
    print("Window Functions")
    print("=" * 60)
    print()

    # --------------------------------------------------------
    # Generate Original Signal
    # --------------------------------------------------------

    original_signal = generate_test_signal()

    # 保存原始信号
    export_signal_csv(
        original_signal,
        output_dir / "original_signal.csv",
    )

    manager = plot_signal(
        original_signal,
        title="Original Signal",
    )

    manager.save(
        output_dir / "original_signal.png",
    )

    manager.close()

    # --------------------------------------------------------
    # Window List
    # --------------------------------------------------------

    windows = [

        WINDOW_RECTANGULAR,

        WINDOW_HANN,

        WINDOW_HAMMING,

        WINDOW_BLACKMAN,

    ]

    reports = []

    # --------------------------------------------------------
    # Run Experiments
    # --------------------------------------------------------

    for window_name in windows:

        report = run_window(
            original_signal,
            window_name,
        )

        reports.append(report)

        export_result(
            report,
            output_dir,
        )

        draw_result(
            original_signal,
            report,
            output_dir,
        )

        print_report(report)

    print()
    print("=" * 60)
    print("Experiment Finished Successfully.")
    print(f"Output Directory : {output_dir}")
    print("=" * 60)

# ============================================================
# Script Entry
# ============================================================

if __name__ == "__main__":

    try:

        main()

    except KeyboardInterrupt:

        print()
        print("Experiment interrupted by user.")

    except Exception as error:

        print()
        print("=" * 60)
        print("Experiment failed.")
        print("=" * 60)
        print(type(error).__name__)
        print(error)
        print("=" * 60)

        raise
