"""
==============================================================
Experiment 07
Signal Time Shift
时间平移
==============================================================

Communication Principle Python

Chapter 1
Experiment 07
Signal Time Shift
"""

from communication.config import ExperimentConfig
from communication.signals import (
    SignalGenerator,
    shift,
)
from communication.plotting import plot_compare
from communication.export import export_signal_csv
from communication.paths import experiment_output_dir


def main() -> None:
    """
    Experiment 07
    Signal time shift.
    """

    output_dir = experiment_output_dir(
        chapter=1,
        experiment="exp07_signal_shift",
    )

    config = ExperimentConfig(
        sampling_frequency=5000,
        duration=0.02,
        amplitude=1.0,
        frequency=50.0,
    )

    generator = SignalGenerator(config)

    original_signal = generator.sine()

    shifted_signal = shift(
        original_signal,
        delay=0.002,
    )

    manager = plot_compare(
        original_signal,
        shifted_signal,
        title="Signal Time Shift",
        label1="Original Signal",
        label2="Shifted Signal",
    )

    manager.grid()

    manager.save(
        output_dir / "signal_shift.png"
    )

    export_signal_csv(
        shifted_signal,
        output_dir / "shifted_signal.csv",
    )

    print("Experiment 07 Finished.")
    print(f"Output : {output_dir}")


if __name__ == "__main__":
    main()