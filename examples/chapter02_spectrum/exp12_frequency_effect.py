"""
============================================================
Communication_Principle_Python

Experiment 12

Signal Frequency Effect on Spectrum

Version
-------
3.0.0

Compatible SDK
--------------
Communication_Principle_Python API Freeze v1.0

Description
-----------
Study the influence of signal frequency on FFT spectrum.

Author
------
Communication_Principle_Python Textbook Project
============================================================
"""

from __future__ import annotations

from dataclasses import dataclass

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
)

from communication.export import (
    export_signal_csv,
    export_spectrum_csv,
    export_statistics_csv,
)


# ==========================================================
# Experiment Template
# ==========================================================

experiment = ExperimentTemplate(
    chapter=2,
    experiment="exp12_frequency_effect",
)

output_dir = experiment.output


# ==========================================================
# Experiment Parameters
# ==========================================================

CONFIG = DEFAULT_CONFIG

FFT_POINTS = CONFIG.fft_points

TEST_FREQUENCIES = [

    50,

    100,

    200,

    500,

    1000,

]

# ==========================================================
# Frequency Report
# ==========================================================

@dataclass
class FrequencyReport:
    """
    Experiment result of one frequency.
    """

    frequency: float

    statistics: object

    spectrum: object

    signal: Signal

# ==========================================================
# Signal Generator
# ==========================================================

def generate_signal(
    frequency: float,
) -> Signal:
    """
    Generate sine signal with specified frequency.
    """

    generator = SignalGenerator(CONFIG)

    signal = generator.sine(

        amplitude=CONFIG.amplitude,

        frequency=frequency,

        phase=CONFIG.phase,

    )

    signal.name = f"{frequency:.0f} Hz"

    return signal

# ==========================================================
# Run One Experiment
# ==========================================================

def run_case(
    frequency: float,
) -> FrequencyReport:
    """
    Run one frequency experiment.

    Parameters
    ----------
    frequency
        Signal frequency.

    Returns
    -------
    FrequencyReport
    """

    # --------------------------------------------------
    # Generate Signal
    # --------------------------------------------------

    signal = generate_signal(
        frequency,
    )

    # --------------------------------------------------
    # FFT
    # --------------------------------------------------

    spectrum = fft(
        signal,
        fft_points=FFT_POINTS,
    )

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    statistics = analyze(
        signal,
    )

    return FrequencyReport(

        frequency=frequency,

        statistics=statistics,

        spectrum=spectrum,

        signal=signal,

    )


# ==========================================================
# Export Result
# ==========================================================

def export_result(
    report: FrequencyReport,
    output_dir,
) -> None:
    """
    Export CSV files.
    """

    prefix = f"freq{int(report.frequency)}"

    export_signal_csv(

        report.signal,

        output_dir / f"{prefix}_signal.csv",

    )

    export_spectrum_csv(

        report.spectrum,

        output_dir / f"{prefix}_spectrum.csv",

    )

    export_statistics_csv(

        report.statistics,

        output_dir / f"{prefix}_statistics.csv",

    )


# ==========================================================
# Draw Figures
# ==========================================================

def draw_result(
    report: FrequencyReport,
    output_dir,
) -> None:
    """
    Draw figures.
    """

    prefix = f"freq{int(report.frequency)}"

    # --------------------------------------------------
    # Time Domain
    # --------------------------------------------------

    manager = plot_signal(

        report.signal,

        title=f"{report.frequency:.0f} Hz Signal",

    )

    manager.grid()

    manager.save(

        output_dir / f"{prefix}_signal.png",

    )

    manager.close()

    # --------------------------------------------------
    # Spectrum
    # --------------------------------------------------

    manager = plot_spectrum(

        report.spectrum,

        title=f"{report.frequency:.0f} Hz Spectrum",

    )

    manager.grid()

    manager.save(

        output_dir / f"{prefix}_spectrum.png",

    )

    manager.close()

# ==========================================================
# Print Report
# ==========================================================

def print_report(
    report: FrequencyReport,
) -> None:
    """
    Print experiment report.
    """

    statistics = report.statistics
    spectrum = report.spectrum

    print("=" * 60)
    print(f"Signal Frequency : {report.frequency:.0f} Hz")
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

# ==========================================================
# Main
# ==========================================================

def main() -> None:
    """
    Main experiment.
    """

    print()
    print("=" * 60)
    print("Communication_Principle_Python")
    print("Experiment 12")
    print("Signal Frequency Effect on Spectrum")
    print("=" * 60)
    print()

    reports = []

    # ------------------------------------------------------
    # Run Experiments
    # ------------------------------------------------------

    for frequency in TEST_FREQUENCIES:

        report = run_case(
            frequency,
        )

        reports.append(report)

        export_result(
            report,
            output_dir,
        )

        draw_result(
            report,
            output_dir,
        )

        print_report(
            report,
        )

    # ------------------------------------------------------
    # Summary JSON
    # ------------------------------------------------------

    import json

    summary = []

    for report in reports:

        summary.append({

            "frequency": report.frequency,

            "peak_frequency":
                report.spectrum.peak_frequency,

            "peak_magnitude":
                report.spectrum.peak_magnitude,

            "resolution":
                report.spectrum.resolution,

        })

    with open(

        output_dir / "summary.json",

        "w",

        encoding="utf-8",

    ) as fp:

        json.dump(

            summary,

            fp,

            indent=4,

            ensure_ascii=False,

        )

    # ------------------------------------------------------
    # Summary CSV
    # ------------------------------------------------------

    with open(

        output_dir / "summary.csv",

        "w",

        encoding="utf-8",

    ) as fp:

        fp.write(

            "Frequency,"
            "PeakFrequency,"
            "PeakMagnitude,"
            "Resolution\n"

        )

        for report in reports:

            fp.write(

                f"{report.frequency:.0f},"

                f"{report.spectrum.peak_frequency:.6f},"

                f"{report.spectrum.peak_magnitude:.6f},"

                f"{report.spectrum.resolution:.6f}\n"

            )

    print("=" * 60)
    print("Experiment Finished Successfully.")
    print(f"Output Directory : {output_dir}")
    print("=" * 60)

    experiment.finish()

# ==========================================================
# Script Entry
# ==========================================================

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