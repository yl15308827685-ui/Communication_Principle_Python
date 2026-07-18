"""
============================================================
Communication_Principle_Python

Experiment 13
Phase Effect on Spectrum

Version
-------
3.0.0

Compatible SDK
--------------
Communication_Principle_Python API Freeze v1.0

Description
-----------
Compare the influence of signal phase on
time-domain waveform and frequency spectrum.

Author
------
Communication_Principle_Python Textbook Project
============================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np

from examples.template import ExperimentTemplate
from communication.config import DEFAULT_CONFIG

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
# Phase Definition
# ============================================================

PHASE_0 = 0.0

PHASE_45 = np.pi / 4

PHASE_90 = np.pi / 2

PHASE_135 = 3 * np.pi / 4

PHASE_180 = np.pi

# ============================================================
# Experiment Parameters
# ============================================================

CONFIG = DEFAULT_CONFIG

FFT_POINTS = CONFIG.fft_points

# ============================================================
# Experiment Template
# ============================================================

experiment = ExperimentTemplate(
    chapter=2,
    experiment="exp13_phase_effect",
)

output_dir = experiment.output

# ============================================================
# Phase Report
# ============================================================

@dataclass
class PhaseReport:

    name: str

    phase: float

    signal: Signal

    spectrum: object

    statistics: object

# ============================================================
# Generate Signal
# ============================================================

def generate_signal(
    phase: float,
) -> Signal:
    """
    Generate sinusoidal signal with specified phase.
    """

    generator = SignalGenerator(CONFIG)

    signal = generator.sine(

        amplitude=CONFIG.amplitude,

        frequency=CONFIG.frequency,

        phase=phase,

    )

    signal.name = f"{int(np.degrees(phase))} Degree"

    return signal

# ============================================================
# Run One Phase
# ============================================================

def run_phase(
    phase: float,
) -> PhaseReport:
    """
    Run one phase experiment.
    """

    signal = generate_signal(
        phase,
    )

    spectrum = fft(
        signal,
    )

    statistics = analyze(
        signal,
    )

    return PhaseReport(

        name=f"phase{int(np.degrees(phase))}",

        phase=phase,

        signal=signal,

        spectrum=spectrum,

        statistics=statistics,

    )

# ============================================================
# Export Results
# ============================================================

def export_result(
    report: PhaseReport,
    output_dir: Path,
) -> None:
    """
    Export experiment results.
    """

    export_signal_csv(

        report.signal,

        output_dir /
        f"{report.name}_signal.csv",

    )

    export_spectrum_csv(

        report.spectrum,

        output_dir /
        f"{report.name}_spectrum.csv",

    )

    export_statistics_csv(

        report.statistics,

        output_dir /
        f"{report.name}_statistics.csv",

    )

# ============================================================
# Draw Figures
# ============================================================

def draw_result(
    original: Signal,
    report: PhaseReport,
    output_dir: Path,
) -> None:
    """
    Draw all figures.
    """

    # --------------------------------------------------------
    # Time-domain comparison
    # --------------------------------------------------------

    manager = plot_compare(

        original,

        report.signal,

        title=f"{int(np.degrees(report.phase))} Degree",

        label1="0 Degree",

        label2=f"{int(np.degrees(report.phase))} Degree",

    )

    manager.grid()

    manager.save(

        output_dir /
        f"{report.name}_compare.png",

    )

    manager.close()

    # --------------------------------------------------------
    # Windowed signal
    # --------------------------------------------------------

    manager = plot_signal(

        report.signal,

        title=f"{int(np.degrees(report.phase))} Degree Signal",

    )

    manager.grid()

    manager.save(

        output_dir /
        f"{report.name}_signal.png",

    )

    manager.close()

    # --------------------------------------------------------
    # Spectrum
    # --------------------------------------------------------

    manager = plot_spectrum(

        report.spectrum,

        title=f"{int(np.degrees(report.phase))} Degree Spectrum",

    )

    manager.grid()

    manager.save(

        output_dir /
        f"{report.name}_spectrum.png",

    )

    manager.close()

# ============================================================
# Print Report
# ============================================================

def print_report(
    report: PhaseReport,
) -> None:
    """
    Print experiment report.
    """

    statistics = report.statistics

    spectrum = report.spectrum

    print("=" * 60)

    print(
        f"Phase : {int(np.degrees(report.phase))} Degree"
    )

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

    print()
    print("=" * 60)
    print("Communication_Principle_Python")
    print("Experiment 13")
    print("Phase Effect on Spectrum")
    print("=" * 60)
    print()

    # --------------------------------------------------------
    # Original Signal (0 Degree)
    # --------------------------------------------------------

    original_signal = generate_signal(PHASE_0)

    export_signal_csv(
        original_signal,
        output_dir / "original_signal.csv",
    )

    manager = plot_signal(
        original_signal,
        title="Original Signal (0 Degree)",
    )

    manager.grid()

    manager.save(
        output_dir / "original_signal.png",
    )

    manager.close()

    # --------------------------------------------------------
    # Phase List
    # --------------------------------------------------------

    phase_list = [

        PHASE_0,

        PHASE_45,

        PHASE_90,

        PHASE_135,

        PHASE_180,

    ]

    reports = []

    # --------------------------------------------------------
    # Run Experiment
    # --------------------------------------------------------

    for phase in phase_list:

        report = run_phase(
            phase,
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
            "Phase,"
            "PeakFrequency,"
            "PeakMagnitude,"
            "Energy,"
            "Power\n"
        )

        for report in reports:

            fp.write(

                f"{int(np.degrees(report.phase))},"

                f"{report.spectrum.peak_frequency:.6f},"

                f"{report.spectrum.peak_magnitude:.6f},"

                f"{report.statistics.energy:.6f},"

                f"{report.statistics.power:.6f}\n"

            )

    # --------------------------------------------------------
    # Summary JSON
    # --------------------------------------------------------

    import json

    summary_json = output_dir / "summary.json"

    summary = []

    for report in reports:

        summary.append({

            "phase_degree":

                int(np.degrees(report.phase)),

            "peak_frequency":

                report.spectrum.peak_frequency,

            "peak_magnitude":

                report.spectrum.peak_magnitude,

            "energy":

                report.statistics.energy,

            "power":

                report.statistics.power,

        })

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

    # --------------------------------------------------------
    # Finish
    # --------------------------------------------------------

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


