"""
==========================================================
Communication_Principle_Python

File:
    spectrum.py

Version:
    1.1.0

Description:
    频谱分析模块（Python 3.9 Compatible）

提供：

    • FFT
    • FFT Shift
    • 单边频谱
    • 双边频谱
    • 功率谱
    • 理论矩形脉冲频谱

==========================================================
"""

from __future__ import annotations

from typing import Dict
from typing import Tuple

import numpy as np

from .models import Signal
from .models import Spectrum


class SpectrumAnalyzer:
    """
    统一频谱分析器
    """

    # =====================================================
    # FFT
    # =====================================================

    def fft(
        self,
        signal: Signal,
        normalize: bool = True
    ) -> Spectrum:

        x = np.asarray(signal.value)

        n = len(x)

        spectrum = np.fft.fft(x)

        frequency = np.fft.fftfreq(
            n,
            d=signal.dt
        )

        spectrum = np.fft.fftshift(spectrum)

        frequency = np.fft.fftshift(frequency)

        magnitude = np.abs(spectrum)

        if normalize:

            magnitude = magnitude / n

        phase = np.angle(spectrum)

        return Spectrum(

            frequency=frequency,

            magnitude=magnitude,

            phase=phase,

            complex_value=spectrum,

            sampling_rate=signal.sampling_rate,

        )

    # =====================================================
    # 双边频谱
    # =====================================================

    def double_side(
        self,
        signal: Signal
    ) -> Spectrum:

        return self.fft(signal)

    # =====================================================
    # 单边频谱
    # =====================================================

    def single_side(
        self,
        signal: Signal
    ) -> Spectrum:

        x = np.asarray(signal.value)

        n = len(x)

        fft = np.fft.rfft(x)

        frequency = np.fft.rfftfreq(

            n,

            d=signal.dt

        )

        magnitude = np.abs(fft) / n

        if len(magnitude) > 2:

            magnitude[1:-1] *= 2

        phase = np.angle(fft)

        return Spectrum(

            frequency=frequency,

            complex_value=fft,

            magnitude=magnitude,

            phase=phase,

            sampling_rate=signal.sampling_rate

        )

    # =====================================================
    # 功率谱
    # =====================================================

    def power_spectrum(
        self,
        signal: Signal
    ) -> Spectrum:

        result = self.fft(signal)

        return Spectrum(

            frequency=result.frequency,

            complex_value=result.complex_value,

            magnitude=result.magnitude ** 2,

            phase=result.phase,

            sampling_rate=signal.sampling_rate

        )

    # =====================================================
    # FFT Shift
    # =====================================================

    @staticmethod
    def fft_shift(
        spectrum: Spectrum

    ) -> Spectrum:

        return Spectrum(

            frequency=np.fft.fftshift(
                spectrum.frequency
            ),

            complex_value=np.fft.fftshift(
                spectrum.complex_value
            ),

            magnitude=np.fft.fftshift(
                spectrum.magnitude
            ),

            phase=np.fft.fftshift(
                spectrum.phase
            ),

            sampling_rate=spectrum.sampling_rate

        )

    # =====================================================
    # 理论矩形脉冲频谱
    # =====================================================

    @staticmethod
    def rectangle_theory(
        amplitude: float,
        width: float,
        frequency: np.ndarray
    ) -> np.ndarray:
        """
        X(f)=Aτsinc(fτ)
        """

        return (

            amplitude *

            width *

            np.sinc(

                frequency *

                width

            )

        )
    # =====================================================
    # FFT频谱与理论频谱比较
    # =====================================================

    @staticmethod
    def compare(
        fft_spectrum: Spectrum,
        theory: np.ndarray
    ) -> Dict[str, float]:
        """
        比较FFT频谱与理论频谱

        Returns
        -------
        Dict
            max_error
            mean_error
            rmse
        """

        fft_mag = np.asarray(
            fft_spectrum.magnitude,
            dtype=float
        )

        theory = np.asarray(
            theory,
            dtype=float
        )

        if fft_mag.shape != theory.shape:
            raise ValueError(
                "FFT频谱与理论频谱长度不一致。"
            )

        error = fft_mag - theory

        return {

            "max_error": float(
                np.max(np.abs(error))
            ),

            "mean_error": float(
                np.mean(np.abs(error))
            ),

            "rmse": float(
                np.sqrt(
                    np.mean(error ** 2)
                )
            )

        }

    # =====================================================
    # 峰值检测
    # =====================================================

    @staticmethod
    def peak(
        spectrum: Spectrum
    ) -> Tuple[float, float]:
        """
        返回最大峰值
        """

        index = np.argmax(
            spectrum.magnitude
        )

        return (

            float(
                spectrum.frequency[index]
            ),

            float(
                spectrum.magnitude[index]
            )

        )

    # =====================================================
    # 第一零点
    # =====================================================

    @staticmethod
    def first_zero(
        spectrum: Spectrum,
        threshold: float = 1e-6
    ) -> float:
        """
        自动寻找第一零点
        """

        freq = spectrum.frequency
        mag = spectrum.magnitude

        center = np.argmin(np.abs(freq))

        for i in range(center + 1, len(freq)):

            if mag[i] <= threshold:

                return float(freq[i])

        return float("nan")

    # =====================================================
    # 主瓣宽度
    # =====================================================

    @staticmethod
    def main_lobe_width(
        spectrum: Spectrum
    ) -> float:
        """
        根据第一零点估计主瓣宽度
        """

        zero = SpectrumAnalyzer.first_zero(
            spectrum
        )

        if np.isnan(zero):

            return float("nan")

        return abs(zero) * 2.0

    # =====================================================
    # 幅度归一化
    # =====================================================

    @staticmethod
    def normalize(
        spectrum: Spectrum
    ) -> Spectrum:

        maximum = np.max(
            spectrum.magnitude
        )

        if maximum <= 0:

            return spectrum

        return Spectrum(

            frequency=spectrum.frequency.copy(),

            complex_value=spectrum.complex_value.copy(),

            magnitude=spectrum.magnitude / maximum,

            phase=spectrum.phase.copy(),

            sampling_rate=spectrum.sampling_rate

        )

    # =====================================================
    # dB频谱
    # =====================================================

    @staticmethod
    def to_db(
        spectrum: Spectrum,
        floor: float = -120.0
    ) -> Spectrum:
        """
        转换为dB频谱
        """

        magnitude = np.maximum(
            spectrum.magnitude,
            1e-12
        )

        db = 20.0 * np.log10(
            magnitude
        )

        db = np.maximum(
            db,
            floor
        )

        return Spectrum(

            frequency=spectrum.frequency.copy(),

            complex_value=spectrum.complex_value.copy(),

            magnitude=db,

            phase=spectrum.phase.copy(),

            sampling_rate=spectrum.sampling_rate

        )


# ==========================================================
# 快捷接口函数
# ==========================================================

_default_analyzer = SpectrumAnalyzer()


def fft(
    signal: Signal
) -> Spectrum:
    """
    FFT快捷接口
    """

    return _default_analyzer.fft(signal)


def double_side(
    signal: Signal
) -> Spectrum:
    """
    双边频谱快捷接口
    """

    return _default_analyzer.double_side(signal)


def single_side(
    signal: Signal
) -> Spectrum:
    """
    单边频谱快捷接口
    """

    return _default_analyzer.single_side(signal)


def power_spectrum(
    signal: Signal
) -> Spectrum:
    """
    功率谱快捷接口
    """

    return _default_analyzer.power_spectrum(signal)


def normalize(
    spectrum: Spectrum
) -> Spectrum:
    """
    幅度归一化快捷接口
    """

    return SpectrumAnalyzer.normalize(
        spectrum
    )


def to_db(
    spectrum: Spectrum
) -> Spectrum:
    """
    dB频谱快捷接口
    """

    return SpectrumAnalyzer.to_db(
        spectrum
    )


# ==========================================================
# End of File
# ==========================================================