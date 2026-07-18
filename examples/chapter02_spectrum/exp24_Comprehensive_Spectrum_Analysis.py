"""
============================================================
Communication_Principle_Python

Experiment 24

Comprehensive Spectrum Analysis

Version
-------
SDK v1.0 Frozen

Description
-----------
Course Project of Chapter 2.

Comprehensive comparison of FFT spectrum analysis,
window functions,
zero padding,
FFT length,
and frequency identification.

============================================================
"""

from __future__ import annotations

import json
import numpy as np

from dataclasses import dataclass
from pathlib import Path

from communication.config import (
    DEFAULT_CONFIG,
    ExperimentConfig,
)

from communication.models import Signal

from communication.paths import experiment_output_dir

from communication.signals import (
    SignalGenerator,
    add,
)

from communication.window import apply_window

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

MAIN_FREQUENCY = 80.0

SECOND_FREQUENCY = 160.0

THIRD_FREQUENCY = 300.0

AMPLITUDE_1 = 1.0

AMPLITUDE_2 = 0.6

AMPLITUDE_3 = 0.2

FFT_LIST = [

    1024,

    2048,

    4096,

]

WINDOW_LIST = [

    "rectangular",

    "hann",

    "hamming",

    "blackman",

]

ZERO_PADDING = [

    False,

    True,

]

@dataclass
class CourseProjectReport:

    fft_points: int

    window: str

    zero_padding: bool

    signal: Signal

    spectrum: object

    statistics: object

def generate_signal() -> Signal:
    """
    Generate three-tone signal.
    """

    config = ExperimentConfig(

        sampling_frequency=CONFIG.sampling_frequency,

        duration=CONFIG.duration,

        amplitude=1.0,

        frequency=MAIN_FREQUENCY,

        phase=0.0,

        fft_points=max(FFT_LIST),

    )

    generator = SignalGenerator(config)

    signal1 = generator.sine(

        amplitude=AMPLITUDE_1,

        frequency=MAIN_FREQUENCY,

    )

    signal2 = generator.sine(

        amplitude=AMPLITUDE_2,

        frequency=SECOND_FREQUENCY,

    )

    signal3 = generator.sine(

        amplitude=AMPLITUDE_3,

        frequency=THIRD_FREQUENCY,

    )

    signal = add(

        signal1,

        signal2,

    )

    signal = add(

        signal,

        signal3,

    )

    signal.name = "Three-Tone Signal"

    return signal

def run_project(

    fft_points: int,

    window: str,

    zero_padding: bool,

) -> CourseProjectReport:
    """
    Run comprehensive spectrum analysis.
    """

    signal = generate_signal()

    signal = apply_window(

        signal,

        window,

    )

    if zero_padding:

        fft_size = fft_points * 2

    else:

        fft_size = fft_points

    spectrum = fft(

        signal,

        fft_points=fft_size,

    )

    statistics = analyze(

        signal,

    )

    return CourseProjectReport(

        fft_points=fft_size,

        window=window,

        zero_padding=zero_padding,

        signal=signal,

        spectrum=spectrum,

        statistics=statistics,

    )

# ============================================================
# Export Result
# ============================================================

def export_result(
    report: CourseProjectReport,
    output_dir: Path,
) -> None:
    """
    Export experiment results.
    """

    suffix = "padding" if report.zero_padding else "normal"

    prefix = (
        f"{report.window}_"
        f"{report.fft_points}_"
        f"{suffix}"
    )

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
# Draw Result
# ============================================================

def draw_result(
    report: CourseProjectReport,
    output_dir: Path,
) -> None:
    """
    Draw experiment figures.
    """

    suffix = "padding" if report.zero_padding else "normal"

    prefix = (
        f"{report.window}_"
        f"{report.fft_points}_"
        f"{suffix}"
    )

    title = (
        f"{report.window.upper()} | "
        f"FFT={report.fft_points} | "
        f"{'Padding' if report.zero_padding else 'Normal'}"
    )

    manager = plot_signal(

        report.signal,

        title=title,

    )

    manager.save(

        output_dir / f"{prefix}_signal.png",

    )

    manager.close()

    manager = plot_spectrum(

        report.spectrum,

        title=title,

    )

    manager.save(

        output_dir / f"{prefix}_spectrum.png",

    )

    manager.close()

# ============================================================
# Print Report
# ============================================================

