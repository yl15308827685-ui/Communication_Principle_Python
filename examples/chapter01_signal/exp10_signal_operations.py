"""
==============================================================
Experiment 10
Signal Operations Summary
综合实验
==============================================================

Communication Principle Python

Chapter 1
Experiment 10
Comprehensive Signal Processing
"""

from communication.config import ExperimentConfig
from communication.signals import (
    SignalGenerator,
    scale,
    shift,
    reverse,
)
from communication.plotting import plot_compare
from communication.export import export_signal_csv
from communication.paths import experiment_output_dir


def main() -> None:

    output_dir = experiment_output_dir(
        chapter=1,
        experiment="exp10_signal_operations",
    )

    config = ExperimentConfig(
        sampling_frequency=5000,
        duration=0.02,
        amplitude=1.0,
        frequency=50.0,
    )

    generator = SignalGenerator(config)

    original = generator.sine()

    scaled = scale(
        original,
        factor=2.0,
    )

    shifted = shift(
        scaled,
        delay=0.002,
    )

    reversed_signal = reverse(
        shifted,
    )

    manager = plot_compare(
        original,
        reversed_signal,
        title="Signal Operations Summary",
        label1="Original Signal",
        label2="Processed Signal",
    )

    manager.grid()

    manager.save(
        output_dir / "signal_operations.png"
    )

    export_signal_csv(
        reversed_signal,
        output_dir / "processed_signal.csv",
    )

    print("Experiment 10 Finished.")
    print(f"Output : {output_dir}")


if __name__ == "__main__":
    main()