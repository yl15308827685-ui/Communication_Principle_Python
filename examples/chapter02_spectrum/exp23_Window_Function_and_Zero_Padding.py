"""
============================================================
Communication_Principle_Python

Experiment 23

Window Function and Zero Padding Comparison

Version
-------
SDK v1.0 Frozen

Description
-----------
Comprehensive comparison of different window
functions with and without zero padding.

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

from communication.signals import SignalGenerator

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

SIGNAL_FREQUENCY = 100.0

FFT_POINTS = 2048

ZERO_PADDING_POINTS = 4096

WINDOW_LIST = [

    "rectangular",

    "hann",

    "hamming",

    "blackman",

]

@dataclass
class WindowExperimentResult:

    window: str

    zero_padding: bool

    signal: Signal

    spectrum: object

    statistics: object


def generate_signal() -> Signal:
    """
    Generate test signal.
    """

    config = ExperimentConfig(

        sampling_frequency=CONFIG.sampling_frequency,

        duration=CONFIG.duration,

        amplitude=CONFIG.amplitude,

        frequency=SIGNAL_FREQUENCY,

        phase=CONFIG.phase,

        fft_points=FFT_POINTS,

    )

    generator = SignalGenerator(config)

    signal = generator.sine(

        amplitude=config.amplitude,

        frequency=config.frequency,

        phase=config.phase,

    )

    signal.name = "Window Test"

    return signal

def run_experiment(

    window: str,

    zero_padding: bool,

) -> WindowExperimentResult:
    """
    Run one experiment.
    """

    signal = generate_signal()

    signal = apply_window(

        signal,

        window,

    )

    fft_points = FFT_POINTS

    if zero_padding:

        fft_points = ZERO_PADDING_POINTS

    spectrum = fft(

        signal,

        fft_points=fft_points,

    )

    statistics = analyze(

        signal,

    )

    return WindowExperimentResult(

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
    report: WindowExperimentResult,
    output_dir: Path,
) -> None:
    """
    Export experiment data.
    """

    suffix = "padding" if report.zero_padding else "normal"

    prefix = f"{report.window}_{suffix}"

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
    report: WindowExperimentResult,
    output_dir: Path,
) -> None:
    """
    Draw figures.
    """

    suffix = "padding" if report.zero_padding else "normal"

    prefix = f"{report.window}_{suffix}"

    manager = plot_signal(

        report.signal,

        title=(
            f"{report.window.upper()} "
            f"({'Zero Padding' if report.zero_padding else 'Normal'})"
        ),

    )

    manager.save(

        output_dir / f"{prefix}_signal.png",

    )

    manager.close()

    manager = plot_spectrum(

        report.spectrum,

        title=(
            f"{report.window.upper()} "
            f"({'Zero Padding' if report.zero_padding else 'Normal'})"
        ),

    )

    manager.save(

        output_dir / f"{prefix}_spectrum.png",

    )

    manager.close()

# ============================================================
# Print Report
# ============================================================

def print_report(
    report: WindowExperimentResult,
) -> None:
    """
    Print experiment report.
    """

    spectrum = report.spectrum

    statistics = report.statistics

    print("=" * 70)

    print(f"Window          : {report.window}")

    print(f"Zero Padding    : {report.zero_padding}")

    print("-" * 70)

    print(f"Mean            : {statistics.mean:.6f}")

    print(f"RMS             : {statistics.rms:.6f}")

    print(f"Variance        : {statistics.variance:.6f}")

    print(f"Standard Dev.   : {statistics.std:.6f}")

    print(f"Energy          : {statistics.energy:.6f}")

    print(f"Average Power   : {statistics.power:.6f}")

    print("-" * 70)

    print(f"FFT Points      : {spectrum.bins}")

    print(f"Resolution      : {spectrum.resolution:.6f} Hz")

    print(f"Peak Frequency  : {spectrum.peak_frequency:.6f} Hz")

    print(f"Peak Magnitude  : {spectrum.peak_magnitude:.6f}")

    print("=" * 70)

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

    print("1. 窗函数可以降低频谱泄漏。")

    print("2. 不同窗函数具有不同的主瓣宽度与旁瓣高度。")

    print("3. Zero Padding 可以提高频谱显示的平滑程度。")

    print("4. Zero Padding 不会提高真实频率分辨率。")

    print("5. FFT 的真实分辨率仍由采样时间决定。")

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

        experiment="exp23_window_padding",

    )

    print()

    print("=" * 70)
    print("Communication_Principle_Python")
    print("Experiment 23")
    print("Window Function and Zero Padding")
    print("=" * 70)
    print()

    reports = []

    for window in WINDOW_LIST:

        for zero_padding in (False, True):

            report = run_experiment(

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

    print("=" * 110)

    print("Experiment Summary")

    print("=" * 110)

    print(

        f"{'Window':<15}"

        f"{'Padding':<12}"

        f"{'Peak Freq':>15}"

        f"{'Peak Mag':>15}"

        f"{'Resolution':>15}"

        f"{'Energy':>18}"

        f"{'Power':>18}"

    )

    print("-" * 110)

    for report in reports:

        spectrum = report.spectrum

        print(

            f"{report.window:<15}"

            f"{str(report.zero_padding):<12}"

            f"{spectrum.peak_frequency:>15.6f}"

            f"{spectrum.peak_magnitude:>15.6f}"

            f"{spectrum.resolution:>15.6f}"

            f"{report.statistics.energy:>18.6f}"

            f"{report.statistics.power:>18.6f}"

        )

    print("=" * 110)

    print()

    print_theory()

    print("Output Directory:")

    print(output_dir)

    print()

    print("Experiment Finished Successfully.")


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

        print("=" * 70)

        print("Experiment failed.")

        print("=" * 70)

        print(type(error).__name__)

        print(error)

        print("=" * 70)

        raise



