# Communication_Principle_Python
# API Reference
Version: v1.0 (API Freeze)

---

# 1. 项目简介

Communication_Principle_Python 是《通信原理（Python版）》配套教学库。

本库用于：

- 通信原理教学
- 信号生成
- 信号分析
- 频谱分析
- 数据导出
- 可视化绘图
- 教材实验

自 v1.0 起，API 正式冻结（API Freeze）。

后续版本：

- 允许增加新功能；
- 允许修复 Bug；
- 不再修改已有函数名称、参数名称及返回类型。

---

# 2. 包结构

src/
└── communication/
    ├── __init__.py
    ├── config.py
    ├── models.py
    ├── signals.py
    ├── spectrum.py
    ├── analysis.py
    ├── plotting.py
    ├── export.py
    └── utils.py

---

# 3. config

## ExperimentConfig

实验参数配置对象。

用于统一实验配置。

示例：

config = ExperimentConfig(...)

---

# 4. models

## Signal

时域信号对象。

包含：

- time
- data
- sampling_frequency
- metadata

支持：

copy()

---

## Spectrum

频谱对象。

包含：

- frequency
- magnitude
- phase
- complex

支持：

copy()

---

## Statistics

统计分析对象。

包含：

- mean
- rms
- variance
- standard_deviation
- peak
- minimum
- maximum
- energy
- average_power

---

# 5. signals

## SignalGenerator

信号发生器。

创建方式：

generator = SignalGenerator(config)

---

## rectangle()

生成矩形脉冲。

Signature

rectangle(
    amplitude=None,
    width=None
)

返回：

Signal

---

## sine()

生成正弦信号。

Signature

sine(
    ...
)

返回：

Signal

---

## cosine()

生成余弦信号。

Signature

cosine(
    ...
)

返回：

Signal

---

## step()

生成阶跃信号。

Signature

step(
    ...
)

返回：

Signal

---

## impulse()

生成冲激信号。

Signature

impulse(
    ...
)

返回：

Signal

---

# 信号处理函数

normalize()

normalize_rms()

copy_signal()

scale()

offset()

shift()

reverse()

add()

multiply()

---

# 6. spectrum

FFT 相关算法。

包括：

fft()

ifft()

fftshift()

ifftshift()

frequency_axis()

frequency_resolution()

nyquist_frequency()

single_side()

double_side()

to_db()

from_db()

peak_frequency()

peak_magnitude()

bandwidth()

spectrum_energy()

spectrum_power()

---

# 7. analysis

统计分析模块。

包括：

mean()

maximum()

minimum()

variance()

standard_deviation()

rms()

energy()

average_power()

peak_to_peak()

crest_factor()

mae()

mse()

rmse()

correlation()

auto_correlation()

cross_correlation()

analyze()

SignalAnalyzer

---

# 8. plotting

绘图模块。

## plot_signal()

Signature

plot_signal(
    signal,
    *,
    title=None,
    xlabel="Time (s)",
    ylabel="Amplitude",
    label=None,
    style=None
)

返回：

FigureManager

---

## plot_spectrum()

绘制频谱。

返回：

FigureManager

---

## plot_single_spectrum()

绘制单边频谱。

---

## plot_compare()

多信号比较。

---

## plot_signal_and_spectrum()

同时绘制：

- 时域
- 频域

---

## FigureManager

统一图形管理对象。

主要功能：

clear()

grid()

title()

label()

save()

---

# 9. export

导出模块。

---

## export_signal_csv()

Signature

export_signal_csv(
    signal,
    filename
)

---

## export_spectrum_csv()

导出频谱。

---

## export_statistics_csv()

导出统计结果。

---

## save_figure()

保存当前图片。

---

## Exporter

统一导出对象。

支持：

export_signal()

export_spectrum()

export_statistics()

save_figure()

---

# 10. utils

公共工具模块。

包括：

数学工具

数组工具

单位转换

辅助函数

---

# 11. API Freeze Policy

Communication_Principle_Python v1.0

冻结以下内容：

✔ 函数名称

✔ 参数名称

✔ 返回对象类型

✔ 数据模型

允许：

✔ 新增函数

✔ 新增类

✔ 修复 Bug

✔ 优化性能

禁止：

✘ 修改已有 API

✘ 删除已有 API

✘ 修改参数名称

---

# 12. 教材对应关系

Chapter 1

signals.py

plotting.py

export.py

---

Chapter 2

signals.py

spectrum.py

analysis.py

---

Chapter 3

spectrum.py

analysis.py

---

Chapter 4+

全部模块联合使用。

---

# End

3. SignalGenerator

SignalGenerator 用于产生教材中的各种标准信号。

3. SignalGenerator

SignalGenerator 用于产生教材中的各种标准信号。

rectangle()

产生矩形脉冲。

rectangle()

产生矩形脉冲。

signal = generator.rectangle(
    amplitude=1.0,
    width=0.2
)

参数：

参数	类型	默认
amplitude	float	config.DEFAULT_AMPLITUDE
width	float	config.DEFAULT_WIDTH

返回：
sine()

产生正弦波。

