"""
Experiment 08
=============

Experiment:
    Phase Spectrum

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
    phase_spectrum,
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

PHASE = 30.0

DURATION = 0.5

FFT_POINTS = 2048


# ==========================================================
# Generate Signal
# ==========================================================

def build_signal():
    """
    Generate a sinusoidal signal with an initial phase.
    """

    config = ExperimentConfig(

        sampling_frequency=SAMPLING_FREQUENCY,

        duration=DURATION,

        amplitude=AMPLITUDE,

        frequency=SIGNAL_FREQUENCY,

        phase=PHASE,

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

    signal = build_signal()

    spectrum = fft(

        signal,

        fft_points=FFT_POINTS,

    )

    phase = phase_spectrum(

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
    # Amplitude Spectrum
    # ------------------------------------------------------

    figure = plot_spectrum(

        spectrum,

        title="Amplitude Spectrum",

    )

    figure.grid()

    figure.save(

        output_dir /

        "amplitude_spectrum.png",

    )

    # ------------------------------------------------------
    # Phase Spectrum
    # ------------------------------------------------------

    figure = plot_spectrum(

        phase,

        title="Phase Spectrum",

        ylabel="Phase (rad)",

    )

    figure.grid()

    figure.save(

        output_dir /

        "phase_spectrum.png",

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

        spectrum,

        output_dir /

        "amplitude_spectrum.csv",

    )

    export_signal_csv(

        phase,

        output_dir /

        "phase_spectrum.csv",

    )

    report = {

        "sampling_frequency":

            SAMPLING_FREQUENCY,

        "signal_frequency":

            SIGNAL_FREQUENCY,

        "signal_phase":

            PHASE,

        "fft_points":

            FFT_POINTS,

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
    Main entry of Experiment 08.
    """

    output_dir = experiment_output_dir(
        chapter=2,
        experiment="exp08_phase_spectrum",
    )

    print("=" * 60)
    print("Experiment 08")
    print("Phase Spectrum")
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
        f"Initial Phase      : "
        f"{report['signal_phase']} degree"
    )

    print(
        f"FFT Points         : "
        f"{report['fft_points']}"
    )

    print()

    print(
        f"Peak Frequency : "
        f"{report['peak_frequency']:.6f} Hz"
    )

    print(
        f"Peak Magnitude : "
        f"{report['peak_magnitude']:.6f}"
    )

    print()

    print("-" * 70)

    print("Experiment Conclusion")

    print("-" * 70)

    print(
        "1. The phase spectrum describes the phase shift of every frequency component."
    )

    print(
        "2. Amplitude spectrum and phase spectrum jointly determine the original signal."
    )

    print(
        "3. Different initial phases produce different phase spectra."
    )

    print(
        "4. Phase information is essential for accurate signal reconstruction."
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
