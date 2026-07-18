"""
Experiment 03
==============

Phase Spectrum Analysis

Chapter 2
Communication Principle Python
"""

from communication.config import ExperimentConfig
from communication.paths import experiment_output_dir

from communication.signals import SignalGenerator

from communication.spectrum import (
    fft,
    phase_spectrum,
)

from communication.plotting import (
    plot_signal,
    plot_spectrum,
)

from communication.export import (
    export_signal_csv,
)

from examples.spectrum_common import save_report


def main():

    # ---------------------------------------------------------
    # Output Directory
    # ---------------------------------------------------------

    output_dir = experiment_output_dir(
        chapter=2,
        experiment="exp03_phase_spectrum",
    )

    # ---------------------------------------------------------
    # Experiment Configuration
    # ---------------------------------------------------------

    config = ExperimentConfig(
        sampling_frequency=1000,
        duration=1.0,
        amplitude=1.0,
        frequency=30.0,
        phase=0.7853981633974483,      # π/4
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
    # Phase Spectrum
    # ---------------------------------------------------------

    phase = phase_spectrum(
        spectrum,
    )

    # ---------------------------------------------------------
    # Time Domain
    # ---------------------------------------------------------

    manager = plot_signal(
        signal,
        title="30 Hz Sine Wave (Phase = π/4)",
    )

    manager.grid()

    manager.save(
        output_dir / "time_signal.png",
    )

    # ---------------------------------------------------------
    # Phase Spectrum
    # ---------------------------------------------------------

    manager = plot_spectrum(
        phase,
        title="Phase Spectrum",
    )

    manager.grid()

    manager.save(
        output_dir / "phase_spectrum.png",
    )

    # ---------------------------------------------------------
    # Export CSV
    # ---------------------------------------------------------

    export_signal_csv(
        signal,
        output_dir / "time_signal.csv",
    )

    export_signal_csv(
        phase,
        output_dir / "phase_spectrum.csv",
    )

    # ---------------------------------------------------------
    # JSON Report
    # ---------------------------------------------------------

    report = {

        "experiment": "Phase Spectrum Analysis",

        "sampling_frequency": config.sampling_frequency,

        "signal_frequency": config.frequency,

        "initial_phase(rad)": config.phase,

        "fft_points": config.fft_points,

    }

    save_report(
        report,
        output_dir / "report.json",
    )

    # ---------------------------------------------------------

    print("Experiment 03 Finished.")
    print(f"Output : {output_dir}")


if __name__ == "__main__":
    main()