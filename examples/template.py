"""
template.py
===========

Experiment template.

Communication Principle Python
"""

from __future__ import annotations

from pathlib import Path
from typing import Callable, Any

from communication.paths import experiment_output_dir

from examples.common import (
    ensure_output_dir,
    finish_experiment,
)


class ExperimentTemplate:
    """
    Experiment template.

    All examples should inherit or use this class.
    """

    def __init__(
        self,
        chapter: int,
        experiment: str,
    ) -> None:

        self.chapter = chapter

        self.experiment = experiment

        self.output_dir = ensure_output_dir(

            experiment_output_dir(

                chapter,

                experiment,

            )

        )

    @property
    def output(self) -> Path:
        """
        Output directory.
        """

        return self.output_dir

    def finish(self) -> None:
        """
        Finish experiment.
        """

        finish_experiment(

            self.experiment,

            self.output_dir,

        )