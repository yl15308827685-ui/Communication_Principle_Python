"""
============================================================
Communication_Principle_Python

Experiment 15
Two-Tone Spectrum Analysis

Version
-------
3.0.0

Compatible SDK
--------------
Communication_Principle_Python API Freeze v1.0

Description
-----------
Study spectrum characteristics of a two-tone signal.

Author
------
Communication_Principle_Python Textbook Project
============================================================
"""

from __future__ import annotations

import json

from pathlib import Path
from dataclasses import dataclass

import numpy as np

from communication.config import DEFAULT_CONFIG
from communication.paths import experiment_output_dir

from communication.models import Signal

from communication.signals import SignalGenerator

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

# ============================================================
# Experiment Parameters
# ============================================================

CONFIG = DEFAULT_CONFIG

FFT_POINTS = CONFIG.fft_points

AMPLITUDE1 = 1.0
AMPLITUDE2 = 1.0

FREQUENCY1 = 100.0
FREQUENCY2 = 300.0

PHASE1 = 0.0
PHASE2 = 0.0

# ============================================================
# Two Tone Report
# ============================================================

@dataclass
class TwoToneReport:

    statistics: object

    spectrum: object

    signal: Signal

# ============================================================
# Generate Two-Tone Signal
# ============================================================

def generate_signal() -> Signal:
    """
    Generate two-tone signal.
    """

    generator = SignalGenerator(CONFIG)

    signal1 = generator.sine(
        amplitude=AMPLITUDE1,
        frequency=FREQUENCY1,
        phase=PHASE1,
    )

    signal2 = generator.sine(
        amplitude=AMPLITUDE2,
        frequency=FREQUENCY2,
        phase=PHASE2,
    )

    signal = Signal(

        value=signal1.value + signal2.value,

        sampling_rate=signal1.sampling_rate,

        time=signal1.time.copy(),

        name="Two-Tone Signal",

        unit=signal1.unit,

        info=signal1.info.copy(),

    )

    return signal

# ============================================================
# Run Experiment
# ============================================================

def run_experiment() -> TwoToneReport:
    """
    Run experiment.
    """

    signal = generate_signal()

    spectrum = fft(
        signal,
    )

    statistics = analyze(
        signal,
    )

    return TwoToneReport(
        statistics=statistics,
        spectrum=spectrum,
        signal=signal,
    )

# ============================================================
# Export Results
# ============================================================

def export_result(
    report: TwoToneReport,
    output_dir: Path,
) -> None:
    """
    Export experiment results.
    """

    export_signal_csv(
        report.signal,
        output_dir / "two_tone_signal.csv",
    )

    export_spectrum_csv(
        report.spectrum,
        output_dir / "two_tone_spectrum.csv",
    )

    export_statistics_csv(
        report.statistics,
        output_dir / "two_tone_statistics.csv",
    )

# ============================================================
# Draw Figures
# ============================================================

def draw_result(
    report: TwoToneReport,
    output_dir: Path,
) -> None:
    """
    Draw experiment figures.
    """

    # --------------------------------------------------------
    # Signal
    # --------------------------------------------------------

    manager = plot_signal(
        report.signal,
        title="Two-Tone Signal",
    )

    manager.grid()

    manager.save(
        output_dir / "two_tone_signal.png",
    )

    manager.close()

    # --------------------------------------------------------
    # Spectrum
    # --------------------------------------------------------

    manager = plot_spectrum(
        report.spectrum,
        title="Two-Tone Spectrum",
    )

    manager.grid()

    manager.save(
        output_dir / "two_tone_spectrum.png",
    )

    manager.close()

# ============================================================
# Print Report
# ============================================================

def print_report(
    report: TwoToneReport,
) -> None:
    """
    Print experiment report.
    """

    statistics = report.statistics
    spectrum = report.spectrum

    print("=" * 60)
    print("Two-Tone Spectrum Analysis")
    print("-" * 60)

    print(f"Frequency 1      : {FREQUENCY1:.2f} Hz")
    print(f"Frequency 2      : {FREQUENCY2:.2f} Hz")

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
        experiment="exp15_two_tone_spectrum",
    )

    print()
    print("=" * 60)
    print("Communication_Principle_Python")
    print("Experiment 15")
    print("Two-Tone Spectrum Analysis")
    print("=" * 60)
    print()

    # --------------------------------------------------------
    # Run Experiment
    # --------------------------------------------------------

    report = run_experiment()

    # --------------------------------------------------------
    # Export Results
    # --------------------------------------------------------

    export_result(
        report,
        output_dir,
    )

    # --------------------------------------------------------
    # Draw Figures
    # --------------------------------------------------------

    draw_result(
        report,
        output_dir,
    )

    # --------------------------------------------------------
    # Console Report
    # --------------------------------------------------------

    print_report(
        report,
    )

    # --------------------------------------------------------
    # Summary CSV
    # --------------------------------------------------------

    summary_csv = output_dir / "summary.csv"

    with open(
        summary_csv,
        "w",
        encoding="utf-8",
    ) as fp:

        fp.write(
            "Frequency1,"
            "Frequency2,"
            "PeakFrequency,"
            "PeakMagnitude,"
            "Energy,"
            "Power\n"
        )

        fp.write(

            f"{FREQUENCY1:.2f},"

            f"{FREQUENCY2:.2f},"

            f"{report.spectrum.peak_frequency:.6f},"

            f"{report.spectrum.peak_magnitude:.6f},"

            f"{report.statistics.energy:.6f},"

            f"{report.statistics.power:.6f}\n"

        )

    # --------------------------------------------------------
    # Summary JSON
    # --------------------------------------------------------

    summary_json = output_dir / "summary.json"

    summary = {

        "frequency_1": FREQUENCY1,

        "frequency_2": FREQUENCY2,

        "peak_frequency":

            report.spectrum.peak_frequency,

        "peak_magnitude":

            report.spectrum.peak_magnitude,

        "energy":

            report.statistics.energy,

        "power":

            report.statistics.power,

    }

    with open(
        summary_json,
        "w",
        encoding="utf-8",
    ) as fp:

        json.dump(
            summary,
            fp,
            indent=4,
            ensure_ascii=False,
        )

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



