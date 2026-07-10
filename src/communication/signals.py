"""
==========================================================
Communication_Principle_Python

File:
    signals.py

Version:
    1.2.0

Description:
    信号生成模块
    Python 3.9 Compatible

提供：

    • 矩形脉冲
    • 正弦波
    • 余弦波
    • 单位冲激
    • 单位阶跃

==========================================================
"""

from __future__ import annotations

from typing import Optional
from typing import Dict
from typing import Any

import numpy as np

from .config import ExperimentConfig
from .models import Signal


class SignalGenerator:
    """
    信号发生器
    """

    def __init__(
        self,
        config: Optional[ExperimentConfig] = None
    ):

        self.config = config or ExperimentConfig()

        self.time = self._create_time_axis()

    # =====================================================
    # 时间轴
    # =====================================================

    def _create_time_axis(self) -> np.ndarray:

        fs = self.config.sampling_frequency

        duration = self.config.duration

        dt = 1.0 / fs

        return np.arange(

            -duration / 2,

            duration / 2,

            dt,

            dtype=float

        )

    # =====================================================
    # 创建Signal对象
    # =====================================================

    def _build_signal(
            self,
            value: np.ndarray,
            name: str,
            info: Optional[Dict[str, Any]] = None
    ) -> Signal:

        return Signal(

            value=np.asarray(
                value,
                dtype=float
            ),

            sampling_rate=self.config.sampling_frequency,

            time=self.time.copy(),

            name=name,

            unit="V"

        )

    # =====================================================
    # 矩形脉冲
    # =====================================================

    def rectangle(

        self,

        amplitude: Optional[float] = None,

        width: Optional[float] = None

    ) -> Signal:

        if amplitude is None:

            amplitude = self.config.amplitude

        if width is None:

            width = self.config.pulse_width

        value = np.where(

            np.abs(self.time) <= width / 2,

            amplitude,

            0.0

        )

        return self._build_signal(

            value,

            "Rectangle Pulse",

            {

                "amplitude": amplitude,

                "width": width

            }

        )

    # =====================================================
    # 正弦波
    # =====================================================

    def sine(

        self,

        amplitude: Optional[float] = None,

        frequency: Optional[float] = None,

        phase: Optional[float] = None

    ) -> Signal:

        if amplitude is None:

            amplitude = self.config.amplitude

        if frequency is None:

            frequency = self.config.frequency

        if phase is None:

            phase = self.config.phase

        value = amplitude * np.sin(

            2 * np.pi *

            frequency *

            self.time +

            phase

        )

        return self._build_signal(

            value,

            "Sine Wave",

            {

                "amplitude": amplitude,

                "frequency": frequency,

                "phase": phase

            }

        )

    # =====================================================
    # 余弦波
    # =====================================================

    def cosine(

        self,

        amplitude: Optional[float] = None,

        frequency: Optional[float] = None,

        phase: Optional[float] = None

    ) -> Signal:

        if amplitude is None:

            amplitude = self.config.amplitude

        if frequency is None:

            frequency = self.config.frequency

        if phase is None:

            phase = self.config.phase

        value = amplitude * np.cos(

            2 * np.pi *

            frequency *

            self.time +

            phase

        )

        return self._build_signal(

            value,

            "Cosine Wave",

            {

                "amplitude": amplitude,

                "frequency": frequency,

                "phase": phase

            }

        )

    # =====================================================
    # 单位冲激
    # =====================================================

    def impulse(
        self,
        amplitude: Optional[float] = None
    ) -> Signal:

        if amplitude is None:
            amplitude = self.config.amplitude

        value = np.zeros_like(self.time)

        index = len(value) // 2

        value[index] = amplitude

        return self._build_signal(

            value,

            "Unit Impulse",

            {
                "amplitude": amplitude
            }

        )

    # =====================================================
    # 单位阶跃
    # =====================================================

    def step(
        self,
        amplitude: Optional[float] = None
    ) -> Signal:

        if amplitude is None:
            amplitude = self.config.amplitude

        value = np.where(
            self.time >= 0,
            amplitude,
            0.0
        )

        return self._build_signal(

            value,

            "Unit Step",

            {
                "amplitude": amplitude
            }

        )


# ==========================================================
# 工具函数
# ==========================================================

def copy_signal(signal: Signal) -> Signal:
    """
    深拷贝Signal对象
    """

    return Signal(

        time=signal.time.copy(),

        value=signal.value.copy(),

        sampling_rate=signal.sampling_frequency,

        name=signal.name,

        unit=signal.unit,

    )


# ==========================================================
# 最大值归一化
# ==========================================================

def normalize(signal: Signal) -> Signal:
    """
    最大值归一化
    """

    result = copy_signal(signal)

    maximum = np.max(np.abs(result.value))

    if maximum > 0:

        result.value = result.value / maximum

    result.info["normalized"] = True

    return result


# ==========================================================
# RMS归一化
# ==========================================================

def normalize_rms(signal: Signal) -> Signal:
    """
    RMS归一化
    """

    result = copy_signal(signal)

    rms = np.sqrt(np.mean(result.value ** 2))

    if rms > 0:

        result.value = result.value / rms

    result.info["normalized_rms"] = True

    return result


# ==========================================================
# 幅度缩放
# ==========================================================

def scale(
    signal: Signal,
    factor: float
) -> Signal:
    """
    幅度缩放
    """

    result = copy_signal(signal)

    result.value = result.value * factor

    result.info["scale"] = factor

    return result


# ==========================================================
# 时间平移
# ==========================================================

def shift(
    signal: Signal,
    delay: float
) -> Signal:
    """
    时间平移（仅修改时间轴）
    """

    result = copy_signal(signal)

    result.time = result.time + delay

    result.info["delay"] = delay

    return result


# ==========================================================
# 时间反转
# ==========================================================

def reverse(
    signal: Signal
) -> Signal:
    """
    时间反转 x(-t)
    """

    result = copy_signal(signal)

    result.time = -result.time[::-1]

    result.value = result.value[::-1]

    result.info["reversed"] = True

    return result


# ==========================================================
# 幅度偏置
# ==========================================================

def offset(
    signal: Signal,
    bias: float
) -> Signal:
    """
    增加直流偏置
    """

    result = copy_signal(signal)

    result.value = result.value + bias

    result.info["offset"] = bias

    return result


# ==========================================================
# 信号相加
# ==========================================================

def add(
    signal1: Signal,
    signal2: Signal
) -> Signal:
    """
    两个信号相加
    """

    if len(signal1.value) != len(signal2.value):

        raise ValueError("两个信号长度不一致。")

    result = copy_signal(signal1)

    result.value = signal1.value + signal2.value

    result.name = signal1.name + " + " + signal2.name

    return result


# ==========================================================
# 信号相乘
# ==========================================================

def multiply(
    signal1: Signal,
    signal2: Signal
) -> Signal:
    """
    两个信号相乘
    """

    if len(signal1.value) != len(signal2.value):

        raise ValueError("两个信号长度不一致。")

    result = copy_signal(signal1)

    result.value = signal1.value * signal2.value

    result.name = signal1.name + " × " + signal2.name

    return result


# ==========================================================
# End of File
# ==========================================================