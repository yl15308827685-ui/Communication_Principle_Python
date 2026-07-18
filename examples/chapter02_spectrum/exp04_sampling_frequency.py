"""
Experiment 04
=============

Sampling Frequency and Spectrum

Chapter 2
Communication Principle Python
"""

from communication.config import ExperimentConfig
from communication.signals import SignalGenerator

from communication.spectrum import (
    fft,
    peak_frequency,
)

from communication.plotting import (
    plot_signal,
    plot_spectrum,
)

from communication.export import (
    export_signal_csv,
)

from communication.paths import (
    experiment_output_dir,
)

import json


def run_case(
    sampling_frequency: float,
    output_dir,
):
    """
    Run one sampling-frequency experiment.
    """

    config = ExperimentConfig(

        sampling_frequency=sampling_frequency,

        duration=0.05,

        amplitude=1.0,

        frequency=100.0,

        fft_points=4096,

    )

    generator = SignalGenerator(
        config,
    )

    signal = generator.sine()

    spectrum = fft(

        signal,

        fft_points=config.fft_points,

    )

    # ---------------------------------------------
    # Time-domain
    # ---------------------------------------------

    manager = plot_signal(

        signal,

        title=f"Sampling Frequency = {sampling_frequency:.0f} Hz",

    )

    manager.grid()

    manager.save(

        output_dir /

        f"time_fs_{int(sampling_frequency)}.png"

    )

    # ---------------------------------------------
    # Spectrum
    # ---------------------------------------------

    manager = plot_spectrum(

        spectrum,

        title=f"Amplitude Spectrum ({sampling_frequency:.0f} Hz)",

    )

    manager.grid()

    manager.save(

        output_dir /

        f"spectrum_fs_{int(sampling_frequency)}.png"

    )

    # ---------------------------------------------
    # CSV
    # ---------------------------------------------

    export_signal_csv(

        signal,

        output_dir /

        f"time_fs_{int(sampling_frequency)}.csv",

    )

    export_signal_csv(

        spectrum,

        output_dir /

        f"spectrum_fs_{int(sampling_frequency)}.csv",

    )

    # ---------------------------------------------
    # Report
    # ---------------------------------------------

    report = {

        "sampling_frequency": sampling_frequency,

        "signal_frequency": config.frequency,

        "fft_points": config.fft_points,

        "peak_frequency": peak_frequency(

            spectrum,

        ),

    }

    with open(

        output_dir /

        f"report_fs_{int(sampling_frequency)}.json",

        "w",

        encoding="utf-8",

    ) as fp:

        json.dump(

            report,

            fp,

            indent=4,

            ensure_ascii=False,

        )


def main():

    output_dir = experiment_output_dir(

        chapter=2,

        experiment="exp04_sampling_frequency",

    )

    sampling_list = [

        300,

        500,

        1000,

        2000,

    ]

    for fs in sampling_list:

        run_case(

            fs,

            output_dir,

        )

    print("Experiment 04 Finished.")

    print(f"Output : {output_dir}")


if __name__ == "__main__":

    main()

