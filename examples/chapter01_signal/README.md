# 第一章 信号基础实验

## 《通信原理（Python版）》配套实验

---

# 一、章节简介

第一章主要介绍通信系统中最基本的连续时间信号。

本章实验围绕矩形脉冲、正弦信号、余弦信号、单位冲激、单位阶跃等典型信号展开，通过 Python 编程实现信号的生成、显示、处理与数据导出，使读者掌握通信信号最基本的分析方法。

本章所有实验均基于 **Communication Principle Python** 实验平台完成。

---

# 二、实验目标

完成本章实验后，应能够掌握以下内容：

- 理解通信信号的数学表示方法
- 掌握常见连续时间信号的产生方法
- 掌握通信信号的可视化方法
- 掌握通信信号数据导出方法
- 掌握信号的基本运算
- 为第二章频谱分析打下基础

---

# 三、实验目录

| 实验编号 | 实验名称 | 对应教材小节 |
|----------|----------|--------------|
| Exp01 | 矩形脉冲信号产生 | 1.2 |
| Exp02 | 余弦信号产生 | 1.3 |
| Exp03 | 正弦信号产生 | 1.3 |
| Exp04 | 单位冲激信号 | 1.4 |
| Exp05 | 单位阶跃信号 | 1.4 |
| Exp06 | 信号幅度缩放 | 1.5 |
| Exp07 | 信号时间平移 | 1.5 |
| Exp08 | 信号时间反转 | 1.5 |
| Exp09 | 信号相加 | 1.5 |
| Exp10 | 信号基本运算综合实验 | 1.6 |

---

# 四、目录结构

```text
examples/
└── chapter01_signal/
    ├── README.md
    ├── exp01_generate_rectangle.py
    ├── exp02_generate_cosine.py
    ├── exp03_generate_sine.py
    ├── exp04_generate_impulse.py
    ├── exp05_generate_step.py
    ├── exp06_signal_scaling.py
    ├── exp07_signal_shift.py
    ├── exp08_signal_reverse.py
    ├── exp09_signal_addition.py
    └── exp10_signal_operations.py
```

---

# 五、实验运行方法

进入工程根目录后，直接运行对应实验即可。

例如：

```bash
python examples/chapter01_signal/exp01_generate_rectangle.py
```

或者

```bash
python examples/chapter01_signal/exp07_signal_shift.py
```

每个实验均可独立运行，互不依赖。

---

# 六、实验结果输出

所有实验结果统一保存在：

```text
output/
└── chapter01/
```

例如：

```text
output/
└── chapter01/
    └── exp01_generate_rectangle/
        ├── rectangle_signal.png
        └── rectangle_signal.csv
```

每个实验通常输出以下内容：

- 波形图片（PNG）
- 信号数据（CSV）

---

# 七、实验平台组成

本章实验依赖 Communication Principle Python 平台。

```text
communication
├── config.py          实验参数配置
├── paths.py           输出路径管理
├── signals.py         信号产生与处理
├── spectrum.py        频谱分析
├── analysis.py        信号分析
├── plotting.py        图形绘制
├── export.py          数据导出
├── models.py          数据模型
└── utils.py           工具函数
```

---

# 八、实验流程

所有实验均遵循统一流程。

```text
实验参数配置
        │
        ▼
信号产生
        │
        ▼
信号处理
        │
        ▼
波形绘制
        │
        ▼
CSV数据导出
        │
        ▼
实验结果保存
```

---

# 九、本章知识点

本章实验对应教材以下知识：

- 连续时间信号
- 时间轴
- 幅值
- 正弦信号
- 余弦信号
- 矩形脉冲
- 单位冲激
- 单位阶跃
- 幅度变换
- 时间平移
- 时间反转
- 信号叠加

这些内容构成了后续频谱分析、调制解调等章节的重要基础。

---

# 十、推荐实验顺序

建议严格按照教材顺序完成实验。

```text
Exp01  矩形脉冲
      ↓
Exp02  余弦信号
      ↓
Exp03  正弦信号
      ↓
Exp04  单位冲激
      ↓
Exp05  单位阶跃
      ↓
Exp06  幅度缩放
      ↓
Exp07  时间平移
      ↓
Exp08  时间反转
      ↓
Exp09  信号相加
      ↓
Exp10  综合实验
```

---

# 十一、本章学习成果

完成第一章全部实验后，应能够：

- 独立生成通信中的基本信号；
- 掌握通信信号的基本运算方法；
- 使用 Python 对通信信号进行可视化分析；
- 导出实验数据并进行进一步处理；
- 为第二章《频谱分析》实验做好准备。

---

# 十二、注意事项

1. 建议在项目根目录下运行实验程序。
2. 所有实验均基于 Python 3.9 及以上版本开发。
3. 实验输出目录会自动创建，无需手动建立。
4. 如需修改实验参数，请优先修改 `ExperimentConfig`，保持实验代码统一规范。
5. 本章所有实验均采用统一的工程接口，请勿直接修改底层库函数，建议通过实验脚本完成验证。

---

**《通信原理（Python版）》**

**第一章 信号基础实验**