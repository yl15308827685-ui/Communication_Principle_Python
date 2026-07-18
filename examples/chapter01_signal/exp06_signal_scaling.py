"""
==============================================================
Experiment 06
Signal Amplitude Scaling
==============================================================

Communication Principle Python

Chapter 1
Experiment 06
Signal Amplitude Scaling
信号幅值归一化/幅度缩放
"""

from communication.config import ExperimentConfig
from communication.signals import (
    SignalGenerator,
    scale,
)
from communication.plotting import plot_signal
from communication.export import export_signal_csv
from communication.paths import experiment_output_dir


def main() -> None:
    """
    Experiment 06
    Signal amplitude scaling.
    """

    output_dir = experiment_output_dir(
        chapter=1,
        experiment="exp06_signal_scaling",
    )

    config = ExperimentConfig(
        sampling_frequency=5000,
        duration=0.02,
        amplitude=1.0,
        frequency=50.0,
    )

    generator = SignalGenerator(config)

    signal = generator.sine()

    scaled_signal = scale(
        signal,
        factor=2.0,
    )

    manager = plot_signal(
        scaled_signal,
        title="Amplitude Scaling",
        label="2 × Sine",
    )

    manager.grid()

    manager.save(
        output_dir / "scaled_signal.png"
    )

    export_signal_csv(
        scaled_signal,
        output_dir / "scaled_signal.csv",
    )

    print("Experiment 06 Finished.")
    print(f"Output : {output_dir}")


if __name__ == "__main__":
    main()