"""
==============================================================
Experiment 02
Generate Cosine Signal
余弦信号
==============================================================
Communication Principle with Python
Chapter 1
"""

from pathlib import Path

from communication.config import ExperimentConfig
from communication.signals import SignalGenerator
from communication.plotting import plot_signal
from communication.export import export_signal_csv


from communication.paths import experiment_output_dir

OUTPUT_DIR = experiment_output_dir(
    1,
    "exp02_generate_cosine",
)


OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def main():

    config = ExperimentConfig(
        sampling_frequency=1000,
        duration=1.0,
    )

    generator = SignalGenerator(config)

    signal = generator.cosine(
        amplitude=1.0,
        frequency=5.0,
        phase=0.0,
    )

    manager = plot_signal(
        signal,
        title="Cosine Signal (5 Hz)",
    )

    manager.save(
        OUTPUT_DIR / "cosine_signal.png"
    )

    export_signal_csv(
        signal,
        OUTPUT_DIR / "cosine_signal.csv",
    )

    print("Experiment 02 Finished.")
    print(f"Output : {OUTPUT_DIR}")


if __name__ == "__main__":
    main()