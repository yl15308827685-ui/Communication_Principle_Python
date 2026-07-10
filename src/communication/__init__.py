"""
==========================================================
Communication_Principle_Python

Package:
    communication

Version:
    1.2.0

Description:
    通信原理教材公共库

Python:
    >=3.9

==========================================================
"""

__version__ = "1.2.0"

# ==========================================================
# Config
# ==========================================================

from .config import (
    ExperimentConfig,
    DEFAULT_CONFIG,
    PROJECT_ROOT,
    SRC_DIR,
    EXPERIMENT_DIR,
    OUTPUT_DIR,
    IMAGE_DIR,
    DATA_DIR,
    DOC_DIR,
    image_path,
    data_path,
    document_path,
)

# ==========================================================
# Models
# ==========================================================

from .models import (
    Signal,
    Spectrum,
    AnalysisResult,
    ExperimentResult,
    ResultTable,
    FigureInfo,
    SignalStatistics,
)

# ==========================================================
# Signals
# ==========================================================

from .signals import (
    SignalGenerator,
    copy_signal,
    normalize,
    normalize_rms,
    scale,
    shift,
    reverse,
    offset,
    add,
    multiply,
)

# ==========================================================
# Spectrum
# ==========================================================

from .spectrum import (
    SpectrumAnalyzer,
    fft,
    single_side,
    double_side,
    power_spectrum,
    to_db,
)

# ==========================================================
# Analysis
# ==========================================================

from .analysis import (
    SignalAnalyzer,
    analyze,
    compare,
    snr,
    psnr,
    rms,
)

# ==========================================================
# Plotting
# ==========================================================

from .plotting import (
    PlotStyle,
    FigureManager,
    plot_signal,
    plot_spectrum,
    plot_single_spectrum,
    plot_compare,
    plot_signal_and_spectrum,
    save_current_figure,
)

# ==========================================================
# Export
# ==========================================================

from .export import (
    Exporter,
    save_png,
    save_svg,
    save_pdf,
    save_signal,
    save_spectrum,
    save_csv,
    save_json,
)

# ==========================================================
# Utils
# ==========================================================

from .utils import (
    time_axis,
    frequency_axis,
    zero_padding,
    next_power_of_two,
    hann_window,
    hamming_window,
    blackman_window,
    hz_to_khz,
    hz_to_mhz,
    khz_to_hz,
    mhz_to_hz,
)

# ==========================================================
# Public API
# ==========================================================

__all__ = [

    # Config
    "ExperimentConfig",
    "DEFAULT_CONFIG",

    # Models
    "Signal",
    "Spectrum",
    "AnalysisResult",
    "ExperimentResult",
    "ResultTable",
    "FigureInfo",
    "SignalStatistics",

    # Generator
    "SignalGenerator",

    # FFT
    "SpectrumAnalyzer",
    "fft",
    "single_side",
    "double_side",
    "power_spectrum",

    # Analysis
    "SignalAnalyzer",
    "analyze",
    "compare",
    "snr",
    "psnr",
    "rms",

    # Plot
    "FigureManager",
    "PlotStyle",
    "plot_signal",
    "plot_spectrum",
    "plot_single_spectrum",
    "plot_compare",
    "plot_signal_and_spectrum",

    # Export
    "Exporter",
    "save_png",
    "save_svg",
    "save_pdf",
    "save_signal",
    "save_spectrum",
    "save_csv",
    "save_json",

    # Utils
    "time_axis",
    "frequency_axis",
    "zero_padding",
    "next_power_of_two",
    "hann_window",
    "hamming_window",
    "blackman_window",
]