"""
============================================================
Communication_Principle_Python

Experiment 20

Signal Phase Effect

Version
-------
3.0.0

Compatible SDK
--------------
Communication_Principle_Python API Freeze v1.0

Description
-----------
Study the influence of signal phase on spectrum analysis.

Author
------
Communication_Principle_Python Textbook Project
============================================================
"""

from __future__ import annotations

import json

from dataclasses import dataclass

import numpy as np

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

FFT_POINTS = 4096

PHASES = [

    0.0,

    np.pi / 6,

    np.pi / 4,

    np.pi / 2,

    np.pi,

]

# ============================================================
# Phase Report
# ============================================================

@dataclass
class PhaseReport:

    phase: float

    signal: Signal

    spectrum: object

    statistics: object

# ============================================================
# Generate Test Signal
# ============================================================

def generate_signal(
    phase: float,
) -> Signal:
    """
    Generate test signal.
    """

    config = ExperimentConfig(

        sampling_frequency=SAMPLING_FREQUENCY,

        duration=CONFIG.duration,

        amplitude=CONFIG.amplitude,

        frequency=SIGNAL_FREQUENCY,

        phase=phase,

        fft_points=FFT_POINTS,

    )

    generator = SignalGenerator(
        config,
    )

    signal = generator.sine(

        amplitude=config.amplitude,

        frequency=config.frequency,

        phase=config.phase,

    )

    signal.name = f"Phase {phase:.2f} rad"

    return signal

# ============================================================
# Run One Phase Experiment
# ============================================================

def run_phase(
    phase: float,
) -> PhaseReport:
    """
    Run one phase experiment.
    """

    signal = generate_signal(
        phase,
    )

    spectrum = fft(

        signal,

        fft_points=FFT_POINTS,

    )

    statistics = analyze(
        signal,
    )

    return PhaseReport(

        phase=phase,

        signal=signal,

        spectrum=spectrum,

        statistics=statistics,

    )

# ============================================================
# Export Results
# ============================================================

def export_result(
    report: PhaseReport,
    output_dir: Path,
) -> None:
    """
    Export experiment results.
    """

    phase_deg = int(np.degrees(report.phase))

    prefix = f"phase{phase_deg:03d}"

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
    report: PhaseReport,
    output_dir: Path,
) -> None:
    """
    Draw experiment figures.
    """

    phase_deg = int(np.degrees(report.phase))

    prefix = f"phase{phase_deg}"

    # --------------------------------------------------------
    # Time-domain Signal
    # --------------------------------------------------------

    manager = plot_signal(

        report.signal,

        title=f"Phase = {phase_deg}°",

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

        title=f"Phase = {phase_deg}°",

    )

    manager.save(

        output_dir / f"{prefix}_spectrum.png",

    )

    manager.close()

# ============================================================
# Print Report
# ============================================================

def print_report(
    report: PhaseReport,
) -> None:
    """
    Print experiment report.
    """

    statistics = report.statistics

    spectrum = report.spectrum

    phase_deg = np.degrees(report.phase)

    print("=" * 60)

    print(f"Signal Phase     : {phase_deg:.1f}°")

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

        experiment="exp20_signal_phase_effect",

    )

    print()

    print("=" * 60)

    print("Communication_Principle_Python")

    print("Experiment 20")

    print("Signal Phase Effect")

    print("=" * 60)

    print()

    reports = []

    # --------------------------------------------------------
    # Run Experiments
    # --------------------------------------------------------

    for phase in PHASES:

        report = run_phase(
            phase,
        )

        reports.append(
            report,
        )

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

                "phase_degree": float(

                    np.degrees(report.phase)

                ),

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

            "Phase(degree),"

            "Peak Frequency,"

            "Peak Magnitude,"

            "Energy,"

            "Power\n"

        )

        for report in reports:

            spectrum = report.spectrum

            fp.write(

                f"{np.degrees(report.phase):.1f},"

                f"{spectrum.peak_frequency:.6f},"

                f"{spectrum.peak_magnitude:.6f},"

                f"{report.statistics.energy:.6f},"

                f"{report.statistics.power:.6f}\n"

            )

    # --------------------------------------------------------
    # Console Summary
    # --------------------------------------------------------

    print()

    print("=" * 90)

    print("Experiment Summary")

    print("=" * 90)

    print(

        f"{'Phase(°)':<15}"

        f"{'Peak Freq':>18}"

        f"{'Peak Mag':>18}"

        f"{'Energy':>18}"

        f"{'Power':>18}"

    )

    print("-" * 90)

    for report in reports:

        spectrum = report.spectrum

        print(

            f"{np.degrees(report.phase):<15.1f}"

            f"{spectrum.peak_frequency:>18.6f}"

            f"{spectrum.peak_magnitude:>18.6f}"

            f"{report.statistics.energy:>18.6f}"

            f"{report.statistics.power:>18.6f}"

        )

    print("=" * 90)

    print()

    print("Experiment Conclusion")

    print("---------------------")

    print("1. 改变信号相位不会改变频谱峰值位置。")

    print("2. 改变信号相位不会改变幅度谱。")

    print("3. 信号能量保持不变。")

    print("4. FFT幅度谱主要由幅值和频率决定。")

    print("5. 相位信息体现在相位谱，而非幅度谱。")

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

