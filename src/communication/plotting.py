"""
==========================================================
Communication_Principle_Python

File:
    plotting.py

Version:
    1.1.0

Description:
    出版级绘图模块
    Python 3.9 Compatible

==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional
from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np

from .config import ExperimentConfig
from .models import Signal
from .models import Spectrum


# ==========================================================
# 默认绘图风格
# ==========================================================

@dataclass
class PlotStyle:

    linewidth: float = 2.0

    linestyle: str = "-"

    marker: str = ""

    alpha: float = 1.0

    grid: bool = True

    dpi: int = 300

    figsize: Tuple[float, float] = (10, 4)

    title_size: int = 15

    label_size: int = 12

    tick_size: int = 11

    legend_size: int = 11


# ==========================================================
# Figure管理器
# ==========================================================

class FigureManager:

    def __init__(

        self,

        config: Optional[ExperimentConfig] = None

    ):

        self.config = config or ExperimentConfig()

        self.style = PlotStyle()

        self._configure_matplotlib()

    # ------------------------------------------------------

    @staticmethod
    def _configure_matplotlib():

        plt.rcParams["figure.dpi"] = 300

        plt.rcParams["axes.grid"] = True

        plt.rcParams["grid.linestyle"] = "--"

        plt.rcParams["grid.alpha"] = 0.35

        plt.rcParams["axes.unicode_minus"] = False

        # Windows / Linux / Mac 自动兼容

        plt.rcParams["font.sans-serif"] = [

            "Microsoft YaHei",

            "SimHei",

            "PingFang SC",

            "Noto Sans CJK SC",

            "Arial Unicode MS",

            "DejaVu Sans"

        ]

    # ------------------------------------------------------

    def figure(

        self,

        width: Optional[float] = None,

        height: Optional[float] = None

    ):

        width = width or self.config.figure_width

        height = height or self.config.figure_height

        return plt.figure(

            figsize=(width, height),

            dpi=self.style.dpi

        )

    # ------------------------------------------------------

    @staticmethod
    def close():

        plt.close()

    # ------------------------------------------------------

    @staticmethod
    def show():

        plt.show()


# ==========================================================
# 时间域绘图
# ==========================================================

def plot_signal(

    signal: Signal,

    title: Optional[str] = None,

    color: str = "tab:blue",

    linewidth: float = 2.0

):

    plt.plot(

        signal.time,

        signal.value,

        color=color,

        linewidth=linewidth,

        label=signal.name

    )

    plt.xlabel("Time (s)")

    plt.ylabel(signal.unit)

    plt.grid(True)

    if title:

        plt.title(title)

    else:

        plt.title(signal.name)

    plt.legend()


# ==========================================================
# 双边频谱
# ==========================================================

def plot_spectrum(

    spectrum: Spectrum,

    title: Optional[str] = None,

    color: str = "tab:red"

):

    plt.plot(

        spectrum.frequency,

        spectrum.magnitude,

        color=color,

        linewidth=2

    )

    plt.xlabel("Frequency (Hz)")

    plt.ylabel("Magnitude")

    plt.grid(True)

    if title:

        plt.title(title)

    else:

        plt.title(spectrum.name)

# ==========================================================
# 单边频谱绘图
# ==========================================================

def plot_single_spectrum(
    spectrum: Spectrum,
    title: Optional[str] = None,
    color: str = "tab:blue",
    linewidth: float = 2.0
):
    """
    绘制单边频谱
    """

    plt.plot(
        spectrum.frequency,
        spectrum.magnitude,
        color=color,
        linewidth=linewidth,
        label=spectrum.name
    )

    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid(True)

    if title is None:
        title = spectrum.name

    plt.title(title)
    plt.legend()


# ==========================================================
# FFT与理论频谱对比
# ==========================================================

def plot_compare(
    frequency: np.ndarray,
    fft_value: np.ndarray,
    theory_value: np.ndarray,
    title: str = "FFT vs Theory"
):
    """
    FFT频谱与理论频谱对比
    """

    plt.plot(
        frequency,
        fft_value,
        linewidth=2,
        label="FFT"
    )

    plt.plot(
        frequency,
        theory_value,
        "--",
        linewidth=2,
        label="Theory"
    )

    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.title(title)
    plt.grid(True)
    plt.legend()


# ==========================================================
# 双子图：时域 + 频域
# ==========================================================

def plot_signal_and_spectrum(
    signal: Signal,
    spectrum: Spectrum
):
    """
    同时绘制时域与频域
    """

    plt.figure(figsize=(10, 7))

    plt.subplot(2, 1, 1)

    plot_signal(
        signal,
        title=signal.name
    )

    plt.subplot(2, 1, 2)

    plot_spectrum(
        spectrum,
        title=spectrum.name
    )

    plt.tight_layout()


# ==========================================================
# 设置时间轴
# ==========================================================

def set_time_axis(
    xmin: float,
    xmax: float
):
    """
    设置时间轴范围
    """

    plt.xlim(xmin, xmax)


# ==========================================================
# 设置频率轴
# ==========================================================

def set_frequency_axis(
    xmin: float,
    xmax: float
):
    """
    设置频率轴范围
    """

    plt.xlim(xmin, xmax)


# ==========================================================
# 设置标题
# ==========================================================

def add_title(
    title: str
):
    """
    设置标题
    """

    plt.title(title)


# ==========================================================
# 设置X轴
# ==========================================================

def add_xlabel(
    label: str
):
    """
    设置X轴标题
    """

    plt.xlabel(label)


# ==========================================================
# 设置Y轴
# ==========================================================

def add_ylabel(
    label: str
):
    """
    设置Y轴标题
    """

    plt.ylabel(label)


# ==========================================================
# 图例
# ==========================================================

def add_legend():
    """
    添加图例
    """

    plt.legend()


# ==========================================================
# 当前图保存
# ==========================================================

def save_current_figure(
    filename: str,
    dpi: int = 300
):
    """
    保存当前图像
    """

    plt.savefig(
        filename,
        dpi=dpi,
        bbox_inches="tight"
    )


# ==========================================================
# 清空当前图
# ==========================================================

def clear():
    """
    清空当前图形
    """

    plt.clf()


# ==========================================================
# End of File
# ==========================================================