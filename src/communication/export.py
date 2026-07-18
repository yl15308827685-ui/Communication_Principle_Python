"""
==========================================================
Communication_Principle_Python

File:
    export.py

Version:
    1.0.0

Description:
    Export Module

Python:
    >=3.9

==========================================================
"""

from __future__ import annotations

from pathlib import Path
from typing import Union

import csv

import matplotlib.pyplot as plt

from .models import Signal
from .models import Spectrum
from .models import SignalStatistics



# ==========================================================
# Signal Exporter
# ==========================================================

class SignalExporter:
    """
    Export signal analysis results.

    Examples
    --------

    >>> exporter = SignalExporter()

    >>> exporter.export_signal_csv(
    ...     signal,
    ...     "signal.csv",
    ... )
    """

    def export_signal_csv(
        self,
        signal_or_spectrum: Union[
            Signal,
            Spectrum,
        ],
        filename: Union[str, Path],
    ) -> None:
        """
        Export Signal to CSV.
        """

        export_signal_csv(
            signal_or_spectrum,
            filename,
        )

    def export_spectrum_csv(
        self,
        spectrum: Spectrum,
        filename: Union[str, Path],
    ) -> None:
        """
        Export Spectrum to CSV.
        """

        export_spectrum_csv(
            spectrum,
            filename,
        )

    def export_statistics_csv(
        self,
        statistics: SignalStatistics,
        filename: Union[str, Path],
    ) -> None:
        """
        Export SignalStatistics to CSV.
        """

        export_statistics_csv(
            statistics,
            filename,
        )

    def save_figure(
        self,
        filename: Union[str, Path],
        dpi: int = 300,
    ) -> None:
        """
        Save current figure.
        """

        save_figure(
            filename,
            dpi=dpi,
        )


# ==========================================================
# Internal Helper
# ==========================================================

def _to_path(
    filename: Union[str, Path],
) -> Path:
    """
    Convert filename to Path object.
    """

    return Path(filename)


# ==========================================================
# Export Signal
# ==========================================================

def export_signal_csv(
    signal_or_spectrum,
    filename: Union[str, Path],
) -> None:
    """
    Export Signal or Spectrum to CSV.
    """

    path = _to_path(filename)

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        path,
        "w",
        newline="",
        encoding="utf-8",
    ) as csvfile:

        writer = csv.writer(csvfile)

        # ----------------------------------------
        # Signal
        # ----------------------------------------

        if isinstance(signal_or_spectrum, Signal):

            writer.writerow(
                [
                    "Time",
                    "Value",
                ]
            )

            for t, v in zip(
                signal_or_spectrum.time,
                signal_or_spectrum.value,
            ):

                writer.writerow(
                    [
                        t,
                        v,
                    ]
                )

            return

        # ----------------------------------------
        # Spectrum
        # ----------------------------------------

        if isinstance(signal_or_spectrum, Spectrum):

            writer.writerow(
                [
                    "Frequency",
                    "Magnitude",
                    "Phase",
                ]
            )

            for f, m, p in zip(
                signal_or_spectrum.frequency,
                signal_or_spectrum.magnitude,
                signal_or_spectrum.phase,
            ):

                writer.writerow(
                    [
                        f,
                        m,
                        p,
                    ]
                )

            return

        # ----------------------------------------

        raise TypeError(
            "Input must be Signal or Spectrum."
        )

# ==========================================================
# Export Spectrum
# ==========================================================

def export_spectrum_csv(
    spectrum: Spectrum,
    filename: Union[str, Path],
) -> None:
    """
    Export Spectrum to CSV.

    Parameters
    ----------
    spectrum
        Input spectrum.

    filename
        Output CSV filename.
    """

    if not isinstance(
        spectrum,
        Spectrum,
    ):

        raise TypeError(
            "spectrum must be a Spectrum object."
        )

    path = _to_path(
        filename,
    )

    with open(

        path,

        "w",

        newline="",

        encoding="utf-8",

    ) as csvfile:

        writer = csv.writer(
            csvfile
        )

        writer.writerow(

            [

                "Frequency",

                "Magnitude",

                "Phase",

            ]

        )

        for frequency, magnitude, phase in zip(

            spectrum.frequency,

            spectrum.magnitude,

            spectrum.phase,

        ):

            writer.writerow(

                [

                    frequency,

                    magnitude,

                    phase,

                ]

            )


# ==========================================================
# Export Signal Statistics
# ==========================================================

def export_statistics_csv(
    statistics: SignalStatistics,
    filename: Union[str, Path],
) -> None:
    """
    Export SignalStatistics to CSV.

    Parameters
    ----------
    statistics
        Signal statistics.

    filename
        Output CSV filename.
    """

    if not isinstance(
        statistics,
        SignalStatistics,
    ):

        raise TypeError(
            "statistics must be a SignalStatistics object."
        )

    path = _to_path(
        filename,
    )

    with open(

        path,

        "w",

        newline="",

        encoding="utf-8",

    ) as csvfile:

        writer = csv.writer(
            csvfile
        )

        writer.writerow(

            [

                "Item",

                "Value",

            ]

        )

        writer.writerow(
            ["Mean", statistics.mean]
        )

        writer.writerow(
            ["RMS", statistics.rms]
        )

        writer.writerow(
            ["Variance", statistics.variance]
        )

        writer.writerow(
            [
                "Standard Deviation",
                statistics.std,
            ]
        )

        writer.writerow(
            ["Peak", statistics.peak]
        )

        writer.writerow(
            [
                "Peak-to-Peak",
                statistics.peak_to_peak,
            ]
        )

        writer.writerow(
            ["Energy", statistics.energy]
        )

        writer.writerow(
            [
                "Average Power",
                statistics.power,
            ]
        )


# ==========================================================
# Save Figure
# ==========================================================

def save_figure(
    filename: Union[str, Path],
    dpi: int = 300,
) -> None:
    """
    Save current matplotlib figure.

    Parameters
    ----------
    filename
        Output image filename.

    dpi
        Figure resolution.
    """

    path = _to_path(
        filename,
    )

    # Automatically create output directory
    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    plt.savefig(

        path,

        dpi=dpi,

        bbox_inches="tight",

    )

# ==========================================================
# Export
# ==========================================================

def export(
    obj,
    filename: Union[str, Path],
) -> None:
    """
    Export object automatically.

    Parameters
    ----------
    obj
        Object to export.

    filename
        Output filename.
    """

    if isinstance(
        obj,
        Signal,
    ):

        export_signal_csv(
            obj,
            filename,
        )

        return

    if isinstance(
        obj,
        Spectrum,
    ):

        export_spectrum_csv(
            obj,
            filename,
        )

        return

    if isinstance(
        obj,
        SignalStatistics,
    ):

        export_statistics_csv(
            obj,
            filename,
        )

        return

    raise TypeError(

        "unsupported export object."

    )


# ==========================================================
# Public API
# ==========================================================

__all__ = [

    "SignalExporter",

    "export",

    "export_signal_csv",

    "export_spectrum_csv",

    "export_statistics_csv",

    "save_figure",

]

