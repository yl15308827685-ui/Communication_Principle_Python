"""
============================================================
Communication_Principle_Python

Experiment 11
FFT Length Effect

Version
-------
3.0.0

Compatible SDK
--------------
Communication_Principle_Python API Freeze v1.0

Description
-----------
Study the influence of FFT length on spectrum display and
frequency resolution.

Author
------
Communication_Principle_Python Textbook Project
============================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from pathlib import Path

import json

from communication.config import DEFAULT_CONFIG

from communication.models import Signal
from communication.models import Spectrum

from communication.signals import SignalGenerator

from communication.analysis import analyze

from communication.spectrum import (
    fft,
    peak_frequency,
    peak_magnitude,
)

from communication.export import (
    export_signal_csv,
    export_spectrum_csv,
    export_statistics_csv,
)

from communication.plotting import (
    plot_signal,
    plot_spectrum,
)

from examples.template import ExperimentTemplate

from examples.spectrum_common import (
    build_report,
    save_report,
)

# ==========================================================
# Experiment
# ==========================================================

experiment = ExperimentTemplate(
    chapter=2,
    experiment="exp11_fft_length",
)

output_dir = experiment.output

# ==========================================================
# Parameters
# ==========================================================

CONFIG = DEFAULT_CONFIG

FFT_LENGTHS = [
    512,
    1024,
    2048,
    4096,
]

# ==========================================================
# Result Object
# ==========================================================


@dataclass
class FFTReport:
    """
    FFT experiment result.
    """

    fft_points: int

    signal: Signal

    spectrum: Spectrum

    statistics: object


# ==========================================================
# Generate Test Signal
# ==========================================================

def generate_test_signal() -> Signal:
    """
    Generate experiment signal.
    """

    generator = SignalGenerator(CONFIG)

    signal = generator.sine(
        amplitude=CONFIG.amplitude,
        frequency=CONFIG.frequency,
        phase=CONFIG.phase,
    )

    signal.name = "Original Signal"

    return signal


# ==========================================================
# Run One FFT Experiment
# ==========================================================

def run_case(
    signal: Signal,
    fft_points: int,
) -> FFTReport:
    """
    Run one FFT-length experiment.

    Parameters
    ----------
    signal
        Input signal.

    fft_points
        FFT length.

    Returns
    -------
    FFTReport
    """

    spectrum = fft(
        signal,
        fft_points=fft_points,
    )

    statistics = analyze(
        signal,
    )

    return FFTReport(
        fft_points=fft_points,
        signal=signal,
        spectrum=spectrum,
        statistics=statistics,
    )


# ==========================================================
# Export Result
# ==========================================================

def export_result(
    report: FFTReport,
) -> None:
    """
    Export CSV and JSON files.
    """

    prefix = f"fft{report.fft_points}"

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

    spectrum_report = build_report(
        report.spectrum,
        report.fft_points,
    )

    save_report(
        spectrum_report,
        output_dir / f"{prefix}_report.json",
    )

# ==========================================================
# Draw Result
# ==========================================================

def draw_result(
    report: FFTReport,
) -> None:
    """
    Draw experiment figures.
    """

    prefix = f"fft{report.fft_points}"

    # ------------------------------------------------------
    # Time-domain Signal
    # ------------------------------------------------------

    manager = plot_signal(
        report.signal,
        title=f"Time Signal ({report.fft_points} Points)",
    )

    manager.grid()

    manager.save(
        output_dir / f"{prefix}_signal.png",
    )

    manager.close()

    # ------------------------------------------------------
    # Spectrum
    # ------------------------------------------------------

    manager = plot_spectrum(
        report.spectrum,
        title=f"FFT Spectrum ({report.fft_points} Points)",
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
    report: FFTReport,
) -> dict:
    """
    Print one experiment report.

    Returns
    -------
    dict
        Summary information.
    """

    statistics = report.statistics
    spectrum = report.spectrum

    print("=" * 60)
    print(f"FFT Length : {report.fft_points}")
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

    return {
        "fft_points": report.fft_points,
        "frequency_resolution": spectrum.resolution,
        "peak_frequency": peak_frequency(spectrum),
        "peak_magnitude": peak_magnitude(spectrum),
    }


# ==========================================================
# Export Summary
# ==========================================================

def export_summary(
    summary: list[dict],
) -> None:
    """
    Export summary.csv and summary.json.
    """

    # ------------------------------------------------------
    # JSON
    # ------------------------------------------------------

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
    # CSV
    # ------------------------------------------------------

    with open(
        output_dir / "summary.csv",
        "w",
        encoding="utf-8",
    ) as fp:

        fp.write(
            "FFT Points,"
            "Resolution(Hz),"
            "Peak Frequency(Hz),"
            "Peak Magnitude\n"
        )

        for item in summary:

            fp.write(
                f"{item['fft_points']},"
                f"{item['frequency_resolution']:.6f},"
                f"{item['peak_frequency']:.6f},"
                f"{item['peak_magnitude']:.6f}\n"
            )

# ==========================================================
# Main Experiment
# ==========================================================

def main() -> None:
    """
    Main entry.
    """

    print()
    print("=" * 60)
    print("Communication_Principle_Python")
    print("Experiment 11")
    print("FFT Length Effect")
    print("=" * 60)
    print()

    # ------------------------------------------------------
    # Generate Test Signal
    # ------------------------------------------------------

    signal = generate_test_signal()

    export_signal_csv(
        signal,
        output_dir / "original_signal.csv",
    )

    manager = plot_signal(
        signal,
        title="Original Signal",
    )

    manager.grid()

    manager.save(
        output_dir / "original_signal.png",
    )

    manager.close()

    # ------------------------------------------------------
    # Run Experiments
    # ------------------------------------------------------

    summary = []

    for fft_points in FFT_LENGTHS:

        report = run_case(
            signal,
            fft_points,
        )

        export_result(
            report,
        )

        draw_result(
            report,
        )

        summary.append(
            print_report(
                report,
            )
        )

    # ------------------------------------------------------
    # Export Summary
    # ------------------------------------------------------

    export_summary(
        summary,
    )

    # ------------------------------------------------------
    # Console Summary
    # ------------------------------------------------------

    print("-" * 78)
    print("Experiment Summary")
    print("-" * 78)

    print(
        f"{'FFT':<12}"
        f"{'Resolution(Hz)':>18}"
        f"{'Peak(Hz)':>18}"
        f"{'Magnitude':>18}"
    )

    print("-" * 78)

    for item in summary:

        print(
            f"{item['fft_points']:<12}"
            f"{item['frequency_resolution']:>18.6f}"
            f"{item['peak_frequency']:>18.6f}"
            f"{item['peak_magnitude']:>18.6f}"
        )

    print("-" * 78)
    print()

    # ------------------------------------------------------
    # Experiment Conclusion
    # ------------------------------------------------------

    print("Experiment Conclusion")
    print("---------------------")

    print("1. Increasing FFT length improves frequency resolution.")
    print("2. Zero-padding makes the spectrum smoother.")
    print("3. FFT length does not increase actual signal information.")
    print("4. Longer FFT provides finer frequency sampling.")
    print("5. Appropriate FFT length should balance accuracy and computation.")

    print()

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

