"""
Analysis Module Tests
"""

import numpy as np

from communication import *


def create_signal():

    generator = SignalGenerator()

    return generator.sine(
        amplitude=2.0,
        frequency=100.0,
    )


# ==========================================================
# Statistics
# ==========================================================

def test_mean():

    signal = create_signal()

    value = mean(signal)

    assert isinstance(value, float)


def test_maximum():

    signal = create_signal()

    value = maximum(signal)

    assert value > 0


def test_minimum():

    signal = create_signal()

    value = minimum(signal)

    assert value < 0


def test_rms():

    signal = create_signal()

    value = rms(signal)

    assert value > 0


def test_variance():

    signal = create_signal()

    value = variance(signal)

    assert value >= 0


def test_standard_deviation():

    signal = create_signal()

    value = standard_deviation(signal)

    assert value >= 0


def test_peak_to_peak():

    signal = create_signal()

    value = peak_to_peak(signal)

    assert value > 0


def test_crest_factor():

    signal = create_signal()

    value = crest_factor(signal)

    assert value > 0


# ==========================================================
# Energy
# ==========================================================

def test_energy():

    signal = create_signal()

    value = energy(signal)

    assert value > 0


def test_average_power():

    signal = create_signal()

    value = average_power(signal)

    assert value > 0


# ==========================================================
# Error
# ==========================================================

def test_mae():

    signal = create_signal()

    value = mae(signal, signal)

    assert value == 0.0


def test_mse():

    signal = create_signal()

    value = mse(signal, signal)

    assert value == 0.0


def test_rmse():

    signal = create_signal()

    value = rmse(signal, signal)

    assert value == 0.0


# ==========================================================
# Correlation
# ==========================================================

def test_correlation():

    signal = create_signal()

    value = correlation(signal, signal)

    assert np.isclose(
        value,
        1.0,
        atol=1e-6,
    )


def test_auto_correlation():

    signal = create_signal()

    value = auto_correlation(signal)

    assert isinstance(
        value,
        np.ndarray,
    )


def test_cross_correlation():

    signal = create_signal()

    value = cross_correlation(
        signal,
        signal,
    )

    assert isinstance(
        value,
        np.ndarray,
    )


# ==========================================================
# Analyzer
# ==========================================================

def test_analyze():

    signal = create_signal()

    result = analyze(signal)

    assert isinstance(
        result,
        SignalStatistics,
    )


def test_signal_analyzer():

    signal = create_signal()

    analyzer = SignalAnalyzer()

    result = analyzer.analyze(signal)

    assert isinstance(
        result,
        SignalStatistics,
    )