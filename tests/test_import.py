"""
==========================================================

Communication_Principle_Python

File:
    test_import.py

Description:
    Import tests for Communication SDK

Python:
    >=3.9

==========================================================
"""

import numpy as np

import communication as comm


def test_package_import():
    """SDK package can be imported."""

    assert comm is not None
    assert hasattr(comm, "__version__")


def test_version():
    """Version string exists."""

    assert isinstance(comm.__version__, str)
    assert len(comm.__version__) > 0


def test_signal_generator():
    """SignalGenerator can be instantiated."""

    cfg = comm.ExperimentConfig()

    gen = comm.SignalGenerator(cfg)

    assert gen is not None


def test_generate_sine():
    """Generate a sine signal."""

    cfg = comm.ExperimentConfig()

    gen = comm.SignalGenerator(cfg)

    signal = gen.sine()

    assert signal is not None

    assert signal.sample_count > 0

    assert len(signal.time) == len(signal.value)

    assert np.isfinite(signal.value).all()


def test_fft():
    """FFT interface works."""

    cfg = comm.ExperimentConfig()

    gen = comm.SignalGenerator(cfg)

    signal = gen.sine()

    spectrum = comm.fft(signal)

    assert spectrum is not None

    assert spectrum.frequency is not None
    assert spectrum.magnitude is not None
    assert spectrum.phase is not None
    assert spectrum.complex_value is not None

    assert len(spectrum.frequency) == spectrum.sample_count
    assert len(spectrum.magnitude) == spectrum.sample_count
    assert len(spectrum.phase) == spectrum.sample_count
    assert len(spectrum.complex_value) == spectrum.sample_count

    assert np.isfinite(spectrum.magnitude).all()


def test_rms():
    """Analysis interface works."""

    cfg = comm.ExperimentConfig()

    gen = comm.SignalGenerator(cfg)

    signal = gen.sine()

    value = comm.rms(signal)

    assert isinstance(value, (float, np.floating))

    assert value > 0