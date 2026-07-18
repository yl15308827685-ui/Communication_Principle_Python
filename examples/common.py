"""
common.py
=========

Common helper functions for all experiments.

Communication Principle Python
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from communication.export import export_signal_csv
from communication.plotting import (
    plot_signal,
    plot_spectrum,
)


# ==========================================================
# Directory
# ==========================================================

def ensure_output_dir(output_dir: Path) -> Path:
    """
    Ensure output directory exists.

    Parameters
    ----------
    output_dir
        Output directory.

    Returns
    -------
    Path
    """

    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    return output_dir


# ==========================================================
# Plot
# ==========================================================

def save_signal_plot(
    signal,
    filename: Path,
    title: str,
) -> Path:
    """
    Save signal figure.
    """

    manager = plot_signal(
        signal,
        title=title,
    )

    manager.grid()

    manager.save(
        filename,
    )

    return filename


def save_spectrum_plot(
    spectrum,
    filename: Path,
    title: str,
) -> Path:
    """
    Save spectrum figure.
    """

    manager = plot_spectrum(
        spectrum,
        title=title,
    )

    manager.grid()

    manager.save(
        filename,
    )

    return filename


# ==========================================================
# CSV
# ==========================================================

def save_signal_csv(
    signal,
    filename: Path,
) -> Path:
    """
    Save signal csv.
    """

    export_signal_csv(
        signal,
        filename,
    )

    return filename


def save_spectrum_csv(
    spectrum,
    filename: Path,
) -> Path:
    """
    Save spectrum csv.
    """

    export_signal_csv(
        spectrum,
        filename,
    )

    return filename


# ==========================================================
# JSON
# ==========================================================

def save_json(
    data: dict[str, Any],
    filename: Path,
) -> Path:
    """
    Save dictionary as JSON.
    """

    with open(
        filename,
        "w",
        encoding="utf-8",
    ) as fp:

        json.dump(
            data,
            fp,
            indent=4,
            ensure_ascii=False,
        )

    return filename


# ==========================================================
# Finish
# ==========================================================

def finish_experiment(
    experiment_name: str,
    output_dir: Path,
) -> None:
    """
    Print experiment finished message.
    """

    print(f"{experiment_name} Finished.")
    print(f"Output : {output_dir}")