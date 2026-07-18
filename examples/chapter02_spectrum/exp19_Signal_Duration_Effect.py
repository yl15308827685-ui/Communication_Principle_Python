"""
============================================================
Communication_Principle_Python

Experiment 19

Signal Duration Effect

Version
-------
3.0.0

Compatible SDK
--------------
Communication_Principle_Python API Freeze v1.0

Description
-----------
Study the influence of signal duration on spectrum analysis.

Author
------
Communication_Principle_Python Textbook Project
============================================================
"""

from __future__ import annotations

import json

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

FFT_POINTS = 4096

DURATIONS = [

    0.005,

    0.010,

    0.020,

    0.050,

    0.100,

]

# ============================================================
# Duration Report
# ============================================================

@dataclass
class DurationReport:

    duration: float

    signal: Signal

    spectrum: object

    statistics: object

# ============================================================
# Generate Test Signal
# ============================================================

def generate_signal(
    duration: float,
) -> Signal:
    """
    Generate test signal.
    """

    config = ExperimentConfig(

        sampling_frequency=SAMPLING_FREQUENCY,

        duration=duration,

        amplitude=CONFIG.amplitude,

        frequency=SIGNAL_FREQUENCY,

        phase=CONFIG.phase,

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

    signal.name = f"{duration * 1000:.0f} ms"

    return signal

# ============================================================
# Run One Duration Experiment
# ============================================================

def run_duration(
    duration: float,
) -> DurationReport:
    """
    Run one duration experiment.
    """

    signal = generate_signal(
        duration,
    )

    spectrum = fft(

        signal,

        fft_points=FFT_POINTS,

    )

    statistics = analyze(
        signal,
    )

    return DurationReport(

        duration=duration,

        signal=signal,

        spectrum=spectrum,

        statistics=statistics,

    )

# ============================================================
# Export Results
# ============================================================

def export_result(
    report: DurationReport,
    output_dir: Path,
) -> None:
    """
    Export experiment results.
    """

    prefix = f"duration{int(report.duration * 1000)}"

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
    report: DurationReport,
    output_dir: Path,
) -> None:
    """
    Draw figures.
    """

    prefix = f"duration{int(report.duration * 1000)}"

    # -----------------------------------------
    # Time-domain Signal
    # -----------------------------------------

    manager = plot_signal(

        report.signal,

        title=f"Signal Duration = {report.duration * 1000:.0f} ms",

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

        title=f"Duration = {report.duration * 1000:.0f} ms",

    )

    manager.save(

        output_dir / f"{prefix}_spectrum.png",

    )

    manager.close()

# ============================================================
# Print Report
# ============================================================

def print_report(
    report: DurationReport,
) -> None:
    """
    Print experiment report.
    """

    statistics = report.statistics

    spectrum = report.spectrum

    print("=" * 60)

    print(f"Signal Duration : {report.duration * 1000:.0f} ms")

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
        experiment="exp19_signal_duration_effect",
    )

    print()
    print("=" * 60)
    print("Communication_Principle_Python")
    print("Experiment 19")
    print("Signal Duration Effect")
    print("=" * 60)
    print()

    reports = []

    # --------------------------------------------------------
    # Run Experiments
    # --------------------------------------------------------

    for duration in DURATIONS:

        report = run_duration(
            duration,
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

                "duration_ms": report.duration * 1000,

                "frequency_resolution":
                    spectrum.resolution,

                "peak_frequency":
                    spectrum.peak_frequency,

                "peak_magnitude":
                    spectrum.peak_magnitude,

                "energy":
                    report.statistics.energy,

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

            "Duration(ms),"

            "Resolution,"

            "Peak Frequency,"

            "Peak Magnitude,"

            "Energy\n"

        )

        for report in reports:

            spectrum = report.spectrum

            fp.write(

                f"{report.duration * 1000:.0f},"

                f"{spectrum.resolution:.6f},"

                f"{spectrum.peak_frequency:.6f},"

                f"{spectrum.peak_magnitude:.6f},"

                f"{report.statistics.energy:.6f}\n"

            )

    # --------------------------------------------------------
    # Console Summary
    # --------------------------------------------------------

    print()

    print("=" * 90)

    print("Experiment Summary")

    print("=" * 90)

    print(

        f"{'Duration(ms)':<16}"

        f"{'Resolution':>16}"

        f"{'Peak':>16}"

        f"{'Magnitude':>18}"

        f"{'Energy':>16}"

    )

    print("-" * 90)

    for report in reports:

        spectrum = report.spectrum

        print(

            f"{report.duration * 1000:<16.0f}"

            f"{spectrum.resolution:>16.6f}"

            f"{spectrum.peak_frequency:>16.6f}"

            f"{spectrum.peak_magnitude:>18.6f}"

            f"{report.statistics.energy:>16.6f}"

        )

    print("=" * 90)

    print()

    print("Experiment Conclusion")

    print("---------------------")

    print("1. 信号持续时间越长，可获得更多信号周期。")

    print("2. 时域观察时间增加，FFT分析更加稳定。")

    print("3. 持续时间较短时，频谱泄漏更加明显。")

    print("4. 持续时间增加后，谱峰更加集中。")

    print("5. FFT点数与持续时间共同影响频谱分析结果。")

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

