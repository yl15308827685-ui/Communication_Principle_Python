"""
==========================================================
Communication_Principle_Python

File:
    utils.py

Version:
    1.1.0

Description:
    公共工具函数
    Python 3.9 Compatible

==========================================================
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable
from typing import Optional

import numpy as np

from .models import Signal


# ==========================================================
# 时间轴
# ==========================================================

def time_axis(
    sampling_frequency: float,
    duration: float
) -> np.ndarray:
    """
    生成时间轴
    """

    dt = 1.0 / sampling_frequency

    return np.arange(

        -duration / 2,

        duration / 2,

        dt,

        dtype=float

    )


# ==========================================================
# FFT频率轴
# ==========================================================

def frequency_axis(
    sampling_frequency: float,
    fft_points: int,
    shift: bool = True
) -> np.ndarray:
    """
    生成FFT频率轴
    """

    frequency = np.fft.fftfreq(

        fft_points,

        d=1.0 / sampling_frequency

    )

    if shift:

        frequency = np.fft.fftshift(

            frequency

        )

    return frequency


# ==========================================================
# 最大值归一化
# ==========================================================

def normalize(
    x: np.ndarray
) -> np.ndarray:
    """
    最大值归一化
    """

    x = np.asarray(

        x,

        dtype=float

    )

    maximum = np.max(

        np.abs(x)

    )

    if maximum <= 0:

        return x.copy()

    return x / maximum


# ==========================================================
# RMS归一化
# ==========================================================

def normalize_rms(
    x: np.ndarray
) -> np.ndarray:
    """
    RMS归一化
    """

    x = np.asarray(

        x,

        dtype=float

    )

    rms = np.sqrt(

        np.mean(

            x ** 2

        )

    )

    if rms <= 0:

        return x.copy()

    return x / rms


# ==========================================================
# 幅度→dB
# ==========================================================

def to_db(
    x: np.ndarray,
    floor: float = -120.0
) -> np.ndarray:
    """
    幅度转dB
    """

    x = np.maximum(

        np.abs(x),

        1e-12

    )

    db = 20.0 * np.log10(x)

    db = np.maximum(

        db,

        floor

    )

    return db


# ==========================================================
# dB→幅度
# ==========================================================

def from_db(
    db: np.ndarray
) -> np.ndarray:
    """
    dB转幅度
    """

    db = np.asarray(

        db,

        dtype=float

    )

    return np.power(

        10.0,

        db / 20.0

    )


# ==========================================================
# 功率→dB
# ==========================================================

def power_to_db(
    power: np.ndarray
) -> np.ndarray:
    """
    功率转dB
    """

    power = np.maximum(

        power,

        1e-20

    )

    return 10.0 * np.log10(power)


# ==========================================================
# dB→功率
# ==========================================================

def db_to_power(
    db: np.ndarray
) -> np.ndarray:
    """
    dB转功率
    """

    db = np.asarray(

        db,

        dtype=float

    )

    return np.power(

        10.0,

        db / 10.0

    )


# ==========================================================
# Signal检查
# ==========================================================

def check_signal(
    signal: Signal
):
    """
    检查Signal合法性
    """

    if len(signal.time) != len(signal.value):

        raise ValueError(

            "Signal.time与Signal.value长度不一致。"

        )

    if signal.sampling_frequency <= 0:

        raise ValueError(

            "sampling_frequency必须大于0。"

        )


# ==========================================================
# 数组长度检查
# ==========================================================

def check_same_length(
    *arrays: Iterable
):
    """
    检查多个数组长度
    """

    if len(arrays) <= 1:

        return

    length = len(arrays[0])

    for array in arrays[1:]:

        if len(array) != length:

            raise ValueError(

                "数组长度不一致。"

            )

# ==========================================================
# Frequency Unit Conversion
# ==========================================================

def hz_to_khz(value):
    """
    Hz → kHz
    """
    return np.asarray(value, dtype=float) / 1_000.0


def khz_to_hz(value):
    """
    kHz → Hz
    """
    return np.asarray(value, dtype=float) * 1_000.0


def hz_to_mhz(value):
    """
    Hz → MHz
    """
    return np.asarray(value, dtype=float) / 1_000_000.0


def mhz_to_hz(value):
    """
    MHz → Hz
    """
    return np.asarray(value, dtype=float) * 1_000_000.0

# ==========================================================
# FFT Utilities
# ==========================================================

import numpy as np


def next_power_of_two(n: int) -> int:
    """
    Return the smallest power of two greater than or equal to n.
    """
    if n <= 1:
        return 1
    return 1 << (n - 1).bit_length()


def zero_padding(x, target_length: int):
    """
    Zero-pad a 1-D sequence to the specified length.
    """
    x = np.asarray(x)

    if target_length <= len(x):
        return x.copy()

    y = np.zeros(target_length, dtype=x.dtype)
    y[:len(x)] = x
    return y


# ==========================================================
# Window Functions
# ==========================================================

def hann_window(length: int):
    return np.hanning(length)


def hamming_window(length: int):
    return np.hamming(length)


def blackman_window(length: int):
    return np.blackman(length)


