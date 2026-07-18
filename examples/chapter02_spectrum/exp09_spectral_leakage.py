"""
Experiment 09
=============

Experiment:
    Spectral Leakage

Chapter:
    Chapter 02 Spectrum Analysis

Project:
    Communication_Principle_Python

Author:
    Communication_Principle_Python

Version:
    v1.0
"""

from __future__ import annotations

import json
from pathlib import Path

from communication.config import ExperimentConfig
from communication.paths import experiment_output_dir

from communication.signals import SignalGenerator

from communication.spectrum import (
    fft,
    peak_frequency,
    peak_magnitude,
)

from communication.plotting import (
    plot_signal,
    plot_spectrum,
)

from communication.export import (
    export_signal_csv,
)

# ==========================================================
# Experiment Parameters
# ==========================================================

SAMPLING_FREQUENCY = 1000

AMPLITUDE = 1.0

DURATION = 0.5

FFT_POINTS = 2048

# ----------------------------------------------------------
# 为了演示频谱泄漏
#
# 100Hz：
#     FFT整数点，不产生明显泄漏
#
# 105.5Hz：
#     FFT非整数点，产生明显泄漏
# ----------------------------------------------------------

REFERENCE_FREQUENCY = 100.0

LEAKAGE_FREQUENCY = 105.5


# ==========================================================
# Generate Signal
# ==========================================================

def build_signal(
    frequency: float,
):
    """
    Generate sinusoidal signal.
    """

    config = ExperimentConfig(

        sampling_frequency=SAMPLING_FREQUENCY,

        duration=DURATION,

        amplitude=AMPLITUDE,

        frequency=frequency,

        phase=0.0,

        fft_points=FFT_POINTS,

    )

    generator = SignalGenerator(config)

    return generator.sine()


# ==========================================================
# Run One Case
# ==========================================================

def run_case(
    frequency: float,
    name: str,
    output_dir: Path,
):

    """
    Run one experiment.
    """

    signal = build_signal(frequency)

    spectrum = fft(

        signal,

        fft_points=FFT_POINTS,

    )

    # ------------------------------------------------------
    # Time-domain Figure
    # ------------------------------------------------------

    figure = plot_signal(

        signal,

        title=f"{name} Time Signal",

    )

    figure.grid()

    figure.save(

        output_dir /

        f"{name}_time.png",

    )

    # ------------------------------------------------------
    # Spectrum Figure
    # ------------------------------------------------------

    figure = plot_spectrum(

        spectrum,

        title=f"{name} Spectrum",

    )

    figure.grid()

    figure.save(

        output_dir /

        f"{name}_spectrum.png",

    )

    # ------------------------------------------------------
    # Export CSV
    # ------------------------------------------------------

    export_signal_csv(

        signal,

        output_dir /

        f"{name}_signal.csv",

    )

    export_signal_csv(

        spectrum,

        output_dir /

        f"{name}_spectrum.csv",

    )

    report = {

        "signal_name": name,

        "frequency": frequency,

        "sampling_frequency": SAMPLING_FREQUENCY,

        "fft_points": FFT_POINTS,

        "peak_frequency":

            peak_frequency(

                spectrum,

            ),

        "peak_magnitude":

            peak_magnitude(

                spectrum,

            ),

    }

    with open(

        output_dir /

        f"{name}_report.json",

        "w",

        encoding="utf-8",

    ) as fp:

        json.dump(

            report,

            fp,

            indent=4,

            ensure_ascii=False,

        )

    return report

# ==========================================================
# Main
# ==========================================================

def main():
    """
    Main entry of Experiment 09.
    """

    output_dir = experiment_output_dir(
        chapter=2,
        experiment="exp09_spectral_leakage",
    )

    print("=" * 60)
    print("Experiment 09")
    print("Spectral Leakage")
    print("=" * 60)
    print()

    reports = []

    print("Case 1 : Integer-bin Frequency")
    reports.append(
        run_case(
            frequency=REFERENCE_FREQUENCY,
            name="reference",
            output_dir=output_dir,
        )
    )

    print("Case 2 : Non-integer-bin Frequency")
    reports.append(
        run_case(
            frequency=LEAKAGE_FREQUENCY,
            name="leakage",
            output_dir=output_dir,
        )
    )

    # ------------------------------------------------------
    # Export Summary
    # ------------------------------------------------------

    summary_file = output_dir / "summary.json"

    with open(
        summary_file,
        "w",
        encoding="utf-8",
    ) as fp:

        json.dump(
            reports,
            fp,
            indent=4,
            ensure_ascii=False,
        )

    # ------------------------------------------------------
    # Export CSV
    # ------------------------------------------------------

    csv_file = output_dir / "summary.csv"

    with open(
        csv_file,
        "w",
        encoding="utf-8",
    ) as fp:

        fp.write(
            "Signal,"
            "Frequency,"
            "Peak Frequency,"
            "Peak Magnitude\n"
        )

        for item in reports:

            fp.write(

                f"{item['signal_name']},"

                f"{item['frequency']:.4f},"

                f"{item['peak_frequency']:.6f},"

                f"{item['peak_magnitude']:.6f}\n"

            )

    # ------------------------------------------------------
    # Console Report
    # ------------------------------------------------------

    print()

    print("-" * 72)

    print("Experiment Summary")

    print("-" * 72)

    print(
        f"{'Signal':<15}"
        f"{'Input(Hz)':>12}"
        f"{'Peak(Hz)':>15}"
        f"{'Magnitude':>15}"
    )

    print("-" * 72)

    for item in reports:

        print(

            f"{item['signal_name']:<15}"

            f"{item['frequency']:>12.3f}"

            f"{item['peak_frequency']:>15.6f}"

            f"{item['peak_magnitude']:>15.6f}"

        )

    print("-" * 72)

    print()

    print("Experiment Conclusion")

    print("---------------------")

    print(
        "1. Integer-bin frequencies produce highly concentrated FFT spectra."
    )

    print(
        "2. Non-integer-bin frequencies spread energy into adjacent bins."
    )

    print(
        "3. This phenomenon is called Spectral Leakage."
    )

    print(
        "4. Spectral Leakage is caused by finite-length observation."
    )

    print(
        "5. Window functions can effectively suppress spectral leakage."
    )

    print()

    print("Output Directory")

    print(output_dir)

    print()

    print("Experiment Finished.")


# ==========================================================
# Program Entry
# ==========================================================

if __name__ == "__main__":

    main()
