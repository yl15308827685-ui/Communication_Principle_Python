"""
=============================================================
Communication_Principle_Python

File:
    plotting.py

Version:
    2.1.0

Description:
    Unified plotting module.

Python:
    >=3.9
=============================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional
from typing import Tuple

import matplotlib.pyplot as plt

from matplotlib.axes import Axes
from matplotlib.figure import Figure

from .models import Signal
from .models import Spectrum
from .config import image_path


# ==========================================================
# Plot Style
# ==========================================================

@dataclass
class PlotStyle:
    """
    Global plotting style.
    """

    # Figure
    figsize: Tuple[float, float] = (10.0, 4.0)
    dpi: int = 300
    facecolor: str = "white"

    # Line
    linewidth: float = 2.0
    linestyle: str = "-"
    color: str = "C0"
    alpha: float = 1.0

    # Marker
    marker: Optional[str] = None
    markersize: float = 5.0

    # Font
    title_size: int = 16
    label_size: int = 12
    tick_size: int = 10

    # Grid
    grid: bool = True
    grid_alpha: float = 0.35

    # Legend
    legend: bool = True
    legend_fontsize: int = 10

    # Layout
    tight_layout: bool = True

    # Save
    save_dpi: int = 300
    transparent: bool = False
    bbox_inches: str = "tight"
    pad_inches: float = 0.10


# ==========================================================
# Figure Manager
# ==========================================================

class FigureManager:
    """
    Wrapper of matplotlib Figure and Axes.
    """

    def __init__(
        self,
        figure: Figure,
        axes: Axes,
    ):

        self.figure = figure
        self.axes = axes

    # ------------------------------------------------------
    # Alias
    # ------------------------------------------------------

    @property
    def fig(self) -> Figure:
        return self.figure

    @property
    def ax(self) -> Axes:
        return self.axes

    # ------------------------------------------------------
    # Display
    # ------------------------------------------------------

    def show(self) -> None:
        plt.show()

    def close(self) -> None:
        plt.close(self.figure)

    def clear(self) -> None:
        self.axes.cla()

    # ------------------------------------------------------
    # Save
    # ------------------------------------------------------

    def save(
        self,
        filename: str,
        dpi: int = 300,
    ) -> Path:
        """
        Save current figure.
        """

        path = Path(filename)

        if not path.is_absolute():
            path = Path.cwd() / path

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.figure.savefig(
            path,
            dpi=dpi,
            bbox_inches="tight",
        )

        return path

    # ------------------------------------------------------
    # Figure Setting
    # ------------------------------------------------------

    def grid(
        self,
        enable: bool = True,
    ) -> None:

        self.axes.grid(enable)

    def tight_layout(self) -> None:

        self.figure.tight_layout()

    def set_title(
        self,
        title: str,
    ) -> None:

        self.axes.set_title(title)

    def set_xlabel(
        self,
        label: str,
    ) -> None:

        self.axes.set_xlabel(label)

    def set_ylabel(
        self,
        label: str,
    ) -> None:

        self.axes.set_ylabel(label)

    def set_xlim(
        self,
        left: float,
        right: float,
    ) -> None:

        self.axes.set_xlim(left, right)

    def set_ylim(
        self,
        bottom: float,
        top: float,
    ) -> None:

        self.axes.set_ylim(bottom, top)

    # ------------------------------------------------------
    # Access
    # ------------------------------------------------------

    def get_figure(self) -> Figure:

        return self.figure

    def get_axes(self) -> Axes:

        return self.axes

    # ------------------------------------------------------

    def __repr__(self) -> str:

        return (
            f"FigureManager("
            f"figure={self.figure!r}, "
            f"axes={self.axes!r})"
        )




# ==========================================================
# Internal Figure Utilities
# ==========================================================

DEFAULT_STYLE = PlotStyle()


def _create_manager(
    style: Optional[PlotStyle] = None,
) -> FigureManager:
    """
    Create a FigureManager.

    Parameters
    ----------
    style
        Plot style.

    Returns
    -------
    FigureManager
    """

    if style is None:
        style = DEFAULT_STYLE

    figure, axes = plt.subplots(
        figsize=style.figsize,
        dpi=style.dpi,
        facecolor=style.facecolor,
    )

    return FigureManager(
        figure=figure,
        axes=axes,
    )


# ==========================================================
# Apply Style
# ==========================================================

def _apply_style(
    manager: FigureManager,
    style: PlotStyle,
) -> None:
    """
    Apply plotting style.
    """

    ax = manager.ax

    ax.tick_params(
        axis="both",
        labelsize=style.tick_size,
    )

    if style.grid:

        ax.grid(
            True,
            alpha=style.grid_alpha,
        )

    if style.legend:

        handles, labels = ax.get_legend_handles_labels()

        if handles:

            ax.legend(
                fontsize=style.legend_fontsize,
            )


# ==========================================================
# Finalize Figure
# ==========================================================

def _finalize(
    manager: FigureManager,
    style: PlotStyle,
) -> FigureManager:
    """
    Finalize figure before returning.
    """

    _apply_style(
        manager,
        style,
    )

    if style.tight_layout:

        manager.tight_layout()

    return manager

# ==========================================================
# Internal Drawing
# ==========================================================

def _draw_signal(
    manager: FigureManager,
    signal: Signal,
    *,
    title: Optional[str] = None,
    xlabel: str = "Time (s)",
    ylabel: str = "Amplitude",
    label: Optional[str] = None,
    style: Optional[PlotStyle] = None,
) -> None:
    """
    Draw a time-domain signal.

    Parameters
    ----------
    manager
        Figure manager.

    signal
        Signal object.

    title
        Figure title.

    xlabel
        X-axis label.

    ylabel
        Y-axis label.

    label
        Legend label.

    style
        Plot style.
    """

    if style is None:
        style = DEFAULT_STYLE

    ax = manager.ax

    ax.plot(
        signal.time,
        signal.value,
        linewidth=style.linewidth,
        linestyle=style.linestyle,
        color=style.color,
        alpha=style.alpha,
        marker=style.marker,
        markersize=style.markersize,
        label=label,
    )

    if title is None:
        title = signal.name

    ax.set_title(
        title,
        fontsize=style.title_size,
    )

    ax.set_xlabel(
        xlabel,
        fontsize=style.label_size,
    )

    ax.set_ylabel(
        ylabel,
        fontsize=style.label_size,
    )


# ==========================================================
# Public API
# ==========================================================

def plot_signal(
    signal: Signal,
    *,
    title: Optional[str] = None,
    xlabel: str = "Time (s)",
    ylabel: str = "Amplitude",
    label: Optional[str] = None,
    style: Optional[PlotStyle] = None,
) -> FigureManager:
    """
    Plot a time-domain signal.

    Parameters
    ----------
    signal
        Signal object.

    title
        Figure title.

    xlabel
        X-axis label.

    ylabel
        Y-axis label.

    label
        Legend label.

    style
        Plot style.

    Returns
    -------
    FigureManager
    """

    if style is None:
        style = DEFAULT_STYLE

    manager = _create_manager(style)

    _draw_signal(
        manager=manager,
        signal=signal,
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
        label=label,
        style=style,
    )

    return _finalize(
        manager,
        style,
    )

# ==========================================================
# Compare Signals
# ==========================================================

def plot_compare(
    signal1: Signal,
    signal2: Signal,
    *,
    title: str = "Signal Comparison",
    xlabel: str = "Time (s)",
    ylabel: str = "Amplitude",
    label1: Optional[str] = None,
    label2: Optional[str] = None,
    style: Optional[PlotStyle] = None,
) -> FigureManager:
    """
    Plot two signals for comparison.

    Parameters
    ----------
    signal1
        First signal.

    signal2
        Second signal.

    title
        Figure title.

    xlabel
        X-axis label.

    ylabel
        Y-axis label.

    label1
        Legend of first signal.

    label2
        Legend of second signal.

    style
        Plot style.

    Returns
    -------
    FigureManager
    """

    if style is None:
        style = DEFAULT_STYLE

    manager = _create_manager(style)

    ax = manager.ax

    if label1 is None:
        label1 = signal1.name

    if label2 is None:
        label2 = signal2.name

    ax.plot(
        signal1.time,
        signal1.value,
        linewidth=style.linewidth,
        linestyle="-",
        alpha=style.alpha,
        label=label1,
    )



    ax.plot(
        signal2.time,
        signal2.value,
        linewidth=style.linewidth,
        alpha=style.alpha,
        label=label2,
    )

    ax.set_title(
        title,
        fontsize=style.title_size,
    )

    ax.set_xlabel(
        xlabel,
        fontsize=style.label_size,
    )

    ax.set_ylabel(
        ylabel,
        fontsize=style.label_size,
    )

    return _finalize(
        manager,
        style,
    )



# ==========================================================
# Internal Spectrum Drawing
# ==========================================================

def _draw_spectrum(
    manager: FigureManager,
    spectrum: Spectrum,
    *,
    title: Optional[str] = None,
    xlabel: str = "Frequency (Hz)",
    ylabel: str = "Magnitude",
    label: Optional[str] = None,
    style: Optional[PlotStyle] = None,
) -> None:
    """
    Draw a frequency-domain spectrum.
    """

    if style is None:
        style = DEFAULT_STYLE

    ax = manager.ax

    ax.plot(
        spectrum.frequency,
        spectrum.magnitude,
        linewidth=style.linewidth,
        linestyle=style.linestyle,
        color=style.color,
        alpha=style.alpha,
        marker=style.marker,
        markersize=style.markersize,
        label=label,
    )

    if title is None:
        title = "Spectrum"

    ax.set_title(
        title,
        fontsize=style.title_size,
    )

    ax.set_xlabel(
        xlabel,
        fontsize=style.label_size,
    )

    ax.set_ylabel(
        ylabel,
        fontsize=style.label_size,
    )

# ==========================================================
# Plot Spectrum
# ==========================================================

def plot_spectrum(
    spectrum: Spectrum,
    *,
    title: Optional[str] = None,
    xlabel: str = "Frequency (Hz)",
    ylabel: str = "Magnitude",
    label: Optional[str] = None,
    style: Optional[PlotStyle] = None,
) -> FigureManager:
    """
    Plot frequency-domain spectrum.
    """

    if style is None:
        style = DEFAULT_STYLE

    manager = _create_manager(style)

    _draw_spectrum(
        manager=manager,
        spectrum=spectrum,
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
        label=label,
        style=style,
    )

    return _finalize(
        manager,
        style,
    )


# ==========================================================
# Alias
# ==========================================================

def plot_single_spectrum(
    spectrum: Spectrum,
    **kwargs,
) -> FigureManager:
    """
    Alias of plot_spectrum().
    """

    return plot_spectrum(
        spectrum,
        **kwargs,
    )

# ==========================================================
# Plot Signal And Spectrum
# ==========================================================

def plot_signal_and_spectrum(
    signal: Signal,
    spectrum: Spectrum,
    *,
    signal_title: str = "Time Domain",
    spectrum_title: str = "Frequency Domain",
    style: Optional[PlotStyle] = None,
) -> FigureManager:
    """
    Plot signal and spectrum in one figure.

    Parameters
    ----------
    signal
        Time-domain signal.

    spectrum
        Frequency-domain spectrum.

    signal_title
        Title of signal subplot.

    spectrum_title
        Title of spectrum subplot.

    style
        Plot style.

    Returns
    -------
    FigureManager
    """

    if style is None:
        style = DEFAULT_STYLE

    figure, axes = plt.subplots(
        2,
        1,
        figsize=style.figsize,
        dpi=style.dpi,
        facecolor=style.facecolor,
    )

    manager = FigureManager(
        figure=figure,
        axes=axes[0],
    )

    # ------------------------------------------------------
    # Time Domain
    # ------------------------------------------------------

    axes[0].plot(
        signal.time,
        signal.value,
        linewidth=style.linewidth,
        alpha=style.alpha,
    )

    axes[0].set_title(
        signal_title,
        fontsize=style.title_size,
    )

    axes[0].set_xlabel(
        "Time (s)",
        fontsize=style.label_size,
    )

    axes[0].set_ylabel(
        "Amplitude",
        fontsize=style.label_size,
    )

    if style.grid:
        axes[0].grid(
            True,
            alpha=style.grid_alpha,
        )

    # ------------------------------------------------------
    # Frequency Domain
    # ------------------------------------------------------

    axes[1].plot(
        spectrum.frequency,
        spectrum.magnitude,
        linewidth=style.linewidth,
        alpha=style.alpha,
    )

    axes[1].set_title(
        spectrum_title,
        fontsize=style.title_size,
    )

    axes[1].set_xlabel(
        "Frequency (Hz)",
        fontsize=style.label_size,
    )

    axes[1].set_ylabel(
        "Magnitude",
        fontsize=style.label_size,
    )

    if style.grid:
        axes[1].grid(
            True,
            alpha=style.grid_alpha,
        )

    if style.tight_layout:
        figure.tight_layout()

    return manager

# ==========================================================
# Save Current Figure
# ==========================================================

def save_current_figure(
    filename: str,
    *,
    dpi: Optional[int] = None,
    transparent: bool = False,
    bbox_inches: str = "tight",
) -> Path:
    """
    Save current matplotlib figure.

    Parameters
    ----------
    filename
        Output filename.

    dpi
        Figure DPI.
        If None, use matplotlib default.

    transparent
        Whether to save with transparent background.

    bbox_inches
        Bounding box option.

    Returns
    -------
    Path
        Absolute output path.
    """

    output_path = image_path(filename)

    # 自动创建目录
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    plt.savefig(
        output_path,
        dpi=dpi,
        transparent=transparent,
        bbox_inches=bbox_inches,
    )

    return output_path.resolve()

# ==========================================================
# Public Export
# ==========================================================

__all__ = [

    # Style
    "PlotStyle",

    # Figure
    "FigureManager",

    # Signal
    "plot_signal",

    # Spectrum
    "plot_spectrum",
    "plot_single_spectrum",

    # Comparison
    "plot_compare",

    # Combined
    "plot_signal_and_spectrum",

    # Save
    "save_current_figure",
]