"""
==========================================================

Communication_Principle_Python

File:
    test_signal.py

Description:
    Signal Module Unit Test

Python:
    >=3.9

==========================================================
"""

import numpy as np
import pytest

import communication as comm


# ==========================================================
# Helper
# ==========================================================

def assert_signal(signal):

    assert signal is not None

    assert isinstance(signal, comm.Signal)

    assert len(signal.time) == len(signal.value)

    assert signal.sample_count == len(signal.value)

    assert signal.sampling_frequency > 0

    assert signal.duration > 0


# ==========================================================
# Signal Generator
# ==========================================================

def test_rectangle(generator):

    signal = generator.rectangle()

    assert_signal(signal)

    assert signal.name == "Rectangle Pulse"

    assert np.max(signal.value) > 0

    assert np.min(signal.value) == 0


def test_sine(generator):

    signal = generator.sine()

    assert_signal(signal)

    assert signal.name == "Sine Wave"

    assert np.max(signal.value) <= 1.01

    assert np.min(signal.value) >= -1.01


def test_cosine(generator):

    signal = generator.cosine()

    assert_signal(signal)

    assert signal.name == "Cosine Wave"

    assert np.max(signal.value) <= 1.01

    assert np.min(signal.value) >= -1.01


def test_impulse(generator):

    signal = generator.impulse()

    assert_signal(signal)

    assert signal.name == "Unit Impulse"

    assert np.count_nonzero(signal.value) == 1


def test_step(generator):

    signal = generator.step()

    assert_signal(signal)

    assert signal.name == "Unit Step"

    assert np.min(signal.value) == 0

    assert np.max(signal.value) > 0


# ==========================================================
# copy_signal
# ==========================================================

def test_copy_signal(sine):

    copied = comm.copy_signal(sine)

    assert copied is not sine

    assert np.array_equal(

        copied.time,

        sine.time

    )

    assert np.array_equal(

        copied.value,

        sine.value

    )

    assert copied.info == sine.info


# ==========================================================
# normalize
# ==========================================================

def test_normalize(sine):

    result = comm.normalize(sine)

    assert np.isclose(

        np.max(np.abs(result.value)),

        1.0,

        atol=1e-8

    )

    assert result.info["normalized"] is True


# ==========================================================
# normalize_rms
# ==========================================================

def test_normalize_rms(sine):

    result = comm.normalize_rms(sine)

    rms = np.sqrt(

        np.mean(

            result.value ** 2

        )

    )

    assert np.isclose(

        rms,

        1.0,

        atol=1e-8

    )

    assert result.info["normalized_rms"] is True