def print_report(
    report: CourseProjectReport,
) -> None:
    """
    Print experiment report.
    """

    spectrum = report.spectrum

    statistics = report.statistics

    print("=" * 80)

    print(f"Window          : {report.window}")

    print(f"FFT Points      : {report.fft_points}")

    print(f"Zero Padding    : {report.zero_padding}")

    print("-" * 80)

    print(f"Mean            : {statistics.mean:.6f}")

    print(f"RMS             : {statistics.rms:.6f}")

    print(f"Variance        : {statistics.variance:.6f}")

    print(f"Standard Dev.   : {statistics.std:.6f}")

    print(f"Peak            : {statistics.peak:.6f}")

    print(f"Peak-to-Peak    : {statistics.peak_to_peak:.6f}")

    print(f"Energy          : {statistics.energy:.6f}")

    print(f"Average Power   : {statistics.power:.6f}")

    print("-" * 80)

    print(f"Peak Frequency  : {spectrum.peak_frequency:.6f} Hz")

    print(f"Peak Magnitude  : {spectrum.peak_magnitude:.6f}")

    print(f"FFT Resolution  : {spectrum.resolution:.6f} Hz")

    print(f"FFT Bins        : {spectrum.bins}")

    print("=" * 80)

    print()

# ============================================================
# Theory
# ============================================================

def print_theory() -> None:
    """
    Print experiment theory.
    """

    print()

    print("Theory")

    print("------")

    print("1. FFT 能够识别多个频率分量。")

    print("2. 窗函数影响频谱泄漏和旁瓣高度。")

    print("3. Zero Padding 可以提高频谱显示密度。")

    print("4. FFT 点数影响频谱采样精度。")

    print("5. 真实频率分辨率仍由采样时间决定。")

    print("6. 本实验综合验证第二章全部 FFT 分析内容。")

    print()

# ============================================================
# Main
# ============================================================

def main() -> None:
    """
    Main experiment.
    """

    output_dir = experiment_output_dir(

        chapter=2,

        experiment="exp24_comprehensive_spectrum_analysis",

    )

    print()

    print("=" * 80)
    print("Communication_Principle_Python")
    print("Experiment 24")
    print("Comprehensive Spectrum Analysis")
    print("=" * 80)
    print()

    reports = []

    for fft_points in FFT_LIST:

        for window in WINDOW_LIST:

            for zero_padding in ZERO_PADDING:

                report = run_project(

                    fft_points,

                    window,

                    zero_padding,

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

                "window": report.window,

                "zero_padding": report.zero_padding,

                "peak_frequency": spectrum.peak_frequency,

                "peak_magnitude": spectrum.peak_magnitude,

                "resolution": spectrum.resolution,

                "energy": report.statistics.energy,

                "power": report.statistics.power,

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

            "Window,"

            "Zero Padding,"

            "Peak Frequency,"

            "Peak Magnitude,"

            "Resolution,"

            "Energy,"

            "Power\n"

        )

        for report in reports:

            spectrum = report.spectrum

            fp.write(

                f"{report.fft_points},"

                f"{report.window},"

                f"{report.zero_padding},"

                f"{spectrum.peak_frequency:.6f},"

                f"{spectrum.peak_magnitude:.6f},"

                f"{spectrum.resolution:.6f},"

                f"{report.statistics.energy:.6f},"

                f"{report.statistics.power:.6f}\n"

            )


    # --------------------------------------------------------
    # Console Summary
    # --------------------------------------------------------

    print()

    print("=" * 120)

    print("Course Project Summary")

    print("=" * 120)

    print(

        f"{'FFT':<10}"

        f"{'Window':<15}"

        f"{'Padding':<10}"

        f"{'PeakFreq':>15}"

        f"{'PeakMag':>15}"

        f"{'Resolution':>15}"

        f"{'Energy':>18}"

        f"{'Power':>18}"

    )

    print("-" * 120)

    for report in reports:

        spectrum = report.spectrum

        print(

            f"{report.fft_points:<10}"

            f"{report.window:<15}"

            f"{str(report.zero_padding):<10}"

            f"{spectrum.peak_frequency:>15.6f}"

            f"{spectrum.peak_magnitude:>15.6f}"

            f"{spectrum.resolution:>15.6f}"

            f"{report.statistics.energy:>18.6f}"

            f"{report.statistics.power:>18.6f}"

        )

    print("=" * 120)

    print()

    print_theory()

    print("Output Directory")

    print(output_dir)

    print()

    print("Course Project Finished Successfully.")

# ============================================================
# Script Entry
# ============================================================

if __name__ == "__main__":

    try:

        main()

    except KeyboardInterrupt:

        print()

        print("Course Project interrupted by user.")

    except Exception as error:

        print()

        print("=" * 80)

        print("Course Project failed.")

        print("=" * 80)

        print(type(error).__name__)

        print(error)

        print("=" * 80)

        raise

