"""
==========================================================
Communication_Principle_Python

File:
    spectrum_common.py

Version:
    3.0.0

Description:
    Common helper functions for spectrum experiments.

==========================================================
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict

from communication.models import Signal
from communication.models import Spectrum

from communication.spectrum import (
    fft,
    peak_frequency,
    peak_magnitude,
    frequency_resolution,
    nyquist_frequency,
)

from communication.plotting import (
    plot_signal,
    plot_spectrum,
)

from communication.export import (
    export_signal_csv,
)


# ==========================================================
# FFT
# ==========================================================

def compute_spectrum(
    signal: Signal,
    fft_points: int = 4096,
) -> Spectrum:
    """
    Compute FFT spectrum.

    Parameters
    ----------
    signal
        Input signal.

    fft_points
        FFT points.

    Returns
    -------
    Spectrum
    """

    return fft(
        signal,
        fft_points=fft_points,
    )


# ==========================================================
# Plot
# ==========================================================

def save_signal_plot(
    signal: Signal,
    filename: Path,
    title: str = "Time Domain Signal",
):
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


def save_spectrum_plot(
    spectrum: Spectrum,
    filename: Path,
    title: str = "Amplitude Spectrum",
):
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


# ==========================================================
# CSV
# ==========================================================

def save_signal_csv(
    signal: Signal,
    filename: Path,
):
    """
    Save signal CSV.
    """

    export_signal_csv(
        signal,
        filename,
    )


def save_spectrum_csv(
    spectrum: Spectrum,
    filename: Path,
):
    """
    Save spectrum CSV.
    """

    export_signal_csv(
        spectrum,
        filename,
    )


# ==========================================================
# Report
# ==========================================================

def build_report(
    spectrum: Spectrum,
    fft_points: int,
) -> Dict:
    """
    Build spectrum report.

    Parameters
    ----------
    spectrum
        FFT spectrum.

    fft_points
        FFT points.

    Returns
    -------
    dict
    """

    sampling_rate = spectrum.sampling_rate

    report = {

        "sampling_frequency": sampling_rate,

        "fft_points": fft_points,

        "frequency_resolution":

            frequency_resolution(

                sampling_rate,

                fft_points,

            ),

        "nyquist_frequency":

            nyquist_frequency(

                sampling_rate,

            ),

        "peak_frequency":

            peak_frequency(

                spectrum,

            ),

        "peak_magnitude":

            peak_magnitude(

                spectrum,

            ),

    }

    return report

# ==========================================================
# JSON
# ==========================================================

def save_report(
    report: Dict,
    filename: Path,
):
    """
    Save report as JSON.

    Parameters
    ----------
    report
        Report dictionary.

    filename
        JSON filename.
    """

    filename.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        filename,
        "w",
        encoding="utf-8",
    ) as fp:

        json.dump(
            report,
            fp,
            indent=4,
            ensure_ascii=False,
        )


# ==========================================================
# Export All
# ==========================================================

def save_experiment(
    signal: Signal,
    spectrum: Spectrum,
    output_dir: Path,
    fft_points: int,
    *,
    signal_image: str = "time_signal.png",
    spectrum_image: str = "amplitude_spectrum.png",
    signal_csv: str = "time_signal.csv",
    spectrum_csv: str = "amplitude_spectrum.csv",
    report_json: str = "report.json",
    signal_title: str = "Time Domain Signal",
    spectrum_title: str = "Amplitude Spectrum",
):
    """
    Save all experiment results.

    Output
    ------
    output_dir/

        time_signal.png

        amplitude_spectrum.png

        time_signal.csv

        amplitude_spectrum.csv

        report.json
    """

    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    # --------------------------------------------------
    # Figures
    # --------------------------------------------------

    save_signal_plot(
        signal,
        output_dir / signal_image,
        signal_title,
    )

    save_spectrum_plot(
        spectrum,
        output_dir / spectrum_image,
        spectrum_title,
    )

    # --------------------------------------------------
    # CSV
    # --------------------------------------------------

    save_signal_csv(
        signal,
        output_dir / signal_csv,
    )

    save_spectrum_csv(
        spectrum,
        output_dir / spectrum_csv,
    )

    # --------------------------------------------------
    # Report
    # --------------------------------------------------

    report = build_report(
        spectrum,
        fft_points,
    )

    save_report(
        report,
        output_dir / report_json,
    )

    return report


# ==========================================================
# Public API
# ==========================================================

__all__ = [

    "compute_spectrum",

    "save_signal_plot",

    "save_spectrum_plot",

    "save_signal_csv",

    "save_spectrum_csv",

    "build_report",

    "save_report",

    "save_experiment",

]
