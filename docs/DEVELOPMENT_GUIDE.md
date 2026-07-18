# Communication Principle Python 开发规范

> Version 1.0  
> 《通信原理（Python版）》配套工程开发规范

---

# 一、项目定位

Communication Principle Python 是《通信原理（Python版）》教材的配套工程。

本项目不是普通的 Python 示例工程，而是一套完整的教学平台，包括：

- 教材
- 实验
- Python源码
- API文档
- 实验数据
- PPT
- 教学资源

所有开发工作均围绕教材展开。

---

# 二、总体开发原则

整个工程遵循以下原则。

## 1、教材驱动

教材是唯一设计依据。

任何代码均应服务于教材，不允许脱离教材单独设计。

---

## 2、小节驱动

教材采用如下节奏：

```
教材小节

↓

对应实验

↓

运行测试

↓

完善文档

↓

进入下一小节
```

禁止：

```
先写完整章

↓

最后补实验
```

---

## 3、实验同步

教材每完成一个小节，

如果存在实验，

必须同步完成实验代码。

保持：

教材 == 实验

一一对应。

---

# 三、目录规范

工程目录保持如下结构：

```text
Communication_Principle_Python/

├── src/
│
├── examples/
│
├── docs/
│
├── tests/
│
├── output/
│
├── README.md
│
└── pyproject.toml
```

不得随意修改。

---

# 四、Examples规范

每章对应一个目录。

例如：

```text
examples/

chapter01_signal/

chapter02_spectrum/

chapter03_modulation/

chapter04_sampling/
```

以后章节依次增加。

---

# 五、实验命名规范

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

不得采用：

```
test.py

demo.py

example.py
```

等不规范命名。

---

# 六、输出目录规范

统一采用：

```text
output/

chapter01/

chapter02/

chapter03/
```

每个实验对应一个目录。

例如：

```text
output/

chapter01/

exp01_generate_rectangle/
```

不得混放。

---

# 七、统一API规范

实验统一调用：

## 参数

```python
ExperimentConfig
```

---

## 信号产生

```python
SignalGenerator(config)
```

---

## 输出路径

```python
experiment_output_dir()
```

---

## 波形绘制

```python
plot_signal()
```

或

```python
plot_compare()
```

---

## 数据导出

```python
export_signal_csv()
```

---

禁止直接调用：

```
matplotlib

numpy.savetxt()

csv.writer()
```

实验应统一通过平台API完成。

---

# 八、绘图规范

所有实验保持统一风格。

标题：

```
Title Case
```

例如：

```
Signal Time Shift

Signal Addition

Frequency Spectrum
```

图例统一：

```
Original Signal

Scaled Signal

Shifted Signal

Reversed Signal

Added Signal
```

Grid：

全部开启。

---

# 九、实验输出规范

每个实验至少输出：

```
PNG

CSV
```

第二章开始增加：

```
FFT

Spectrum

Statistics
```

第三章开始增加：

```
Constellation

Eye Diagram

BER
```

后续章节依次扩展。

---

# 十、实验模板

所有实验统一结构。

```text
ExperimentConfig

↓

SignalGenerator

↓

Signal Processing

↓

Plot

↓

Export CSV

↓

Save Figure
```

保持一致。

---

# 十一、代码风格

统一遵循：

PEP8

Python 3.9+

统一类型注解：

```python
def main() -> None:
```

统一 Docstring。

统一 UTF-8 编码。

---

# 十二、测试规范

每增加一个模块：

必须同步增加：

pytest

测试。

保证：

```
pytest

全部通过
```

以后不得出现：

```
代码未测试
```

情况。

---

# 十三、文档规范

每章至少包含：

```
README.md
```

docs目录统一维护：

```
API_REFERENCE.md

USER_GUIDE.md

DEVELOPMENT_GUIDE.md

CHANGELOG.md
```

后续增加：

```
EXPERIMENT_GUIDE.md
```

---

# 十四、版本规范

建议采用：

```
v1.0

v1.1

v1.2
```

功能更新：

Minor

接口变化：

Major

Bug修复：

Patch

---

# 十五、Git提交规范

统一采用：

```
feat(ch1):

feat(ch2):

fix(signal):

docs(ch1):

refactor(signal):
```

便于版本管理。

---

# 十六、最终目标

最终形成完整教学资源。

包括：

✅ 教材

✅ 配套源码

✅ 全部实验

✅ API文档

✅ 教学PPT

✅ DOCX出版稿

✅ 习题答案

✅ Python实验平台

构建完整的《通信原理（Python版）》课程体系。

---

**Communication Principle Python**

**Development Guide**