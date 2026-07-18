"""
============================================================
Communication_Principle_Python

Experiment 14
Amplitude Effect on Spectrum

Version
-------
3.0.0

Compatible SDK
--------------
Communication_Principle_Python API Freeze v1.0

Description
-----------
Study the influence of signal amplitude on FFT spectrum.

Author
------
Communication_Principle_Python Textbook Project
============================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import json
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

FREQUENCY = CONFIG.frequency

PHASE = CONFIG.phase


AMPLITUDE_05 = 0.5
AMPLITUDE_10 = 1.0
AMPLITUDE_20 = 2.0
AMPLITUDE_40 = 4.0

# ============================================================
# Amplitude Report
# ============================================================

@dataclass
class AmplitudeReport:

    amplitude: float

    statistics: object

    spectrum: object

    signal: Signal

# ============================================================
# Generate Signal
# ============================================================

def generate_signal(
    amplitude: float,
) -> Signal:
    """
    Generate sinusoidal signal with specified amplitude.
    """

    generator = SignalGenerator(CONFIG)

    signal = generator.sine(
        amplitude=amplitude,
        frequency=FREQUENCY,
        phase=PHASE,
    )

    signal.name = f"Amplitude {amplitude:.1f}"

    return signal

# ============================================================
# Run One Experiment
# ============================================================

def run_amplitude(
    amplitude: float,
) -> AmplitudeReport:
    """
    Run one amplitude experiment.
    """

    signal = generate_signal(
        amplitude,
    )

    spectrum = fft(
        signal,
    )

    statistics = analyze(
        signal,
    )

    return AmplitudeReport(
        amplitude=amplitude,
        statistics=statistics,
        spectrum=spectrum,
        signal=signal,
    )

# ============================================================
# Export Results
# ============================================================

def export_result(
    report: AmplitudeReport,
    output_dir: Path,
) -> None:
    """
    Export experiment CSV files.
    """

    name = f"amp_{str(report.amplitude).replace('.', '_')}"

    export_signal_csv(
        report.signal,
        output_dir / f"{name}_signal.csv",
    )

    export_spectrum_csv(
        report.spectrum,
        output_dir / f"{name}_spectrum.csv",
    )

    export_statistics_csv(
        report.statistics,
        output_dir / f"{name}_statistics.csv",
    )

# ============================================================
# Draw Figures
# ============================================================

def draw_result(
    original: Signal,
    report: AmplitudeReport,
    output_dir: Path,
) -> None:
    """
    Draw experiment figures.
    """

    name = f"amp_{str(report.amplitude).replace('.', '_')}"

    # --------------------------------------------------------
    # Comparison
    # --------------------------------------------------------

    manager = plot_compare(
        original,
        report.signal,
        title=f"Amplitude = {report.amplitude}",
        label1="Reference",
        label2=f"A={report.amplitude}",
    )

    manager.save(
        output_dir / f"{name}_compare.png",
    )

    manager.close()

    # --------------------------------------------------------
    # Signal
    # --------------------------------------------------------

    manager = plot_signal(
        report.signal,
        title=f"Amplitude {report.amplitude}",
    )

    manager.save(
        output_dir / f"{name}_signal.png",
    )

    manager.close()

    # --------------------------------------------------------
    # Spectrum
    # --------------------------------------------------------

    manager = plot_spectrum(
        report.spectrum,
        title=f"Amplitude {report.amplitude} Spectrum",
    )

    manager.save(
        output_dir / f"{name}_spectrum.png",
    )

    manager.close()

# ============================================================
# Print Report
# ============================================================

def print_report(
    report: AmplitudeReport,
) -> None:
    """
    Print experiment report.
    """

    statistics = report.statistics
    spectrum = report.spectrum

    print("=" * 60)
    print(f"Amplitude : {report.amplitude}")
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
        experiment="exp14_amplitude_effect",
    )

    print()
    print("=" * 60)
    print("Communication_Principle_Python")
    print("Experiment 14")
    print("Amplitude Effect on Spectrum")
    print("=" * 60)
    print()

    # --------------------------------------------------------
    # Generate Reference Signal
    # --------------------------------------------------------

    reference_signal = generate_signal(
        AMPLITUDE_10,
    )

    export_signal_csv(
        reference_signal,
        output_dir / "reference_signal.csv",
    )

    manager = plot_signal(
        reference_signal,
        title="Reference Signal",
    )

    manager.grid()

    manager.save(
        output_dir / "reference_signal.png",
    )

    manager.close()

    # --------------------------------------------------------
    # Amplitude List
    # --------------------------------------------------------

    amplitude_list = [

        AMPLITUDE_05,

        AMPLITUDE_10,

        AMPLITUDE_20,

        AMPLITUDE_40,

    ]

    reports = []

    # --------------------------------------------------------
    # Run Experiments
    # --------------------------------------------------------

    for amplitude in amplitude_list:

        report = run_amplitude(
            amplitude,
        )

        reports.append(report)

        export_result(
            report,
            output_dir,
        )

        draw_result(
            reference_signal,
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

            "Amplitude,"

            "PeakFrequency,"

            "PeakMagnitude,"

            "Energy,"

            "Power\n"

        )

        for report in reports:

            fp.write(

                f"{report.amplitude:.2f},"

                f"{report.spectrum.peak_frequency:.6f},"

                f"{report.spectrum.peak_magnitude:.6f},"

                f"{report.statistics.energy:.6f},"

                f"{report.statistics.power:.6f}\n"

            )

    # --------------------------------------------------------
    # Summary JSON
    # --------------------------------------------------------

    summary_json = output_dir / "summary.json"

    summary = []

    for report in reports:

        summary.append({

            "amplitude":

                report.amplitude,

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

