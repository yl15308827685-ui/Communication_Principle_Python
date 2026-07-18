"""
Experiment 06
=============

Experiment:
    Zero Padding

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

ORIGINAL_SAMPLES = 500

FFT_POINTS = [
    500,
    1024,
    2048,
    4096,
    8192,
]

SAMPLING_FREQUENCY = 1000

SIGNAL_FREQUENCY = 100

AMPLITUDE = 1.0

DURATION = ORIGINAL_SAMPLES / SAMPLING_FREQUENCY

# ==========================================================
# Run One Case
# ==========================================================


def run_case(
    fft_points: int,
    output_dir: Path,
) -> dict:
    """
    Run one Zero Padding experiment.

    Parameters
    ----------
    fft_points
        FFT length after zero padding.

    output_dir
        Output directory.

    Returns
    -------
    dict
        Experiment report.
    """

    config = ExperimentConfig(

        sampling_frequency=SAMPLING_FREQUENCY,

        duration=DURATION,

        amplitude=AMPLITUDE,

        frequency=SIGNAL_FREQUENCY,

        phase=0.0,

        fft_points=fft_points,

    )

    generator = SignalGenerator(config)

    signal = generator.sine()

    spectrum = fft(
        signal,
        fft_points=fft_points,
    )

    # ------------------------------------------------------
    # Time-domain figure
    # ------------------------------------------------------

    figure = plot_signal(

        signal,

        title=f"Time Signal (FFT={fft_points})",

    )

    figure.grid()

    figure.save(

        output_dir /

        f"time_{fft_points}.png"

    )

    # ------------------------------------------------------
    # Spectrum
    # ------------------------------------------------------

    figure = plot_spectrum(

        spectrum,

        title=f"Zero Padding FFT={fft_points}",

    )

    figure.grid()

    figure.save(

        output_dir /

        f"spectrum_{fft_points}.png"

    )

    # ------------------------------------------------------
    # Export Signal
    # ------------------------------------------------------

    export_signal_csv(

        signal,

        output_dir /

        f"signal_{fft_points}.csv",

    )

    export_signal_csv(

        spectrum,

        output_dir /

        f"spectrum_{fft_points}.csv",

    )

    # ------------------------------------------------------
    # Report
    # ------------------------------------------------------

    report = {

        "original_samples": ORIGINAL_SAMPLES,

        "fft_points": fft_points,

        "zero_padding":

            fft_points - ORIGINAL_SAMPLES,

        "sampling_frequency":

            SAMPLING_FREQUENCY,

        "signal_frequency":

            SIGNAL_FREQUENCY,

        "peak_frequency":

            peak_frequency(

                spectrum,

            ),

        "peak_magnitude":

            peak_magnitude(

                spectrum,

            ),

    }

    report_file = (

        output_dir /

        f"report_{fft_points}.json"

    )

    with open(

        report_file,

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
    Main entry of Experiment 06.
    """

    output_dir = experiment_output_dir(
        chapter=2,
        experiment="exp06_zero_padding",
    )

    summary = []

    print("=" * 60)
    print("Experiment 06")
    print("Zero Padding")
    print("=" * 60)
    print()

    for fft_points in FFT_POINTS:

        print(f"Running FFT = {fft_points}")

        report = run_case(
            fft_points=fft_points,
            output_dir=output_dir,
        )

        summary.append(report)

    # ------------------------------------------------------
    # Export Summary CSV
    # ------------------------------------------------------

    csv_file = output_dir / "zero_padding.csv"

    with open(
        csv_file,
        "w",
        encoding="utf-8",
    ) as fp:

        fp.write(
            "Original Samples,"
            "FFT Points,"
            "Zero Padding,"
            "Peak Frequency (Hz),"
            "Peak Magnitude\n"
        )

        for item in summary:

            fp.write(

                f"{item['original_samples']},"

                f"{item['fft_points']},"

                f"{item['zero_padding']},"

                f"{item['peak_frequency']:.6f},"

                f"{item['peak_magnitude']:.6f}\n"

            )

    # ------------------------------------------------------
    # Export Summary JSON
    # ------------------------------------------------------

    summary_file = output_dir / "summary.json"

    with open(
        summary_file,
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
    # Console Report
    # ------------------------------------------------------

    print()
    print("-" * 70)
    print("Zero Padding Summary")
    print("-" * 70)

    print(
        f"{'FFT':>8}"
        f"{'Padding':>12}"
        f"{'Peak(Hz)':>15}"
        f"{'Magnitude':>15}"
    )

    print("-" * 70)

    for item in summary:

        print(

            f"{item['fft_points']:>8}"

            f"{item['zero_padding']:>12}"

            f"{item['peak_frequency']:>15.6f}"

            f"{item['peak_magnitude']:>15.6f}"

        )

    print("-" * 70)

    print()

    print("Experiment Finished.")

    print(f"Output Directory : {output_dir}")

    print()

    print("Experiment Conclusion")

    print("---------------------")

    print(
        "1. Zero Padding makes the spectrum smoother."
    )

    print(
        "2. Zero Padding helps locate the peak frequency."
    )

    print(
        "3. Zero Padding DOES NOT increase the actual frequency resolution."
    )

    print(
        "4. Zero Padding DOES NOT create new frequency components."
    )


# ==========================================================
# Program Entry
# ==========================================================

if __name__ == "__main__":

    main()