signal = generator.sine(
    amplitude=1,
    frequency=10,
    phase=0
)

| 参数        | 类型         |
| --------- | ---------- |
| amplitude | float      |
| frequency | float      |
| phase     | float(rad) |

cosine()

产生余弦波。

signal = generator.cosine(
    amplitude=1,
    frequency=10,
    phase=0
)

impulse()

单位冲激。

signal = generator.impulse()

step()

单位阶跃。

signal = generator.step()

4. signals 模块

除 SignalGenerator 外，还提供信号处理函数。

normalize()

signal2 = normalize(signal)

最大值归一化。

normalize_rms()

signal2 = normalize_rms(signal)

RMS归一化。

scale()

signal2 = scale(signal,2)

放大。

offset()
signal2 = offset(signal,1)
加直流。

shift()

signal2 = shift(signal,0.2)
时间平移。

reverse()
signal2 = reverse(signal)
时间反转。

add()
signal3 = add(signal1,signal2)
信号相加。

multiply()
signal3 = multiply(signal1,signal2)
信号相乘。

copy_signal()
signal2 = copy_signal(signal)
深拷贝。

5. spectrum 模块
fft()

傅里叶变换。
fft()

spec = fft(signal)
返回
Spectrum

ifft()
傅里叶反变换
signal = ifft(spec)

fftshift()
中心频谱。

spec = fftshift(spec)

ifftshift()
spec = ifftshift(spec)

frequency_axis()

生成频率轴。

frequency_resolution()

频率分辨率。

nyquist_frequency()

奈奎斯特频率。

single_side()

单边谱。

double_side()

双边谱。

to_db()

dB转换。

from_db()

恢复线性值。

peak_frequency()

峰值频率。

peak_magnitude()

峰值幅值。

bandwidth()

计算带宽。

spectrum_energy()

计算频谱能量。

spectrum_power()

计算频谱平均功率。

# 6. plotting 模块

plotting 模块负责教材中的全部绘图功能。

所有绘图均基于 matplotlib 实现，并统一返回 FigureManager 对象。

---

## PlotStyle

绘图样式对象。

可统一设置：

- 图像大小
- DPI
- 网格
- 字体
- 颜色
- 线宽

示例：

style = PlotStyle()

---

## plot_signal()

绘制时域波形。

Signature

plot_signal(
    signal,
    *,
    title=None,
    xlabel="Time (s)",
    ylabel="Amplitude",
    label=None,
    style=None
)

参数

signal

Signal对象。

title

图标题。

xlabel

横坐标标题。

ylabel

纵坐标标题。

label

图例。

style

PlotStyle对象。

返回

FigureManager

示例

manager = plot_signal(signal)

manager.grid()

manager.save("signal.png")

---

## plot_spectrum()

绘制双边频谱。

Signature

plot_spectrum(
    spectrum,
    *,
    title=None,
    style=None
)

返回

FigureManager

---

## plot_single_spectrum()

绘制单边频谱。

Signature

plot_single_spectrum(
    spectrum,
    *,
    title=None,
    style=None
)

返回

FigureManager

---

## plot_compare()

绘制多个信号比较图。

Signature

plot_compare(
    signals,
    *,
    labels=None,
    title=None,
    style=None
)

返回

FigureManager

---

## plot_signal_and_spectrum()

同时绘制

• 时域

• 频域

Signature

plot_signal_and_spectrum(
    signal,
    spectrum,
    *,
    style=None
)

返回

FigureManager

---

## save_current_figure()

保存当前 Figure。

Signature

save_current_figure(filename)

---

## FigureManager

FigureManager 为 plotting 模块统一图形控制对象。

创建方式

manager = plot_signal(signal)

支持以下方法：

clear()

grid()

title()

xlabel()

ylabel()

legend()

save()

close()

figure

axes

---

# 7. analysis 模块

analysis 模块用于教材中的统计分析。

包括：

## mean()

均值。

返回

float

---

## maximum()

最大值。

---

## minimum()

最小值。

---

## variance()

方差。

---

## standard_deviation()

标准差。

---

## rms()

均方根。

---

## peak_to_peak()

峰峰值。

---

## crest_factor()

峰值因子。

---

## energy()

信号能量。

---

## average_power()

平均功率。

---

## mae()

平均绝对误差。

---

## mse()

均方误差。

---

## rmse()

均方根误差。

---

## correlation()

相关系数。

---

## auto_correlation()

自相关函数。

---

## cross_correlation()

互相关函数。

---

## analyze()

一次计算全部统计量。

返回

Statistics

---

## SignalAnalyzer

分析器对象。

示例

analyzer = SignalAnalyzer()

result = analyzer.analyze(signal)

---

# 8. export 模块

export 模块负责教材实验的数据导出。

支持：

CSV

PNG

SVG

PDF（后续）

---

## export_signal_csv()

Signature

export_signal_csv(
    signal,
    filename
)

导出

Time

Amplitude

---

## export_spectrum_csv()

导出

Frequency

Magnitude

Phase

---

## export_statistics_csv()

导出

Statistics

---

## save_figure()

保存图片。

支持

PNG

JPG

SVG

---

## Exporter

统一导出对象。

