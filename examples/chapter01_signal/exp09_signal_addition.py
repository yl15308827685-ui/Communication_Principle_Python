"""
==============================================================
Experiment 09
Signal Addition
信号相加
==============================================================

Communication Principle Python

Chapter 1
Experiment 09
Signal Addition
"""

from communication.config import ExperimentConfig
from communication.signals import (
    SignalGenerator,
    add,
)
from communication.plotting import (
    plot_compare,
    plot_signal,
)
from communication.export import export_signal_csv
from communication.paths import experiment_output_dir


def main() -> None:
    """
    Experiment 09
    Signal addition.
    """

    output_dir = experiment_output_dir(
        chapter=1,
        experiment="exp09_signal_addition",
    )

    config = ExperimentConfig(
        sampling_frequency=5000,
        duration=0.02,
        amplitude=1.0,
        frequency=50.0,
    )

    generator = SignalGenerator(config)

    signal_a = generator.sine()

    signal_b = generator.cosine()

    result = add(
        signal_a,
        signal_b,
    )

    # 原始两路信号比较
    manager = plot_compare(
        signal_a,
        signal_b,
        title="Original Signals",
        label1="Sine Signal",
        label2="Cosine Signal",
    )

    manager.grid()

    manager.save(
        output_dir / "original_signals.png"
    )

    # 合成信号
    manager = plot_signal(
        result,
        title="Added Signal",
        label="Sine + Cosine",
    )

    manager.grid()

    manager.save(
        output_dir / "added_signal.png"
    )

    export_signal_csv(
        result,
        output_dir / "added_signal.csv",
    )

    print("Experiment 09 Finished.")
    print(f"Output : {output_dir}")


if __name__ == "__main__":
    main()