# Communication_Principle_Python

> 《通信原理（Python版）》配套实验源码工程

---

## 项目简介

Communication_Principle_Python 是配套《通信原理（Python版）》教材开发的实验源码工程。

本工程采用 Python 语言实现通信原理课程中的主要理论、算法与实验，覆盖信号分析、傅里叶变换、频谱分析、调制解调、随机过程、数字基带传输、数字调制等内容。

工程目标如下：

- 为教材提供完整的实验源码；
- 为课堂教学提供可运行的演示程序；
- 为学生提供课后实验平台；
- 为教师提供可扩展的教学案例；
- 为通信算法学习提供统一代码框架。

---

# 工程特点

本工程具有以下特点：

- 模块化设计
- 面向对象实现
- 完整中文注释
- 与教材章节一一对应
- 实验代码可直接运行
- 支持图片自动保存
- 支持实验数据自动导出
- 支持 Windows、Linux、macOS

---

# 推荐运行环境

Python

```text
Python ≥ 3.10
```

推荐 IDE

- PyCharm Professional
- PyCharm Community
- Visual Studio Code

---

# 安装依赖

安装 requirements.txt 中的全部依赖：

```bash
pip install -r requirements.txt
```

---

# 工程目录

```text
Communication_Principle_Python
│
├── README.md
├── requirements.txt
│
├── src
│   └── communication
│       ├── config.py
│       ├── plotting.py
│       ├── signals.py
│       ├── spectrum.py
│       ├── analysis.py
│       ├── export.py
│       ├── utils.py
│       └── __init__.py
│
├── experiments
│   ├── chapter02
│   ├── chapter03
│   ├── chapter04
│   ├── chapter05
│   └── ...
│
├── images
│
├── data
│
└── docs
```

---

# 已完成内容

## 第一章

- 通信系统概述
- 信号分类
- 信号模型

## 第二章（开发中）

- 周期信号
- 傅里叶级数
- 傅里叶变换
- FFT 实验
- 理论频谱验证

---

# 后续计划

第三章

- 模拟调制

第四章

- 随机过程

第五章

- 模拟信道

第六章

- 数字基带传输

第七章

- 数字调制

第八章

- 差错控制编码

……

---

# 许可证

本工程仅作为《通信原理（Python版）》教材配套源码使用。

版权所有 © 作者保留所有权利。

---

# 联系方式

本工程将随着教材持续更新。