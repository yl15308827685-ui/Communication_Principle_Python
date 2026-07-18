"""
实验1：矩形脉冲信号

教材：
第一章 信号
1.2 矩形脉冲

功能：

1. 生成矩形脉冲
2. 绘制波形
3. 导出CSV
4. 保存图片
"""

from pathlib import Path

from communication.signals import SignalGenerator
from communication.plotting import plot_signal
from communication.export import export_signal_csv


from pathlib import Path

from communication.paths import experiment_output_dir

OUTPUT_DIR = experiment_output_dir(
    1,
    "exp01_generate_rectangle",
)


def main():

    generator = SignalGenerator()

    signal = generator.rectangle(
        amplitude=1.0,
        width=0.2,
    )

    manager = plot_signal(
        signal,
        title="Rectangle Pulse"
    )

    manager.grid()

    manager.save(
        OUTPUT_DIR / "rectangle_signal.png"
    )

    export_signal_csv(
        signal,
        OUTPUT_DIR / "rectangle_signal.csv",
    )

    print("Experiment 01 Finished.")


if __name__ == "__main__":
    main()