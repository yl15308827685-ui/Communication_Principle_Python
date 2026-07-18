"""
============================================================
Communication_Principle_Python

Experiment 21

FFT Zero Padding Effect

Version
-------
3.0.0

Compatible SDK
--------------
Communication_Principle_Python API Freeze v1.0

Description
-----------
Study the influence of FFT zero padding on spectrum analysis.

Author
------
Communication_Principle_Python Textbook Project
============================================================
"""

from __future__ import annotations

import json
import numpy as np

from dataclasses import dataclass
from pathlib import Path

from communication.paths import experiment_output_dir

from communication.config import (
    DEFAULT_CONFIG,
    ExperimentConfig,
)

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

SAMPLING_FREQUENCY = CONFIG.sampling_frequency

SIGNAL_FREQUENCY = 100.0

SIGNAL_DURATION = CONFIG.duration

FFT_POINTS = [

    256,

    512,

    1024,

    2048,

    4096,

]

# ============================================================
# Zero Padding Report
# ============================================================

@dataclass
class ZeroPaddingReport:

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

    config = ExperimentConfig(

        sampling_frequency=SAMPLING_FREQUENCY,

        duration=SIGNAL_DURATION,

        amplitude=CONFIG.amplitude,

        frequency=SIGNAL_FREQUENCY,

        phase=CONFIG.phase,

        fft_points=max(FFT_POINTS),

    )

    generator = SignalGenerator(
        config,
    )

    signal = generator.sine(

        amplitude=config.amplitude,

        frequency=config.frequency,

        phase=config.phase,

    )

    signal.name = "Original Signal"

    return signal

# ============================================================
# Run One FFT Experiment
# ============================================================

def run_zero_padding(
    signal: Signal,
    fft_points: int,
) -> ZeroPaddingReport:
    """
    Run one zero padding experiment.
    """

    spectrum = fft(

        signal,

        fft_points=fft_points,

    )

    statistics = analyze(
        signal,
    )

    return ZeroPaddingReport(

        fft_points=fft_points,

        signal=signal,

        spectrum=spectrum,

        statistics=statistics,

    )

# ============================================================
# Export Results
# ============================================================

def export_result(
    report: ZeroPaddingReport,
    output_dir: Path,
) -> None:
    """
    Export experiment results.
    """

    prefix = f"fft{report.fft_points:04d}"

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
    report: ZeroPaddingReport,
    output_dir: Path,
) -> None:
    """
    Draw experiment figures.
    """

    prefix = f"fft{report.fft_points:04d}"

    # --------------------------------------------------------
    # Time-domain Signal
    # --------------------------------------------------------

    manager = plot_signal(

        report.signal,

        title=f"Original Signal (FFT={report.fft_points})",

    )

    manager.save(

        output_dir / f"{prefix}_signal.png",

    )

    manager.close()

    # --------------------------------------------------------
    # Spectrum
    # --------------------------------------------------------

    manager = plot_spectrum(

        report.spectrum,

        title=f"FFT Points = {report.fft_points}",

    )

    manager.save(

        output_dir / f"{prefix}_spectrum.png",

    )

    manager.close()

# ============================================================
# Print Report
# ============================================================

def print_report(
    report: ZeroPaddingReport,
) -> None:
    """
    Print experiment report.
    """

    statistics = report.statistics

    spectrum = report.spectrum

    print("=" * 60)

    print(f"FFT Points       : {report.fft_points}")

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
# Theory
# ============================================================

def print_theory() -> None:
    """
    Print experiment theory.
    """

    print()

    print("Theory")

    print("------")

    print("1. Zero Padding 不增加新的信号信息。")

    print("2. Zero Padding 不提高真正的频率分辨率。")

    print("3. FFT 点数增加后，频率采样更加密集。")

    print("4. 频谱曲线更加平滑。")

    print("5. 峰值位置更容易观察，但真实分辨率保持不变。")

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

        experiment="exp21_zero_padding_effect",

    )

    print()

    print("=" * 60)

    print("Communication_Principle_Python")

    print("Experiment 21")

    print("FFT Zero Padding Effect")

    print("=" * 60)

    print()

    signal = generate_signal()

    reports = []

    # --------------------------------------------------------
    # Run Experiments
    # --------------------------------------------------------

    for fft_points in FFT_POINTS:

        report = run_zero_padding(

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

                "energy":

                    report.statistics.energy,

                "power":

                    report.statistics.power,

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

            "Peak Magnitude,"

            "Energy,"

            "Power\n"

        )

        for report in reports:

            spectrum = report.spectrum

            fp.write(

                f"{report.fft_points},"

                f"{spectrum.resolution:.6f},"

                f"{spectrum.peak_frequency:.6f},"

                f"{spectrum.peak_magnitude:.6f},"

                f"{report.statistics.energy:.6f},"

                f"{report.statistics.power:.6f}\n"

            )

    # --------------------------------------------------------
    # Console Summary
    # --------------------------------------------------------

    print()

    print("=" * 96)

    print("Experiment Summary")

    print("=" * 96)

    print(

        f"{'FFT':<12}"

        f"{'Resolution':>18}"

        f"{'Peak Freq':>18}"

        f"{'Peak Mag':>18}"

        f"{'Energy':>15}"

        f"{'Power':>15}"

    )

    print("-" * 96)

    for report in reports:

        spectrum = report.spectrum

        print(

            f"{report.fft_points:<12}"

            f"{spectrum.resolution:>18.6f}"

            f"{spectrum.peak_frequency:>18.6f}"

            f"{spectrum.peak_magnitude:>18.6f}"

            f"{report.statistics.energy:>15.6f}"

            f"{report.statistics.power:>15.6f}"

        )

    print("=" * 96)

    print()

    print_theory()

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

