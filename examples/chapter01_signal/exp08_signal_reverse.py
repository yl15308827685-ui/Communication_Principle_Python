"""
==============================================================
Experiment 08
Signal Time Reversal
时间反转
==============================================================

Communication Principle Python

Chapter 1
Experiment 08
Signal Time Reversal
"""

from communication.config import ExperimentConfig
from communication.signals import (
    SignalGenerator,
    reverse,
)
from communication.plotting import plot_compare
from communication.export import export_signal_csv
from communication.paths import experiment_output_dir


def main() -> None:
    """
    Experiment 08
    Signal time reversal.
    """

    output_dir = experiment_output_dir(
        chapter=1,
        experiment="exp08_signal_reverse",
    )

    config = ExperimentConfig(
        sampling_frequency=5000,
        duration=0.02,
        amplitude=1.0,
        frequency=50.0,
    )

    generator = SignalGenerator(config)

    original_signal = generator.sine()

    reversed_signal = reverse(
        original_signal,
    )

    manager = plot_compare(
        original_signal,
        reversed_signal,
        title="Signal Time Reversal",
        label1="Original Signal",
        label2="Reversed Signal",
    )

    manager.grid()

    manager.save(
        output_dir / "signal_reverse.png"
    )

    export_signal_csv(
        reversed_signal,
        output_dir / "reversed_signal.csv",
    )

    print("Experiment 08 Finished.")
    print(f"Output : {output_dir}")


if __name__ == "__main__":
    main()