支持：

export_signal()

export_spectrum()

export_statistics()

save_figure()


9 Examples（所有实验索引）

10 教材章节对应关系

11 数据模型 UML

12 API 生命周期

13 Version History

14 Compatibility

15 Coding Convention

16 FAQ

17 Change Log

18 Appendix

# 9. Examples（教材实验索引）

Communication_Principle_Python 的所有实验均位于 examples 目录，并按照教材章节组织。

```
examples/
├── chapter01_signal/
├── chapter02_sampling/
├── chapter03_fourier/
├── chapter04_modulation/
├── chapter05_baseband/
├── chapter06_channel/
├── chapter07_noise/
├── chapter08_analog_modulation/
├── chapter09_digital_modulation/
└── chapter10_system/
```

---

## Chapter 1 信号

| 实验 | 文件 | 对应教材 |
|------|------|----------|
| Exp01 | exp01_generate_rectangle.py | 矩形脉冲 |
| Exp02 | exp02_generate_cosine.py | 余弦信号 |
| Exp03 | exp03_generate_sine.py | 正弦信号 |
| Exp04 | exp04_generate_step.py | 阶跃信号 |
| Exp05 | exp05_generate_impulse.py | 单位冲激 |
| Exp06 | exp06_signal_add.py | 信号叠加 |
| Exp07 | exp07_signal_scale.py | 幅度缩放 |
| Exp08 | exp08_signal_shift.py | 时间平移 |
| Exp09 | exp09_signal_reverse.py | 时间反转 |
| Exp10 | exp10_signal_normalize.py | 信号归一化 |

---

## Chapter 2 采样与频谱

| 实验 | 文件 |
|------|------|
| Exp01 | exp01_sampling.py |
| Exp02 | exp02_aliasing.py |
| Exp03 | exp03_fft.py |
| Exp04 | exp04_fftshift.py |
| Exp05 | exp05_single_side.py |
| Exp06 | exp06_double_side.py |
| Exp07 | exp07_db.py |
| Exp08 | exp08_bandwidth.py |
| Exp09 | exp09_energy.py |
| Exp10 | exp10_power.py |

后续章节保持一致命名规范。

---

# 10. 数据模型（Data Model）

整个工程采用三个核心数据对象。

```
Signal
│
├── time
├── data
├── sampling_frequency
└── metadata
```

↓

```
Spectrum
│
├── frequency
├── magnitude
├── phase
├── complex
└── metadata
```

↓

```
Statistics
│
├── mean
├── rms
├── variance
├── std
├── energy
├── power
├── peak
└── crest_factor
```

所有 API 均围绕这三个对象进行计算，不直接操作裸 NumPy 数组。

---

# 11. API 生命周期

所有 API 遵循如下生命周期：

```
SignalGenerator
        │
        ▼
     Signal
        │
        ├────────► plotting
        │
        ├────────► analysis
        │
        ├────────► export
        │
        ▼
      fft()
        │
        ▼
    Spectrum
        │
        ├────────► plotting
        ├────────► export
        └────────► analysis
```

---

# 12. Version History

## v0.x

教材开发阶段。

API 不稳定。

---

## v1.0

教材正式版。

API Freeze。

完成：

- models
- signals
- spectrum
- analysis
- plotting
- export

对应教材：

第一章

第二章

---

## v1.1（规划）

新增：

- filter.py
- noise.py
- modulation.py

保持 v1.0 API 完全兼容。

---

# 13. Compatibility

Python

≥3.9

推荐：

Python 3.10+

---

依赖

NumPy

Matplotlib

pytest

---

操作系统

Windows

Linux

macOS

---

# 14. Coding Convention

整个项目统一采用：

PEP8

类型注解（Type Hint）

Google Docstring

UTF-8

4 空格缩进

snake_case

Class 使用 PascalCase

常量全部大写

---

# 15. Testing

所有公共 API 必须具备 pytest 测试。

当前测试覆盖模块：

- test_import.py
- test_models.py
- test_signal.py
- test_spectrum.py
- test_analysis.py
- test_plotting.py
- test_export.py

每新增一个公共函数，必须同步新增对应测试。

目标覆盖率：

> 95%+

---

# 16. FAQ

## Q1：examples 是否可以直接运行？

可以。

examples 中所有实验均设计为独立运行。

---

## Q2：examples 可以修改 API 吗？

不允许。

examples 必须严格调用公共 API。

---

## Q3：教材代码是否允许直接复制？

允许。

教材全部代码均基于 Communication_Principle_Python 官方 API。

---

## Q4：是否支持 Jupyter？

支持。

examples 可以直接迁移到 Notebook。

---

# 17. Change Log

v1.0

API 冻结。

统一 examples。

统一 plotting。

统一 export。

统一 Spectrum 数据模型。

统一 Statistics 数据模型。

---

# 18. 附录

项目主页：

Communication_Principle_Python

目录：

```
src/
tests/
examples/
docs/
textbook/
slides/
```

教材：

《通信原理（Python版）》

实验：

与教材章节一一对应。

API：

本手册为唯一官方参考文档。

---

End of API Reference
Version 1.0


