"""
==========================================================

Communication_Principle_Python

test_export.py

Export Module Unit Test

==========================================================
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pytest

from communication.signals import SignalGenerator
from communication.spectrum import SpectrumAnalyzer
from communication.analysis import SignalAnalyzer

from communication.export import (

    SignalExporter,

    export,

    export_signal_csv,

    export_spectrum_csv,

    export_statistics_csv,

    save_figure,

)


# ==========================================================
# Fixture
# ==========================================================

@pytest.fixture
def signal():

    return SignalGenerator().sine()


@pytest.fixture
def spectrum(signal):

    return SpectrumAnalyzer().fft(signal)


@pytest.fixture
def statistics(signal):

    return SignalAnalyzer().analyze(signal)


# ==========================================================
# Signal CSV
# ==========================================================

def test_export_signal_csv(signal, tmp_path):

    file = tmp_path / "signal.csv"

    export_signal_csv(signal, file)

    assert file.exists()

    assert file.stat().st_size > 0


# ==========================================================
# Spectrum CSV
# ==========================================================

def test_export_spectrum_csv(spectrum, tmp_path):

    file = tmp_path / "spectrum.csv"

    export_spectrum_csv(spectrum, file)

    assert file.exists()

    assert file.stat().st_size > 0


# ==========================================================
# Statistics CSV
# ==========================================================

def test_export_statistics_csv(statistics, tmp_path):

    file = tmp_path / "statistics.csv"

    export_statistics_csv(statistics, file)

    assert file.exists()

    assert file.stat().st_size > 0


# ==========================================================
# export(signal)
# ==========================================================

def test_export_signal(signal, tmp_path):

    file = tmp_path / "signal.csv"

    export(signal, file)

    assert file.exists()


# ==========================================================
# export(spectrum)
# ==========================================================

def test_export_spectrum(spectrum, tmp_path):

    file = tmp_path / "spectrum.csv"

    export(spectrum, file)

    assert file.exists()


# ==========================================================
# export(statistics)
# ==========================================================

def test_export_statistics(statistics, tmp_path):

    file = tmp_path / "statistics.csv"

    export(statistics, file)

    assert file.exists()


# ==========================================================
# save figure
# ==========================================================

def test_save_figure(tmp_path):

    plt.figure()

    plt.plot([1, 2, 3], [4, 5, 6])

    file = tmp_path / "figure.png"

    save_figure(file)

    assert file.exists()

    assert file.stat().st_size > 0

    plt.close()


# ==========================================================
# Exporter Class
# ==========================================================

def test_exporter_signal(signal, tmp_path):

    exporter = SignalExporter()

    file = tmp_path / "signal.csv"

    exporter.export_signal_csv(signal, file)

    assert file.exists()


def test_exporter_spectrum(spectrum, tmp_path):

    exporter = SignalExporter()

    file = tmp_path / "spectrum.csv"

    exporter.export_spectrum_csv(spectrum, file)

    assert file.exists()


def test_exporter_statistics(statistics, tmp_path):

    exporter = SignalExporter()

    file = tmp_path / "statistics.csv"

    exporter.export_statistics_csv(statistics, file)

    assert file.exists()


def test_exporter_save_figure(tmp_path):

    exporter = SignalExporter()

    plt.figure()

    plt.plot([0, 1], [0, 1])

    file = tmp_path / "figure.png"

    exporter.save_figure(file)

    assert file.exists()

    plt.close()


# ==========================================================
# Exception Test
# ==========================================================

def test_signal_type_error(tmp_path):

    with pytest.raises(TypeError):

        export_signal_csv(

            123,

            tmp_path / "a.csv",

        )


def test_spectrum_type_error(tmp_path):

    with pytest.raises(TypeError):

        export_spectrum_csv(

            123,

            tmp_path / "a.csv",

        )


def test_statistics_type_error(tmp_path):

    with pytest.raises(TypeError):

        export_statistics_csv(

            123,

            tmp_path / "a.csv",

        )


def test_export_type_error(tmp_path):

    with pytest.raises(TypeError):

        export(

            object(),

            tmp_path / "a.csv",

        )