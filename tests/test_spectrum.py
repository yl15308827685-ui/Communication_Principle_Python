"""
Spectrum Module Tests
"""

import numpy as np

from communication import *


def create_signal():

    generator = SignalGenerator()

    return generator.sine(
        amplitude=1.0,
        frequency=100.0,
    )


# ==========================================================
# FFT
# ==========================================================

def test_fft():

    signal = create_signal()

    spectrum = fft(signal)

    assert isinstance(
        spectrum,
        Spectrum,
    )

    assert len(
        spectrum.frequency
    ) == len(signal.value)


# ==========================================================
# IFFT
# ==========================================================

def test_ifft():

    signal = create_signal()

    spectrum = fft(signal)

    restored = ifft(spectrum)

    assert isinstance(
        restored,
        Signal,
    )

    assert len(
        restored.value
    ) == len(signal.value)


# ==========================================================
# Frequency Axis
# ==========================================================

def test_frequency_axis():

    signal = create_signal()

    axis = frequency_axis(
    signal.sampling_frequency,
    len(signal.value),
)

    assert len(axis) == len(signal.value)


def test_frequency_resolution():

    signal = create_signal()

    resolution = frequency_resolution(
        signal.sampling_frequency,
        len(signal.value),
    )

    assert resolution > 0


def test_nyquist_frequency():

    signal = create_signal()

    nyquist = nyquist_frequency(
        signal.sampling_frequency
    )

    assert nyquist == signal.sampling_frequency / 2


# ==========================================================
# FFT Shift
# ==========================================================

def test_fftshift():

    signal = create_signal()

    spectrum = fft(signal)

    shifted = fftshift(spectrum)

    assert isinstance(
        shifted,
        Spectrum,
    )


def test_ifftshift():

    signal = create_signal()

    spectrum = fft(signal)

    shifted = fftshift(spectrum)

    restored = ifftshift(shifted)

    assert isinstance(
        restored,
        Spectrum,
    )


# ==========================================================
# Spectrum Type
# ==========================================================

def test_single_side():

    signal = create_signal()

    spectrum = fft(signal)

    single = single_side(spectrum)

    assert isinstance(
        single,
        Spectrum,
    )


def test_double_side():

    signal = create_signal()

    spectrum = fft(signal)

    double = double_side(spectrum)

    assert isinstance(
        double,
        Spectrum,
    )


# ==========================================================
# dB
# ==========================================================

def test_to_db():

    signal = create_signal()

    spectrum = fft(signal)

    db = to_db(spectrum)

    assert isinstance(
        db,
        Spectrum,
    )


def test_from_db():

    signal = create_signal()

    spectrum = fft(signal)

    db = to_db(spectrum)

    linear = from_db(db)

    assert isinstance(
        linear,
        Spectrum,
    )


# ==========================================================
# Statistics
# ==========================================================

def test_peak_frequency():

    signal = create_signal()

    spectrum = fft(signal)

    peak = peak_frequency(spectrum)

    assert isinstance(
        peak,
        float,
    )


def test_peak_magnitude():

    signal = create_signal()

    spectrum = fft(signal)

    peak = peak_magnitude(spectrum)

    assert peak >= 0


def test_bandwidth():

    signal = create_signal()

    spectrum = fft(signal)

    bw = bandwidth(spectrum)

    assert bw >= 0


def test_spectrum_energy():

    signal = create_signal()

    spectrum = fft(signal)

    energy = spectrum_energy(spectrum)

    assert energy >= 0


def test_spectrum_power():

    signal = create_signal()

    spectrum = fft(signal)

    power = spectrum_power(spectrum)

    assert power >= 0