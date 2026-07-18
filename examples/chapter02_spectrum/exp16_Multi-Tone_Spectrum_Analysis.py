"""
============================================================
Communication_Principle_Python

Experiment 16
Multi-Tone Spectrum Analysis

Version
-------
3.0.0

Compatible SDK
--------------
Communication_Principle_Python API Freeze v1.0

Description
-----------
Spectrum analysis of multi-tone signals.

Author
------
Communication_Principle_Python Textbook Project
============================================================
"""

from __future__ import annotations

import json

import numpy as np

from pathlib import Path

from dataclasses import dataclass

from communication.config import DEFAULT_CONFIG

from communication.paths import experiment_output_dir

from communication.models import Signal

from communication.signals import SignalGenerator

from communication.spectrum import fft

from communication.analysis import analyze

from communication.plotting import (

    plot_signal,

    plot_spectrum,

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

AMPLITUDE = 1.0

FREQUENCIES = [

    100,

    250,

    500,

    800,

]

PHASE = 0.0

# ============================================================
# Report
# ============================================================

@dataclass

class MultiToneReport:

    statistics: object

    spectrum: object

    signal: Signal

# ============================================================
# Generate Multi-Tone Signal
# ============================================================

def generate_signal() -> Signal:
    """
    Generate multi-tone signal.
    """

    generator = SignalGenerator(CONFIG)

    signals = []

    for frequency in FREQUENCIES:

        signals.append(

            generator.sine(

                amplitude=AMPLITUDE,

                frequency=frequency,

                phase=PHASE,

            )

        )

    value = np.zeros_like(

        signals[0].value,

    )

    for signal in signals:

        value += signal.value

    return Signal(

        value=value,

        sampling_rate=signals[0].sampling_rate,

        time=signals[0].time.copy(),

        name="Multi-Tone Signal",

        unit=signals[0].unit,

        info=signals[0].info.copy(),

    )

# ============================================================
# Run Experiment
# ============================================================

def run_experiment() -> MultiToneReport:
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

    return MultiToneReport(

        statistics=statistics,

        spectrum=spectrum,

        signal=signal,

    )

# ============================================================
# Export Results
# ============================================================

def export_result(
    report: MultiToneReport,
    output_dir: Path,
) -> None:
    """
    Export experiment results.
    """

    export_signal_csv(
        report.signal,
        output_dir / "multi_tone_signal.csv",
    )

    export_spectrum_csv(
        report.spectrum,
        output_dir / "multi_tone_spectrum.csv",
    )

    export_statistics_csv(
        report.statistics,
        output_dir / "multi_tone_statistics.csv",
    )

# ============================================================
# Draw Figures
# ============================================================

def draw_result(
    report: MultiToneReport,
    output_dir: Path,
) -> None:
    """
    Draw experiment figures.
    """

    # --------------------------------------------------------
    # Time Domain
    # --------------------------------------------------------

    manager = plot_signal(
        report.signal,
        title="Multi-Tone Signal",
    )

    manager.grid()

    manager.save(
        output_dir / "multi_tone_signal.png",
    )

    manager.close()

    # --------------------------------------------------------
    # Spectrum
    # --------------------------------------------------------

    manager = plot_spectrum(
        report.spectrum,
        title="Multi-Tone Spectrum",
    )

    manager.grid()

    manager.save(
        output_dir / "multi_tone_spectrum.png",
    )

    manager.close()

# ============================================================
# Print Report
# ============================================================

def print_report(
    report: MultiToneReport,
) -> None:
    """
    Print experiment report.
    """

    statistics = report.statistics
    spectrum = report.spectrum

    print("=" * 60)
    print("Multi-Tone Spectrum Analysis")
    print("-" * 60)

    print("Signal Frequencies :")

    for frequency in FREQUENCIES:

        print(f"    {frequency:.2f} Hz")

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
        experiment="exp16_multi_tone_spectrum",
    )

    print()
    print("=" * 60)
    print("Communication_Principle_Python")
    print("Experiment 16")
    print("Multi-Tone Spectrum Analysis")
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
            "Peak Frequency,"
            "Peak Magnitude,"
            "Energy,"
            "Power\n"
        )

        fp.write(

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

        "frequencies": FREQUENCIES,

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
