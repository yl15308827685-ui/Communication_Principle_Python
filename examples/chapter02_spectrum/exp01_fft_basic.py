"""
Experiment 01
==============

FFT Basic Spectrum Analysis

Chapter 2
Communication Principle Python
"""

from communication.config import ExperimentConfig
from communication.paths import experiment_output_dir

from communication.signals import SignalGenerator

from communication.spectrum import fft

from communication.plotting import (
    plot_signal,
    plot_spectrum,
)

from communication.export import export_signal_csv


def main():

    output_dir = experiment_output_dir(
        chapter=2,
        experiment="exp01_fft_basic",
    )

    config = ExperimentConfig(
        sampling_frequency=1000,
        duration=1.0,
        amplitude=1.0,
        frequency=10.0,
        fft_points=4096,
    )

    generator = SignalGenerator(config)

    signal = generator.sine()

    spectrum = fft(
        signal,
        fft_points=config.fft_points,
    )

    # -----------------------------------------
    # Time Domain
    # -----------------------------------------

    manager = plot_signal(
        signal,
        title="Sine Wave (10 Hz)",
    )

    manager.grid()

    manager.save(
        output_dir / "time_signal.png",
    )

    # -----------------------------------------
    # Spectrum
    # -----------------------------------------

    manager = plot_spectrum(
        spectrum,
        title="FFT Spectrum",
    )

    manager.grid()

    manager.save(
        output_dir / "fft_spectrum.png",
    )

    # -----------------------------------------
    # Export CSV
    # -----------------------------------------

    export_signal_csv(
        signal,
        output_dir / "time_signal.csv",
    )

    export_signal_csv(
        spectrum,
        output_dir / "fft_spectrum.csv",
    )

    print("Experiment 01 Finished.")
    print(f"Output : {output_dir}")


if __name__ == "__main__":
    main()