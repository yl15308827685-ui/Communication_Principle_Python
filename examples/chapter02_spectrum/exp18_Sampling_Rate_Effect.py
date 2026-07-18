"""
============================================================
Communication_Principle_Python

Experiment 18

Sampling Rate Effect

Version
-------
3.0.0

Compatible SDK
--------------
Communication_Principle_Python API Freeze v1.0

Description
-----------
Study the influence of sampling rate on spectrum analysis.

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

FFT_POINTS = 4096

SIGNAL_FREQUENCY = 100.0

SAMPLING_RATES = [

    500,

    1000,

    2000,

    5000,

    10000,

]

# ============================================================
# Sampling Report
# ============================================================

@dataclass
class SamplingReport:

    sampling_rate: int

    signal: Signal

    spectrum: object

    statistics: object

# ============================================================
# Generate Test Signal
# ============================================================

# def generate_signal(
#     sampling_rate: int,
# ) -> Signal:
#     """
#     Generate test signal.
#     """
#
#     from communication.config import ExperimentConfig
#
#     config = ExperimentConfig(
#
#         sampling_frequency=sampling_rate,
#
#         duration=CONFIG.duration,
#
#         amplitude=CONFIG.amplitude,
#
#         frequency=SIGNAL_FREQUENCY,
#
#         phase=CONFIG.phase,
#
#         fft_points=FFT_POINTS,
#
#     )
#
#     generator = SignalGenerator(
#         config,
#     )
#
#     signal = generator.sine(
#
#         amplitude=config.amplitude,
#
#         frequency=config.frequency,
#
#         phase=config.phase,
#
#     )
#
#     signal.name = f"{sampling_rate} Hz Sampling"
#
#     return signal

# ============================================================
# Generate Test Signal
# ============================================================

def generate_signal(
    sampling_rate: int,
) -> Signal:
    """
    Generate test signal.
    """

    from communication.config import ExperimentConfig

    config = ExperimentConfig(

        sampling_frequency=float(sampling_rate),

        duration=CONFIG.duration,

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

    signal.name = f"{sampling_rate} Hz Sampling"

    return signal
# ============================================================
# Run One Sampling Experiment
# ============================================================

def run_sampling(
    sampling_rate: int,
) -> SamplingReport:
    """
    Run one sampling-rate experiment.
    """

    signal = generate_signal(
        sampling_rate,
    )

    spectrum = fft(

        signal,

        fft_points=FFT_POINTS,

    )

    statistics = analyze(
        signal,
    )

    return SamplingReport(

        sampling_rate=sampling_rate,

        signal=signal,

        spectrum=spectrum,

        statistics=statistics,

    )

# ============================================================
# Export Results
# ============================================================

def export_result(
    report: SamplingReport,
    output_dir: Path,
) -> None:
    """
    Export experiment results.
    """

    prefix = f"sampling{report.sampling_rate}"

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
    report: SamplingReport,
    output_dir: Path,
) -> None:
    """
    Draw figures.
    """

    prefix = f"sampling{report.sampling_rate}"

    # -----------------------------------------
    # Signal
    # -----------------------------------------

    manager = plot_signal(

        report.signal,

        title=f"Sampling Rate = {report.sampling_rate} Hz",

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

        title=f"Sampling Rate = {report.sampling_rate} Hz",

    )

    manager.save(

        output_dir / f"{prefix}_spectrum.png",

    )

    manager.close()

# ============================================================
# Print Report
# ============================================================

def print_report(
    report: SamplingReport,
) -> None:
    """
    Print experiment report.
    """

    statistics = report.statistics

    spectrum = report.spectrum

    print("=" * 60)

    print(f"Sampling Rate : {report.sampling_rate} Hz")

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
        experiment="exp18_sampling_rate_effect",
    )

    print()
    print("=" * 60)
    print("Communication_Principle_Python")
    print("Experiment 18")
    print("Sampling Rate Effect")
    print("=" * 60)
    print()

    reports = []

    # --------------------------------------------------------
    # Run Experiments
    # --------------------------------------------------------

    for sampling_rate in SAMPLING_RATES:

        report = run_sampling(
            sampling_rate,
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

                "sampling_rate": report.sampling_rate,

                "frequency_resolution":
                    spectrum.resolution,

                "nyquist_frequency":
                    spectrum.nyquist,

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

            "Sampling Rate,"

            "Resolution,"

            "Nyquist,"

            "Peak Frequency,"

            "Peak Magnitude\n"

        )

        for report in reports:

            spectrum = report.spectrum

            fp.write(

                f"{report.sampling_rate},"

                f"{spectrum.resolution:.6f},"

                f"{spectrum.nyquist:.6f},"

                f"{spectrum.peak_frequency:.6f},"

                f"{spectrum.peak_magnitude:.6f}\n"

            )


    # --------------------------------------------------------
    # Console Summary
    # --------------------------------------------------------

    print()

    print("=" * 88)

    print("Experiment Summary")

    print("=" * 88)

    print(

        f"{'Sampling(Hz)':<16}"

        f"{'Resolution':>16}"

        f"{'Nyquist':>16}"

        f"{'Peak':>16}"

        f"{'Magnitude':>16}"

    )

    print("-" * 88)

    for report in reports:

        spectrum = report.spectrum

        print(

            f"{report.sampling_rate:<16}"

            f"{spectrum.resolution:>16.6f}"

            f"{spectrum.nyquist:>16.6f}"

            f"{spectrum.peak_frequency:>16.6f}"

            f"{spectrum.peak_magnitude:>16.6f}"

        )

    print("=" * 88)

    print()

    print("Experiment Conclusion")

    print("---------------------")

    print("1. 采样率决定奈奎斯特频率。")

    print("2. 奈奎斯特频率等于采样率的一半。")

    print("3. 当采样率不足时将发生频谱混叠。")

    print("4. 采样率越高，可正确分析的最高频率越高。")

    print("5. 频率分辨率同时受采样率和FFT点数影响。")

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

