"""
==============================================================
Experiment 05
Generate Step Signal
单位阶跃（下一步）
==============================================================

Communication Principle Python

Chapter 1
Experiment 05
Generate Unit Step Signal
"""

from communication.config import ExperimentConfig
from communication.signals import SignalGenerator
from communication.plotting import plot_signal
from communication.export import export_signal_csv
from communication.paths import experiment_output_dir


def main() -> None:
    """
    Experiment 05
    Generate unit step signal.
    """

    output_dir = experiment_output_dir(
        chapter=1,
        experiment="exp05_generate_step",
    )

    config = ExperimentConfig(
        sampling_frequency=5000,
        duration=0.02,
        amplitude=1.0,
    )

    generator = SignalGenerator(config)

    signal = generator.step()

    manager = plot_signal(
        signal,
        title="Unit Step Signal",
        label="Step",
    )

    manager.grid()

    manager.save(
        output_dir / "step_signal.png"
    )

    export_signal_csv(
        signal,
        output_dir / "step_signal.csv",
    )

    print("Experiment 05 Finished.")
    print(f"Output : {output_dir}")


if __name__ == "__main__":
    main()