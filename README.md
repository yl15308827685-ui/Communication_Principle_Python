# Communication_Principle_Python

> A Python SDK for Communication Principle experiments, signal processing, spectrum analysis, and educational demonstrations.

---

## Overview

Communication_Principle_Python is an educational Python SDK designed for communication engineering courses.

It provides reusable implementations of common communication signal processing algorithms and visualization tools for teaching, laboratory experiments, and research.

The project is written entirely in Python 3.9+ and follows modern Python package standards.

---

## Features

### Signal Generation

- Sine Wave
- Cosine Wave
- Square Wave
- Rectangular Pulse
- Impulse Signal
- Step Signal

### Signal Processing

- FFT
- FFT Shift
- Single-side Spectrum
- Double-side Spectrum
- Power Spectrum
- Signal Normalization
- RMS Normalization

### Signal Analysis

- RMS
- Peak Value
- Energy
- Power
- Mean
- Variance
- Standard Deviation
- SNR
- PSNR

### Visualization

- Signal Plot
- Spectrum Plot
- Comparison Plot
- Publication-quality Figures

### Export

- Images
- Experimental Results
- Tables

---

## Project Structure

```text
Communication_Principle_Python
│
├── src/
│   └── communication/
│       ├── __init__.py
│       ├── analysis.py
│       ├── config.py
│       ├── generator.py
│       ├── models.py
│       ├── plotting.py
│       ├── spectrum.py
│       └── ...
│
├── tests/
│
├── docs/
│
├── data/
│
├── experiments/
│
├── output/
│
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yl15308827685-ui/Communication_Principle_Python.git
```

Enter the project

```bash
cd Communication_Principle_Python
```

Install

```bash
pip install -e .
```

Or

```bash
pip install -r requirements.txt
```

---

## Quick Start

```python
from communication import SignalGenerator

generator = SignalGenerator()

signal = generator.sine()

print(signal)
```

Output

```text
Signal(samples=200, fs=10000.000 Hz)
```

---

## FFT Example

```python
from communication import SignalGenerator
from communication import fft

generator = SignalGenerator()

signal = generator.sine()

spectrum = fft(signal)

print(spectrum.peak_frequency)
```

---

## Running Tests

Run all tests

```bash
pytest
```

Current status

```text
19 Passed
```

---

## Development Environment

- Python 3.9+
- NumPy
- Matplotlib
- PyTest
- PyCharm

---

## Roadmap

Current Version

- Signal Generator
- Spectrum Analyzer
- Signal Analyzer
- Plotting Module
- Unit Tests

Planned Features

- Digital Modulation
- Analog Modulation
- Channel Coding
- Error Control Coding
- Filter Design
- Eye Diagram
- Constellation Diagram
- BER Simulation
- Digital Communication System
- GUI Laboratory

---

## Documentation

Project documentation will be continuously improved in the `docs` directory.

---

## Contributing

Issues and Pull Requests are welcome.

Please make sure all tests pass before submitting changes.

---

## License

This project is released under the MIT License.

---

## Author

Communication_Principle_Python Development Team

GitHub

https://github.com/yl15308827685-ui/Communication_Principle_Python