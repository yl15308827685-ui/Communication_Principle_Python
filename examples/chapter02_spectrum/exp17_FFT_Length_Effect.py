"""
============================================================
Communication_Principle_Python

Experiment 17

FFT Length Effect

Version
-------
3.0.0

Compatible SDK
--------------
Communication_Principle_Python API Freeze v1.0

Description
-----------
Study the influence of FFT length on spectrum analysis.

Author
------
Communication_Principle_Python Textbook Project
============================================================
"""
from __future__ import annotations

import json

from dataclasses import dataclass

from pathlib import Path

import numpy as np

from communication.paths import experiment_output_dir

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
# ============================================================
# Experiment Parameters
# ============================================================

CONFIG = DEFAULT_CONFIG

FFT_LENGTHS = [

    256,

    512,

    1024,

    2048,

    4096,

]
# ============================================================
# FFT Report
# ============================================================

@dataclass
class FFTReport:

    fft_points: int

    signal: Signal

    spectrum: object

    statistics: object

# ============================================================
# Generate Test Signal
# ============================================================

def generate_signal() -> Signal:
    """
    Generate test signal.
    """

    generator = SignalGenerator(CONFIG)

    signal = generator.sine(

        amplitude=CONFIG.amplitude,

        frequency=CONFIG.frequency,

        phase=CONFIG.phase,

    )

    signal.name = "Test Signal"

    return signal
# ============================================================
# Run One FFT Experiment
# ============================================================

def run_fft(
    signal: Signal,
    fft_points: int,
) -> FFTReport:
    """
    Run one FFT experiment.
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
# ============================================================
# Export Results
# ============================================================

def export_result(
    report: FFTReport,
    output_dir: Path,
) -> None:
    """
    Export experiment results.
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

# ============================================================
# Draw Figures
# ============================================================

def draw_result(
    report: FFTReport,
    output_dir: Path,
) -> None:
    """
    Draw figures.
    """

    prefix = f"fft{report.fft_points}"

    # -----------------------------------------
    # Signal
    # -----------------------------------------

    manager = plot_signal(

        report.signal,

        title=f"FFT = {report.fft_points}",

    )

    manager.save(

        output_dir / f"{prefix}_signal.png",

    )

    manager.close()

    # -----------------------------------------
    # Spectrum
    # -----------------------------------------

    manager = plot_spectrum(

        report.spectrum,

        title=f"FFT = {report.fft_points}",

    )

    manager.save(

        output_dir / f"{prefix}_spectrum.png",

    )

    manager.close()

# ============================================================
# Print Report
# ============================================================

def print_report(
    report: FFTReport,
) -> None:
    """
    Print experiment report.
    """

    spectrum = report.spectrum

    statistics = report.statistics

    print("=" * 60)

    print(f"FFT Points : {report.fft_points}")

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
        experiment="exp17_fft_length_effect",
    )

    print()
    print("=" * 60)
    print("Communication_Principle_Python")
    print("Experiment 17")
    print("FFT Length Effect")
    print("=" * 60)
    print()

    # --------------------------------------------------------
    # Generate Test Signal
    # --------------------------------------------------------

    signal = generate_signal()

    export_signal_csv(
        signal,
        output_dir / "original_signal.csv",
    )

    manager = plot_signal(
        signal,
        title="Original Signal",
    )

    manager.save(
        output_dir / "original_signal.png",
    )

    manager.close()

    reports = []

    # --------------------------------------------------------
    # Run Experiments
    # --------------------------------------------------------

    for fft_points in FFT_LENGTHS:

        report = run_fft(

            signal,

            fft_points,

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

    # --------------------------------------------------------
    # summary.json
    # --------------------------------------------------------

    summary = []

    for report in reports:

        spectrum = report.spectrum

        summary.append(

            {

                "fft_points": report.fft_points,

                "frequency_resolution":

                    spectrum.resolution,

                "peak_frequency":

                    spectrum.peak_frequency,

                "peak_magnitude":

                    spectrum.peak_magnitude,

            }

        )

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

    # --------------------------------------------------------
    # summary.csv
    # --------------------------------------------------------

    with open(

        output_dir / "summary.csv",

        "w",

        encoding="utf-8",

    ) as fp:

        fp.write(

            "FFT Points,"

            "Frequency Resolution,"

            "Peak Frequency,"

            "Peak Magnitude\n"

        )

        for report in reports:

            spectrum = report.spectrum

            fp.write(

                f"{report.fft_points},"

                f"{spectrum.resolution:.6f},"

                f"{spectrum.peak_frequency:.6f},"

                f"{spectrum.peak_magnitude:.6f}\n"

            )

    # --------------------------------------------------------
    # Console Summary
    # --------------------------------------------------------

    print()

    print("=" * 72)

    print("Experiment Summary")

    print("=" * 72)

    print(

        f"{'FFT':<12}"

        f"{'Resolution(Hz)':>20}"

        f"{'Peak(Hz)':>18}"

        f"{'Magnitude':>18}"

    )

    print("-" * 72)

    for report in reports:

        spectrum = report.spectrum

        print(

            f"{report.fft_points:<12}"

            f"{spectrum.resolution:>20.6f}"

            f"{spectrum.peak_frequency:>18.6f}"

            f"{spectrum.peak_magnitude:>18.6f}"

        )

    print("=" * 72)

    print()

    print("Experiment Conclusion")

    print("---------------------")

    print("1. FFT点数越大，频率分辨率越高。")

    print("2. 峰值频率定位更加准确。")

    print("3. 谱线显示更加平滑。")

    print("4. FFT点数不会改变原始信号频率。")

    print("5. FFT点数增加会提高运算量。")

    print()

    print("Output Directory")

    print(output_dir)

    print()

    print("Experiment Finished.")

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

