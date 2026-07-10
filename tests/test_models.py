"""
tests/test_models.py

Communication_Principle_Python v2.0
"""

import numpy as np

import communication as comm


# ============================================================
# Signal
# ============================================================

def test_signal():

    x = np.arange(100)

    signal = comm.Signal(

        value=x,

        sampling_rate=1000

    )

    assert signal.samples == 100

    assert signal.sampling_rate == 1000

    assert len(signal.time) == 100

    assert signal.duration == 0.1


def test_signal_copy():

    signal = comm.Signal(

        value=np.random.randn(128),

        sampling_rate=8000

    )

    copied = signal.copy()

    assert copied is not signal

    assert np.array_equal(

        copied.value,

        signal.value

    )


# ============================================================
# Spectrum
# ============================================================

def test_spectrum():

    frequency = np.linspace(

        0,

        500,

        256

    )

    magnitude = np.random.rand(256)

    phase = np.random.rand(256)

    complex_value = (

        magnitude *

        np.exp(1j * phase)

    )

    spectrum = comm.Spectrum(

        frequency=frequency,

        magnitude=magnitude,

        phase=phase,

        complex_value=complex_value,

        sampling_rate=1000

    )

    assert spectrum.bins == 256

    assert len(spectrum) == 256

    assert spectrum.nyquist == 500


def test_spectrum_copy():

    frequency = np.arange(128)

    magnitude = np.ones(128)

    phase = np.zeros(128)

    complex_value = np.ones(

        128,

        dtype=complex

    )

    spectrum = comm.Spectrum(

        frequency,

        magnitude,

        phase,

        complex_value,

        256

    )

    copied = spectrum.copy()

    assert copied is not spectrum

    assert np.array_equal(

        copied.magnitude,

        spectrum.magnitude

    )


# ============================================================
# SignalStatistics
# ============================================================

def test_statistics():

    stats = comm.SignalStatistics(

        mean=0,

        rms=0.707,

        variance=0.5,

        std=0.707,

        peak=1,

        peak_to_peak=2,

        energy=500,

        power=0.5

    )

    assert stats.rms == 0.707

    assert stats.energy == 500

    assert isinstance(

        stats.as_dict(),

        dict

    )

    # ============================================================
    # AnalysisResult
    # ============================================================

    def test_analysis_result():
        result = comm.AnalysisResult(

            mae=0.01,

            mse=0.001,

            rmse=0.0316,

            correlation=0.998

        )

        assert result.mae == 0.01

        assert result.correlation > 0.99

        assert isinstance(

            result.as_dict(),

            dict

        )

    # ============================================================
    # FilterResult
    # ============================================================

    def test_filter_result():
        signal = comm.Signal(

            value=np.random.randn(128),

            sampling_rate=8000

        )

        result = comm.FilterResult(

            input_signal=signal,

            output_signal=signal.copy(),

            filter_name="LowPass"

        )

        assert result.samples == 128

        assert result.filter_name == "LowPass"

    # ============================================================
    # ModulationResult
    # ============================================================

    def test_modulation_result():
        baseband = comm.Signal(

            np.random.randn(256),

            10000

        )

        carrier = comm.Signal(

            np.random.randn(256),

            10000

        )

        modulated = comm.Signal(

            np.random.randn(256),

            10000

        )

        result = comm.ModulationResult(

            baseband=baseband,

            carrier=carrier,

            modulated=modulated,

            modulation="AM"

        )

        assert result.samples == 256

        assert result.modulation == "AM"

    # ============================================================
    # ChannelResult
    # ============================================================

    def test_channel_result():
        tx = comm.Signal(

            np.random.randn(128),

            8000

        )

        rx = comm.Signal(

            np.random.randn(128),

            8000

        )

        result = comm.ChannelResult(

            transmitted=tx,

            received=rx,

            channel="AWGN",

            snr=20

        )

        assert result.channel == "AWGN"

        assert result.snr == 20

    # ============================================================
    # CodingResult
    # ============================================================

    def test_coding_result():
        source = np.array(

            [1, 0, 1, 1],

            dtype=np.uint8

        )

        coded = np.array(

            [1, 1, 0, 0, 1, 0, 1, 1],

            dtype=np.uint8

        )

        result = comm.CodingResult(

            input_bits=source,

            output_bits=coded,

            coding="Hamming"

        )

        assert result.input_length == 4

        assert result.output_length == 8

        assert result.code_rate == 0.5

    # ============================================================
    # SimulationResult
    # ============================================================

    def test_simulation_result():
        signal = comm.Signal(

            np.random.randn(64),

            1000

        )

        simulation = comm.SimulationResult(

            signal=signal,

            description="Unit Test"

        )

        assert simulation.signal.samples == 64

        assert simulation.description == "Unit Test"