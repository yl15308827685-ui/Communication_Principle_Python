"""
Experiment 05
==============

FFT Points and Frequency Resolution

Chapter 2
Communication Principle Python
"""

from __future__ import annotations

import json
from pathlib import Path

from communication.config import ExperimentConfig
from communication.paths import experiment_output_dir

from communication.signals import SignalGenerator

from communication.spectrum import (
    fft,
    peak_frequency,
    peak_magnitude,
    frequency_resolution,
)

from communication.plotting import (
    plot_signal,
    plot_spectrum,
)

from communication.export import (
    export_signal_csv,
)

FFT_POINTS = [
    128,
    256,
    512,
    1024,
    2048,
    4096,
]


def run_case(
    fft_points: int,
    output_dir: Path,
):
    """
    Run one FFT experiment.
    """

    config = ExperimentConfig(

        sampling_frequency=1000,

        duration=0.05,

        amplitude=1.0,

        frequency=100.0,

        phase=0.0,

        fft_points=fft_points,

    )

    generator = SignalGenerator(config)

    signal = generator.sine()

    spectrum = fft(

        signal,

        fft_points=config.fft_points,

    )

    # ----------------------------------------
    # Time-domain figure
    # ----------------------------------------

    manager = plot_signal(

        signal,

        title=f"Time Domain Signal (FFT={fft_points})",

    )

    manager.grid()

    manager.save(

        output_dir /

        f"time_fft_{fft_points}.png"

    )

    # ----------------------------------------
    # Spectrum
    # ----------------------------------------

    manager = plot_spectrum(

        spectrum,

        title=f"Amplitude Spectrum (FFT={fft_points})",

    )

    manager.grid()

    manager.save(

        output_dir /

        f"spectrum_fft_{fft_points}.png"

    )

    # ----------------------------------------
    # Export CSV
    # ----------------------------------------

    export_signal_csv(

        signal,

        output_dir /

        f"time_fft_{fft_points}.csv",

    )

    export_signal_csv(

        spectrum,

        output_dir /

        f"spectrum_fft_{fft_points}.csv",

    )

    # ----------------------------------------
    # Report
    # ----------------------------------------

    report = {

        "fft_points": fft_points,

        "sampling_frequency":
            config.sampling_frequency,

        "signal_frequency":
            config.frequency,

        "frequency_resolution":
            frequency_resolution(

                config.sampling_frequency,

                fft_points,

            ),

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

        f"report_fft_{fft_points}.json",

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

def main():
    """
    Main function.
    """

    output_dir = experiment_output_dir(
        chapter=2,
        experiment="exp05_fft_points",
    )

    summary = []

    print("=" * 60)
    print("Experiment 05")
    print("FFT Points and Frequency Resolution")
    print("=" * 60)

    for fft_points in FFT_POINTS:

        print(f"Running FFT = {fft_points} ...")

        report = run_case(
            fft_points,
            output_dir,
        )

        summary.append(report)

    # --------------------------------------------------
    # Export Summary CSV
    # --------------------------------------------------

    csv_file = output_dir / "fft_resolution.csv"

    with open(
        csv_file,
        "w",
        encoding="utf-8",
    ) as fp:

        fp.write(
            "FFT Points,"
            "Frequency Resolution (Hz),"
            "Peak Frequency (Hz),"
            "Peak Magnitude\n"
        )

        for item in summary:

            fp.write(

                f"{item['fft_points']},"

                f"{item['frequency_resolution']:.6f},"

                f"{item['peak_frequency']:.6f},"

                f"{item['peak_magnitude']:.6f}\n"

            )

    # --------------------------------------------------
    # Export Summary JSON
    # --------------------------------------------------

    json_file = output_dir / "summary.json"

    with open(
        json_file,
        "w",
        encoding="utf-8",
    ) as fp:

        json.dump(
            summary,
            fp,
            indent=4,
            ensure_ascii=False,
        )

    # --------------------------------------------------
    # Print Result
    # --------------------------------------------------

    print()

    print("-" * 60)
    print("Frequency Resolution")
    print("-" * 60)

    for item in summary:

        print(

            f"FFT = "

            f"{item['fft_points']:>5d}"

            f"    "

            f"Δf = "

            f"{item['frequency_resolution']:.6f} Hz"

        )

    print()

    print("Experiment Finished.")

    print(f"Output Directory : {output_dir}")


if __name__ == "__main__":

    main()
