"""
==========================================================
Communication_Principle_Python

File:
    config.py

Version:
    1.1.0

Description:
    全局实验配置（Python 3.9 Compatible）

==========================================================
"""

from dataclasses import dataclass
from pathlib import Path


# ==========================================================
# 工程目录
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

SRC_DIR = PROJECT_ROOT / "src"

EXPERIMENT_DIR = PROJECT_ROOT / "experiments"

OUTPUT_DIR = PROJECT_ROOT / "output"

IMAGE_DIR = OUTPUT_DIR / "assets"

DATA_DIR = OUTPUT_DIR / "data"

DOC_DIR = OUTPUT_DIR / "documents"


# 自动创建输出目录
for directory in (
    OUTPUT_DIR,
    IMAGE_DIR,
    DATA_DIR,
    DOC_DIR,
):
    directory.mkdir(parents=True, exist_ok=True)


# ==========================================================
# 默认实验参数
# ==========================================================

@dataclass
class ExperimentConfig:
    """
    实验配置类
    """

    # ---------- 采样参数 ----------

    sampling_frequency: float = 10000.0

    duration: float = 0.02

    # ---------- 信号参数 ----------

    amplitude: float = 1.0

    frequency: float = 100.0

    phase: float = 0.0

    pulse_width: float = 0.004

    # ---------- FFT ----------

    fft_points: int = 4096

    # ---------- 绘图 ----------

    figure_width: float = 10.0

    figure_height: float = 4.0

    dpi: int = 300

    grid: bool = True

    # ---------- 保存 ----------

    save_figure: bool = True

    save_data: bool = False

    image_format: str = "png"


# ==========================================================
# 默认配置对象
# ==========================================================

DEFAULT_CONFIG = ExperimentConfig()


# ==========================================================
# 路径工具函数
# ==========================================================

def image_path(filename: str) -> Path:
    """
    图片输出路径
    """
    return IMAGE_DIR / filename


def data_path(filename: str) -> Path:
    """
    数据输出路径
    """
    return DATA_DIR / filename


def document_path(filename: str) -> Path:
    """
    文档输出路径
    """
    return DOC_DIR / filename