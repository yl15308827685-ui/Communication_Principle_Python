"""
============================================================
Communication_Principle_Python

Experiment 22

Spectrum Dynamic Range

Version
-------
3.0.0

Compatible SDK
--------------
Communication_Principle_Python API Freeze v1.0

Description
-----------
Study spectrum dynamic range using two sine waves with
different amplitudes.

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

from communication.signals import add

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

FFT_POINTS = 4096

SIGNAL_DURATION = CONFIG.duration

MAIN_FREQUENCY = 100.0

SECOND_FREQUENCY = 300.0

AMPLITUDE_PAIRS = [

    (1.0, 1.0),

    (1.0, 0.5),

    (1.0, 0.1),

    (1.0, 0.01),

    (1.0, 0.001),

]

# ============================================================
# Dynamic Range Report
# ============================================================

@dataclass
class DynamicRangeReport:

    amplitude_ratio: float

    signal: Signal

    spectrum: object

    statistics: object

# ============================================================
# Generate Two-Tone Signal
# ============================================================

def generate_signal(
    amp1: float,
    amp2: float,
) -> Signal:
    """
    Generate two-tone signal.
    """

    config = ExperimentConfig(

        sampling_frequency=SAMPLING_FREQUENCY,

        duration=SIGNAL_DURATION,

        amplitude=1.0,

        frequency=MAIN_FREQUENCY,

        phase=0.0,

        fft_points=FFT_POINTS,

    )

    generator = SignalGenerator(config)

    signal1 = generator.sine(

        amplitude=amp1,

        frequency=MAIN_FREQUENCY,

        phase=0.0,

    )

    signal2 = generator.sine(

        amplitude=amp2,

        frequency=SECOND_FREQUENCY,

        phase=0.0,

    )

    signal = add(

        signal1,

        signal2,

    )

    signal.name = (

        f"A1={amp1:.3f}, "

        f"A2={amp2:.3f}"

    )

    signal.info["amplitude_ratio"] = amp2 / amp1

    return signal

# ============================================================
# Run One Dynamic Range Experiment
# ============================================================

def run_dynamic_range(
    amp1: float,
    amp2: float,
) -> DynamicRangeReport:
    """
    Run one experiment.
    """

    signal = generate_signal(

        amp1,

        amp2,

    )

    spectrum = fft(

        signal,

        fft_points=FFT_POINTS,

    )

    statistics = analyze(

        signal,

    )

    return DynamicRangeReport(

        amplitude_ratio=amp2 / amp1,

        signal=signal,

        spectrum=spectrum,

        statistics=statistics,

    )

# ============================================================
# Export Results
# ============================================================

def export_result(
    report: DynamicRangeReport,
    output_dir: Path,
) -> None:
    """
    Export experiment results.
    """

    ratio = int(report.amplitude_ratio * 1000)

    prefix = f"ratio{ratio:04d}"

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
    report: DynamicRangeReport,
    output_dir: Path,
) -> None:
    """
    Draw experiment figures.
    """

    ratio = int(report.amplitude_ratio * 1000)

    prefix = f"ratio{ratio:04d}"

    manager = plot_signal(

        report.signal,

        title=f"Amplitude Ratio = {report.amplitude_ratio:.3f}",

    )

    manager.save(

        output_dir / f"{prefix}_signal.png",

    )

    manager.close()

    manager = plot_spectrum(

        report.spectrum,

        title=f"Amplitude Ratio = {report.amplitude_ratio:.3f}",

    )

    manager.save(

        output_dir / f"{prefix}_spectrum.png",

    )

    manager.close()


# ============================================================
# Print Report
# ============================================================

def print_report(
    report: DynamicRangeReport,
) -> None:
    """
    Print experiment report.
    """

    spectrum = report.spectrum

    statistics = report.statistics

    print("=" * 60)

    print(

        f"Amplitude Ratio : "

        f"{report.amplitude_ratio:.3f}"

    )

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

    print(f"FFT Points       : {spectrum.bins}")

    print(f"Frequency Res.   : {spectrum.resolution:.6f} Hz")

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

    print("1. 两个频率分量幅值差异越大，弱信号越难观察。")

    print("2. FFT 可以同时检测多个频率分量。")

    print("3. 当动态范围过大时，弱谱线可能被主谱线掩盖。")

    print("4. 频谱动态范围决定系统检测微弱信号的能力。")

    print("5. 提高 FFT 点数不能提高动态范围。")

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

        experiment="exp22_dynamic_range",

    )

    print()

    print("=" * 60)

    print("Communication_Principle_Python")

    print("Experiment 22")

    print("Spectrum Dynamic Range")

    print("=" * 60)

    print()

    reports = []

    # --------------------------------------------------------
    # Run Experiments
    # --------------------------------------------------------

    for amp1, amp2 in AMPLITUDE_PAIRS:

        report = run_dynamic_range(

            amp1,

            amp2,

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

                "amplitude_ratio":

                    report.amplitude_ratio,

                "peak_frequency":

                    spectrum.peak_frequency,

                "peak_magnitude":

                    spectrum.peak_magnitude,

                "frequency_resolution":

                    spectrum.resolution,

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

            "Amplitude Ratio,"

            "Peak Frequency,"

            "Peak Magnitude,"

            "Resolution,"

            "Energy,"

            "Power\n"

        )

        for report in reports:

            spectrum = report.spectrum

            fp.write(

                f"{report.amplitude_ratio:.6f},"

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

    print("=" * 100)

    print("Experiment Summary")

    print("=" * 100)

    print(

        f"{'Amplitude Ratio':<20}"

        f"{'Peak Frequency':>18}"

        f"{'Peak Magnitude':>18}"

        f"{'Resolution':>18}"

        f"{'Energy':>13}"

        f"{'Power':>13}"

    )

    print("-" * 100)

    for report in reports:

        spectrum = report.spectrum

        print(

            f"{report.amplitude_ratio:<20.6f}"

            f"{spectrum.peak_frequency:>18.6f}"

            f"{spectrum.peak_magnitude:>18.6f}"

            f"{spectrum.resolution:>18.6f}"

            f"{report.statistics.energy:>13.6f}"

            f"{report.statistics.power:>13.6f}"

        )

    print("=" * 100)

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



