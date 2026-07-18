# Communication Principle Python 实验编写规范

> Version 1.0  
> 《通信原理（Python版）》实验开发规范

---

# 一、目的

本规范用于统一《通信原理（Python版）》所有实验的开发方式。

所有章节实验均应遵循本规范。

实验包括：

- 第一章 信号基础
- 第二章 频谱分析
- 第三章 调制技术
- 第四章 采样理论
- 第五章 数字基带传输
- 第六章 数字调制
- 第七章 信道
- 第八章 编码
- 第九章 同步
- 第十章 综合实验

保证整个工程具有统一风格。

---

# 二、实验目录

每章建立独立目录。

例如：

```text
examples/

chapter01_signal/

chapter02_spectrum/

chapter03_modulation/

chapter04_sampling/
```

不得跨章节存放。

---

# 三、实验命名规范

统一采用：

```text
expXX_xxxxx.py
```

例如：

```text
exp01_generate_rectangle.py

exp02_generate_cosine.py

exp03_generate_sine.py
```

禁止：

```
demo.py

example.py

test.py

hello.py
```

---

# 四、实验编号规则

每章重新编号。

例如：

第一章

```
Exp01

Exp02

…

Exp10
```

第二章

```
Exp01

Exp02

…

Exp08
```

编号仅在章节内唯一。

---

# 五、实验模板

所有实验统一采用如下结构：

```python
"""
Experiment XX
====================

Experiment Name

Chapter X

Communication Principle Python
"""

from communication.config import ExperimentConfig
from communication.signals import SignalGenerator
from communication.plotting import plot_signal
from communication.export import export_signal_csv
from communication.paths import experiment_output_dir
```

保持一致。

---

# 六、统一流程

所有实验必须遵循：

```text
ExperimentConfig

↓

SignalGenerator

↓

Signal Processing

↓

Visualization

↓

Export CSV

↓

Save Figure
```

不得跳过。

---

# 七、ExperimentConfig

实验参数统一放入：

```python
config = ExperimentConfig(...)
```

禁止：

```python
generator.sine(
    amplitude=1,
    frequency=100
)
```

统一由 Config 管理。

---

# 八、输出目录

统一采用：

```python
output_dir = experiment_output_dir(
    chapter=1,
    experiment="exp01_generate_rectangle",
)
```

禁止：

```
output/

temp/

desktop/
```

等硬编码路径。

---

# 九、图片输出

统一输出：

PNG

命名规范：

```text
rectangle_signal.png

cosine_signal.png

fft_spectrum.png

eye_diagram.png
```

统一使用小写。

---

# 十、CSV输出

统一采用：

```python
export_signal_csv(...)
```

命名：

```text
rectangle_signal.csv

cosine_signal.csv

fft.csv
```

---

# 十一、绘图规范

统一使用：

```python
plot_signal()
```

或者：

```python
plot_compare()
```

禁止直接调用 matplotlib。

---

# 十二、图标题规范

统一采用英文。

例如：

```
Rectangle Signal

Cosine Signal

Signal Addition

FFT Spectrum

Eye Diagram
```

采用 Title Case。

---

# 十三、图例规范

统一采用：

```
Original Signal

Scaled Signal

Shifted Signal

Reversed Signal

Processed Signal

FFT Spectrum
```

保持一致。

---

# 十四、Grid

全部开启：

```python
manager.grid()
```

保持统一。

---

# 十五、字体

统一采用 plotting.py 默认字体。

实验不得单独修改字体。

---

# 十六、图片尺寸

统一由：

```
ExperimentConfig
```

控制。

禁止：

```
plt.figure(figsize=...)
```

---

# 十七、实验输出

第一章：

```
PNG

CSV
```

第二章：

```
PNG

CSV

FFT
```

第三章：

```
Constellation

Spectrum

Eye Diagram
```

以后章节逐步增加。

---

# 十八、异常处理

实验代码尽量保持简洁。

异常处理放到底层模块。

实验脚本只负责：

```
调用

展示

保存
```

---

# 十九、教材同步

原则：

一个教材小节

↓

一个实验

↓

一个README

↓

一个测试

↓

进入下一小节

禁止：

```
教材全部完成

最后补实验
```

---

# 二十、测试要求

每个实验必须：

能够独立运行。

输出：

```
PNG

CSV
```

无异常退出。

---

# 二十一、最终目标

最终形成：

```
教材

↓

实验

↓

源码

↓

API

↓

PPT

↓

DOCX

↓

习题

↓

教学资源
```

形成完整的《通信原理（Python版）》教学平台。

---

**Communication Principle Python**

**Experiment Guide**