"""
Experiment 07
=============

Experiment:
    Single-Sided Spectrum and Double-Sided Spectrum

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
    single_side,
    double_side,
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

SIGNAL_FREQUENCY = 100

AMPLITUDE = 1.0

DURATION = 0.5

FFT_POINTS = 2048

# ==========================================================
# Generate Signal
# ==========================================================


def build_signal():

    """
    Generate experiment signal.
    """

    config = ExperimentConfig(

        sampling_frequency=SAMPLING_FREQUENCY,

        duration=DURATION,

        amplitude=AMPLITUDE,

        frequency=SIGNAL_FREQUENCY,

        phase=0.0,

        fft_points=FFT_POINTS,

    )

    generator = SignalGenerator(config)

    return generator.sine()


# ==========================================================
# Run Experiment
# ==========================================================


def run_experiment(
    output_dir: Path,
):

    """
    Run Experiment 07.
    """

    signal = build_signal()

    spectrum = fft(

        signal,

        fft_points=FFT_POINTS,

    )

    single = single_side(

        spectrum,

    )

    double = double_side(

        spectrum,

    )

    # ------------------------------------------------------
    # Time Domain
    # ------------------------------------------------------

    figure = plot_signal(

        signal,

        title="Time Domain Signal",

    )

    figure.grid()

    figure.save(

        output_dir /

        "time_signal.png",

    )

    # ------------------------------------------------------
    # Single-Sided Spectrum
    # ------------------------------------------------------

    figure = plot_spectrum(

        single,

        title="Single-Sided Spectrum",

    )

    figure.grid()

    figure.save(

        output_dir /

        "single_side.png",

    )

    # ------------------------------------------------------
    # Double-Sided Spectrum
    # ------------------------------------------------------

    figure = plot_spectrum(

        double,

        title="Double-Sided Spectrum",

    )

    figure.grid()

    figure.save(

        output_dir /

        "double_side.png",

    )

    # ------------------------------------------------------
    # Export CSV
    # ------------------------------------------------------

    export_signal_csv(

        signal,

        output_dir /

        "signal.csv",

    )

    export_signal_csv(

        single,

        output_dir /

        "single_side.csv",

    )

    export_signal_csv(

        double,

        output_dir /

        "double_side.csv",

    )

    report = {

        "sampling_frequency":

            SAMPLING_FREQUENCY,

        "signal_frequency":

            SIGNAL_FREQUENCY,

        "fft_points":

            FFT_POINTS,

        "single_peak_frequency":

            peak_frequency(single),

        "single_peak_magnitude":

            peak_magnitude(single),

        "double_peak_frequency":

            peak_frequency(double),

        "double_peak_magnitude":

            peak_magnitude(double),

    }

    with open(

        output_dir /

        "report.json",

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
    Main entry of Experiment 07.
    """

    output_dir = experiment_output_dir(
        chapter=2,
        experiment="exp07_single_double_side",
    )

    print("=" * 60)
    print("Experiment 07")
    print("Single-Sided Spectrum and Double-Sided Spectrum")
    print("=" * 60)
    print()

    report = run_experiment(
        output_dir=output_dir,
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
            report,
            fp,
            indent=4,
            ensure_ascii=False,
        )

    # ------------------------------------------------------
    # Console Report
    # ------------------------------------------------------

    print("-" * 70)
    print("Experiment Summary")
    print("-" * 70)

    print(
        f"Sampling Frequency : "
        f"{report['sampling_frequency']} Hz"
    )

    print(
        f"Signal Frequency   : "
        f"{report['signal_frequency']} Hz"
    )

    print(
        f"FFT Points         : "
        f"{report['fft_points']}"
    )

    print()

    print("Single-Sided Spectrum")

    print(
        f"Peak Frequency : "
        f"{report['single_peak_frequency']:.6f} Hz"
    )

    print(
        f"Peak Magnitude : "
        f"{report['single_peak_magnitude']:.6f}"
    )

    print()

    print("Double-Sided Spectrum")

    print(
        f"Peak Frequency : "
        f"{report['double_peak_frequency']:.6f} Hz"
    )

    print(
        f"Peak Magnitude : "
        f"{report['double_peak_magnitude']:.6f}"
    )

    print()

    print("-" * 70)

    print("Experiment Conclusion")

    print("-" * 70)

    print(
        "1. Real-valued signals produce conjugate symmetric spectra."
    )

    print(
        "2. The double-sided spectrum contains both positive and negative frequencies."
    )

    print(
        "3. The single-sided spectrum keeps only the positive-frequency half."
    )

    print(
        "4. For real signals, the single-sided spectrum is usually used for engineering analysis."
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

