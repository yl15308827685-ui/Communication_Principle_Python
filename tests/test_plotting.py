"""
Plotting Module Tests
"""

from pathlib import Path

import matplotlib.pyplot as plt

from communication import *

import matplotlib

matplotlib.use("Agg", force=True)

import matplotlib.pyplot as plt


def create_signal():

    generator = SignalGenerator()

    return generator.sine(
        amplitude=1.0,
        frequency=100.0,
    )


def create_spectrum():

    signal = create_signal()

    return fft(signal)


# ==========================================================
# PlotStyle
# ==========================================================

def test_plot_style():

    style = PlotStyle()

    assert style.dpi > 0

    assert style.linewidth > 0


# ==========================================================
# FigureManager
# ==========================================================

def test_create_manager():
    signal = create_signal()

    manager = plot_signal(signal)

    assert manager.figure is not None
    assert manager.axes is not None

    manager.close()


def test_manager_clear():
    signal = create_signal()

    manager = plot_signal(signal)

    manager.clear()

    manager.close()


def test_manager_grid():
    signal = create_signal()

    manager = plot_signal(signal)

    manager.grid(True)

    manager.close()


def test_manager_title():
    signal = create_signal()

    manager = plot_signal(signal)

    manager.set_title("Test")

    manager.close()


def test_manager_label():
    signal = create_signal()

    manager = plot_signal(signal)

    manager.set_xlabel("Time")

    manager.set_ylabel("Amplitude")

    manager.close()

# ==========================================================
# Plot Signal
# ==========================================================

def test_plot_signal():

    signal = create_signal()

    manager = plot_signal(signal)

    assert manager.figure is not None

    manager.close()


# ==========================================================
# Plot Spectrum
# ==========================================================

def test_plot_spectrum():

    spectrum = create_spectrum()

    manager = plot_spectrum(spectrum)

    assert manager.figure is not None

    manager.close()


def test_plot_single_spectrum():

    spectrum = create_spectrum()

    manager = plot_single_spectrum(spectrum)

    assert manager.figure is not None

    manager.close()


# ==========================================================
# Compare
# ==========================================================

def test_plot_compare():

    signal = create_signal()

    manager = plot_compare(

        signal,

        signal,

    )

    assert manager.figure is not None

    manager.close()


# ==========================================================
# Combined
# ==========================================================

def test_plot_signal_and_spectrum():

    signal = create_signal()

    spectrum = fft(signal)

    manager = plot_signal_and_spectrum(

        signal,

        spectrum,

    )

    assert manager.figure is not None

    manager.close()


# ==========================================================
# Save
# ==========================================================

def test_save_current_figure(tmp_path):

    signal = create_signal()

    plot_signal(signal)

    filename = tmp_path / "figure.png"

    save_current_figure(filename)

    assert filename.exists()

    plt.close("all")


def test_manager_save(tmp_path):
    def test_manager_save(tmp_path):
        signal = create_signal()

        manager = plot_signal(signal)

        filename = tmp_path / "manager.png"

        manager.save(filename)

        assert filename.exists()

        manager.close()


