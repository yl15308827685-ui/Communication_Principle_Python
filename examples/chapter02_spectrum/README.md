# 第二章 频谱分析实验

## 《通信原理（Python版）》配套实验

---

# 一、章节简介

第二章主要介绍通信信号的频域分析方法。

通过快速傅里叶变换（FFT），可以将时域信号转换到频域，从而分析信号的频率组成、幅度特性、相位特性以及功率分布。

本章所有实验均基于 **Communication Principle Python** 平台完成，重点掌握 FFT 的工程应用。

---

# 二、实验目标

完成本章实验后，应能够掌握：

- FFT 基本原理
- 时域与频域的关系
- 单边频谱与双边频谱
- 幅度谱分析
- 相位谱分析
- 功率谱分析
- FFT 点数对频谱的影响
- 采样率与频率分辨率
- 频谱泄漏
- 零填充
- FFT 在通信工程中的应用

---

# 三、实验目录

| 实验编号 | 实验名称 | 对应教材 |
|----------|----------|----------|
| Exp01 | FFT 基本频谱分析 | 2.2 |
| Exp02 | 幅度谱分析 | 2.3 |
| Exp03 | 相位谱分析 | 2.3 |
| Exp04 | 单边与双边频谱 | 2.4 |
| Exp05 | FFT 点数分析 | 2.5 |
| Exp06 | 采样率与频率分辨率 | 2.6 |
| Exp07 | 功率谱分析 | 2.7 |
| Exp08 | dB 频谱分析 | 2.8 |
| Exp09 | FFT Shift | 2.9 |
| Exp10 | FFT 综合实验 | 2.10 |

---

# 四、目录结构

```text
examples/
└── chapter02_spectrum/
    ├── README.md
    ├── exp01_fft_basic.py
    ├── exp02_amplitude_spectrum.py
    ├── exp03_phase_spectrum.py
    ├── exp04_single_double_spectrum.py
    ├── exp05_fft_points.py
    ├── exp06_frequency_resolution.py
    ├── exp07_power_spectrum.py
    ├── exp08_db_spectrum.py
    ├── exp09_fftshift.py
    └── exp10_fft_summary.py
```

---

# 五、运行方法

进入项目根目录：

```bash
python examples/chapter02_spectrum/exp01_fft_basic.py
```

或

```bash
python examples/chapter02_spectrum/exp05_fft_points.py
```

每个实验均可独立运行。

---

# 六、实验输出

统一输出目录：

```text
output/
└── chapter02/
```

例如：

```text
output/
└── chapter02/
    └── exp01_fft_basic/
        ├── time_signal.png
        ├── spectrum.png
        ├── signal.csv
        ├── spectrum.csv
        └── report.json
```

---

# 七、统一实验流程

所有实验均遵循：

```text
ExperimentConfig
        │
        ▼
SignalGenerator
        │
        ▼
FFT
        │
        ▼
Spectrum Analysis
        │
        ▼
Plot Time Domain
        │
        ▼
Plot Spectrum
        │
        ▼
Export CSV
        │
        ▼
Export JSON
```

---

# 八、本章涉及 API

本章主要使用以下接口：

## Spectrum

```python
fft()

ifft()
```

## Spectrum Processing

```python
single_side()

double_side()

fftshift()

ifftshift()
```

## Spectrum Analysis

```python
amplitude_spectrum()

phase_spectrum()

power_spectrum()

normalize_spectrum()

to_db()

from_db()
```

## Statistics

```python
peak_frequency()

peak_magnitude()

frequency_resolution()

bandwidth()

nyquist_frequency()

dominant_component()
```

---

# 九、本章知识点

完成本章实验后，应能够理解：

- FFT 的工程意义
- 时域与频域之间的转换
- 单边频谱
- 双边频谱
- FFT 分辨率
- Nyquist 采样定理
- 频谱泄漏
- 功率谱
- 相位谱
- dB 频谱表示

这些知识是后续调制、解调、滤波以及数字通信的理论基础。

---

# 十、推荐实验顺序

```text
Exp01 FFT 基本分析
        ↓
Exp02 幅度谱
        ↓
Exp03 相位谱
        ↓
Exp04 单双边频谱
        ↓
Exp05 FFT 点数
        ↓
Exp06 频率分辨率
        ↓
Exp07 功率谱
        ↓
Exp08 dB 频谱
        ↓
Exp09 FFT Shift
        ↓
Exp10 综合实验
```

---

# 十一、本章学习成果

完成全部实验后，应能够：

- 熟练使用 FFT 分析通信信号；
- 理解采样率与频谱之间的关系；
- 掌握通信系统中频谱分析的基本方法；
- 能够利用 Python 独立完成频域分析实验；
- 为第三章《模拟调制》打下坚实基础。

---

# 十二、注意事项

1. 建议在项目根目录运行实验。
2. FFT 点数建议采用 2 的整数次幂（512、1024、2048、4096 等）。
3. 本章实验统一使用 `communication.spectrum` 模块完成频谱分析。
4. 实验输出目录自动创建，无需手动建立。
5. 所有实验均采用统一接口和统一输出格式。

---

**《通信原理（Python版）》**

**第二章 频谱分析实验**