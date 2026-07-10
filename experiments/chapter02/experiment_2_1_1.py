"""
==========================================================
Experiment 2.1.1

矩形脉冲信号

通信原理（Python版）

==========================================================
"""

from pathlib import Path
import sys

# ---------------------------------------------------------
# 将src加入Python搜索路径
# ---------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

# ---------------------------------------------------------

import matplotlib.pyplot as plt

from communication import (
    ExperimentConfig,
    SignalGenerator,
    save_png,
)

# ---------------------------------------------------------
# 实验参数
# ---------------------------------------------------------

config = ExperimentConfig(

    sampling_frequency=10000,

    duration=0.02,

    amplitude=1.0,

    pulse_width=0.004

)

# ---------------------------------------------------------
# 信号生成
# ---------------------------------------------------------

generator = SignalGenerator(config)

signal = generator.rectangle()

# ---------------------------------------------------------
# 绘图
# ---------------------------------------------------------

plt.figure(figsize=(9,4))

plt.plot(

    signal.time,

    signal.value,

    linewidth=2

)

plt.grid(True)

plt.xlabel("Time (s)")

plt.ylabel("Amplitude")

plt.title("Rectangular Pulse")

plt.xlim(

    -config.duration/2,

    config.duration/2

)

plt.ylim(

    -0.2,

    1.2

)

plt.tight_layout()

# ---------------------------------------------------------
# 保存图片
# ---------------------------------------------------------

save_png(

    "experiment_2_1_1.png"

)

# ---------------------------------------------------------

plt.show()

print()

print("="*60)

print("Experiment 2.1.1 Finished")

print("Signal Name :", signal.name)

print("Samples     :", signal.sample_count)

print("Duration(s) :", signal.duration)

print("="*60)