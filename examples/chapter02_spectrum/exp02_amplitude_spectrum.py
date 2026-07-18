"""
Experiment 02
==============

Amplitude Spectrum Analysis

Chapter 2
Communication Principle Python
"""

from communication.config import ExperimentConfig
from communication.paths import experiment_output_dir

from communication.signals import SignalGenerator

from communication.spectrum import (
    fft,
    amplitude_spectrum,
)

from communication.plotting import (
    plot_signal,
    plot_spectrum,
)

from communication.export import (
    export_signal_csv,
)


def main():

    # ---------------------------------------------------------
    # Output Directory
    # ---------------------------------------------------------

    output_dir = experiment_output_dir(
        chapter=2,
        experiment="exp02_amplitude_spectrum",
    )

    # ---------------------------------------------------------
    # Experiment Configuration
    # ---------------------------------------------------------

    config = ExperimentConfig(
        sampling_frequency=1000,
        duration=1.0,
        amplitude=1.0,
        frequency=20.0,
        fft_points=4096,
    )

    # ---------------------------------------------------------
    # Generate Signal
    # ---------------------------------------------------------

    generator = SignalGenerator(config)

    signal = generator.sine()

    # ---------------------------------------------------------
    # FFT
    # ---------------------------------------------------------

    spectrum = fft(
        signal,
        fft_points=config.fft_points,
    )

    # ---------------------------------------------------------
    # Amplitude Spectrum
    # ---------------------------------------------------------

    amp_spectrum = amplitude_spectrum(
        spectrum,
    )

    # ---------------------------------------------------------
    # Plot Time Domain
    # ---------------------------------------------------------

    manager = plot_signal(
        signal,
        title="20 Hz Sine Wave",
    )

    manager.grid()

    manager.save(
        output_dir / "time_signal.png",
    )

    # ---------------------------------------------------------
    # Plot Amplitude Spectrum
    # ---------------------------------------------------------

    manager = plot_spectrum(
        amp_spectrum,
        title="Amplitude Spectrum",
    )

    manager.grid()

    manager.save(
        output_dir / "amplitude_spectrum.png",
    )

    # ---------------------------------------------------------
    # Export CSV
    # ---------------------------------------------------------

    export_signal_csv(
        signal,
        output_dir / "time_signal.csv",
    )

    export_signal_csv(
        amp_spectrum,
        output_dir / "amplitude_spectrum.csv",
    )

    # ---------------------------------------------------------
    # Finish
    # ---------------------------------------------------------

    print("Experiment 02 Finished.")
    print(f"Output : {output_dir}")


if __name__ == "__main__":
    main()