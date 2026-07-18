"""
communication.paths
===================

Project path helper.

Communication_Principle_Python
"""

from __future__ import annotations

from pathlib import Path


# ==========================================================
# Project Root
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

SRC_ROOT = PROJECT_ROOT / "src"

PACKAGE_ROOT = PROJECT_ROOT / "src" / "communication"

EXAMPLES_ROOT = PROJECT_ROOT / "examples"

OUTPUT_ROOT = PROJECT_ROOT / "output"

DOCS_ROOT = PROJECT_ROOT / "docs"

TESTS_ROOT = PROJECT_ROOT / "tests"

RESOURCE_ROOT = PROJECT_ROOT / "resources"


# ==========================================================
# Internal Helper
# ==========================================================

def ensure_dir(path: Path) -> Path:
    """
    Ensure directory exists.

    Parameters
    ----------
    path
        Directory path.

    Returns
    -------
    pathlib.Path
    """

    path.mkdir(
        parents=True,
        exist_ok=True,
    )

    return path


# ==========================================================
# Output
# ==========================================================

def output_dir() -> Path:
    """
    Return project output directory.
    """

    return ensure_dir(
        OUTPUT_ROOT,
    )


def chapter_output_dir(
    chapter: int,
) -> Path:
    """
    Return output directory of one chapter.

    Example
    -------
    output/chapter01
    """

    return ensure_dir(
        output_dir()
        / f"chapter{chapter:02d}"
    )


def experiment_output_dir(
    chapter: int,
    experiment: str,
) -> Path:
    """
    Return output directory of one experiment.

    Example
    -------
    output/chapter01/exp01_generate_rectangle
    """

    return ensure_dir(
        chapter_output_dir(
            chapter,
        )
        / experiment
    )


# ==========================================================
# Resources
# ==========================================================

def resource_dir() -> Path:
    """
    Return project resource directory.
    """

    return ensure_dir(
        RESOURCE_ROOT,
    )


# ==========================================================
# Temporary
# ==========================================================

def temp_dir() -> Path:
    """
    Return temporary directory.
    """

    return ensure_dir(
        output_dir()
        / "_temp"
    )


# ==========================================================
# Figures
# ==========================================================

def figure_dir(
    experiment_dir: Path,
) -> Path:
    """
    Figure directory of one experiment.
    """

    return ensure_dir(
        experiment_dir
        / "figures"
    )


# ==========================================================
# CSV
# ==========================================================

def csv_dir(
    experiment_dir: Path,
) -> Path:
    """
    CSV directory of one experiment.
    """

    return ensure_dir(
        experiment_dir
        / "csv"
    )


# ==========================================================
# Report
# ==========================================================

def report_dir(
    experiment_dir: Path,
) -> Path:
    """
    Report directory of one experiment.
    """

    return ensure_dir(
        experiment_dir
        / "report"
    )