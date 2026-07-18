"""
Communication_Principle_Python

Unit Test

Window Functions
"""

import numpy as np

from communication.window import (
    rectangular,
    hann,
    hamming,
    blackman,
    apply_window,
)

from communication.signals import SignalGenerator
from communication.config import DEFAULT_CONFIG


def test_rectangular():

    w = rectangular(64)

    assert len(w) == 64

    assert np.allclose(w, np.ones(64))


def test_hann():

    w = hann(128)

    assert len(w) == 128

    assert np.max(w) <= 1.0

    assert np.min(w) >= 0.0


def test_hamming():

    w = hamming(256)

    assert len(w) == 256

    assert np.max(w) <= 1.0

    assert np.min(w) >= 0.0


def test_blackman():

    w = blackman(512)

    assert len(w) == 512

    assert np.max(w) <= 1.0


def test_apply_window():

    generator = SignalGenerator(DEFAULT_CONFIG)

    signal = generator.sine()

    window_signal = apply_window(

        signal,

        "hann",

    )

    assert len(window_signal) == len(signal)

    assert window_signal.info["window"] == "hann"

    assert window_signal.name.endswith("[hann]")


def test_supported_windows():

    from communication.window import supported_windows

    names = supported_windows()

    assert "rectangular" in names

    assert "hann" in names

    assert "hamming" in names

    assert "blackman" in names