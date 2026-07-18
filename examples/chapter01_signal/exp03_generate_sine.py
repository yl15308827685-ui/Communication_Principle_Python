"""
==============================================================
Experiment 03
Generate Sine Wave
==============================================================

通信原理 Python

第一章实验三
产生正弦信号
"""

from communication.config import ExperimentConfig
from communication.signals import SignalGenerator
from communication.plotting import plot_signal
from communication.export import export_signal_csv
from communication.paths import experiment_output_dir


OUTPUT_DIR = experiment_output_dir(
    1,
    "exp03_generate_sine",
)


def main() -> None:
    """
    Experiment 03
    """

    config = ExperimentConfig(
        sampling_frequency=1000,
        duration=1,
        amplitude=1.0,
        frequency=5.0,
        phase=0.0,
    )

    generator = SignalGenerator(config)

    signal = generator.sine()

    manager = plot_signal(
        signal,
        title="Sine Wave",
    )

    manager.grid()

    manager.save(
        OUTPUT_DIR / "sine_signal.png"
    )

    export_signal_csv(
        signal,
        OUTPUT_DIR / "sine_signal.csv",
    )

    print("Experiment 03 Finished.")
    print(f"Output : {OUTPUT_DIR}")


if __name__ == "__main__":
    main()