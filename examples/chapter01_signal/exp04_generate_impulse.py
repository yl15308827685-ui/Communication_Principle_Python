"""
Experiment 04
==============

Generate an impulse signal.
单位冲激

Chapter 1
Communication Principle Python
"""

from pathlib import Path

from communication.config import ExperimentConfig
from communication.signals import SignalGenerator
from communication.plotting import plot_signal
from communication.export import export_signal_csv

from communication.paths import experiment_output_dir


def main():

    output_dir = experiment_output_dir(
        chapter=1,
        experiment="exp04_generate_impulse",
    )

    config = ExperimentConfig(
        sampling_frequency=1000,
        duration=0.02,
    )

    generator = SignalGenerator(config)

    signal = generator.impulse()

    manager = plot_signal(
        signal,
        title="Unit Impulse Signal",
    )

    manager.grid()

    manager.save(
        output_dir / "impulse_signal.png"
    )

    export_signal_csv(
        signal,
        output_dir / "impulse_signal.csv",
    )

    print("Experiment 04 Finished.")
    print(f"Output : {output_dir}")


if __name__ == "__main__":
    main()