"""
==========================================================
Communication_Principle_Python

File:
    export.py

Version:
    1.1.0

Description:
    数据导出模块
    Python 3.9 Compatible

==========================================================
"""

from __future__ import annotations

import csv
import json

from pathlib import Path
from typing import Any
from typing import Dict
from typing import Iterable
from typing import List

import matplotlib.pyplot as plt
import numpy as np

from .config import DATA_DIR
from .config import IMAGE_DIR

from .models import Signal
from .models import Spectrum


class Exporter:
    """
    数据导出器
    """

    def __init__(
        self,
        image_dir: Path = IMAGE_DIR,
        data_dir: Path = DATA_DIR
    ):

        self.image_dir = Path(image_dir)

        self.data_dir = Path(data_dir)

        self.image_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        self.data_dir.mkdir(
            parents=True,
            exist_ok=True
        )

    # =====================================================
    # 内部路径
    # =====================================================

    def image_path(
        self,
        filename: str
    ) -> Path:

        return self.image_dir / filename

    def data_path(
        self,
        filename: str
    ) -> Path:

        return self.data_dir / filename

    # =====================================================
    # 图片保存
    # =====================================================

    def save_png(
        self,
        filename: str,
        dpi: int = 300
    ) -> Path:

        path = self.image_path(filename)

        plt.savefig(

            path,

            dpi=dpi,

            bbox_inches="tight"

        )

        return path

    def save_svg(
        self,
        filename: str
    ) -> Path:

        path = self.image_path(filename)

        plt.savefig(

            path,

            format="svg",

            bbox_inches="tight"

        )

        return path

    def save_pdf(
        self,
        filename: str
    ) -> Path:

        path = self.image_path(filename)

        plt.savefig(

            path,

            format="pdf",

            bbox_inches="tight"

        )

        return path

    # =====================================================
    # NumPy
    # =====================================================

    def save_numpy(
        self,
        filename: str,
        array: np.ndarray
    ) -> Path:

        path = self.data_path(filename)

        np.save(

            path,

            array

        )

        return path

    # =====================================================
    # Signal
    # =====================================================

    def save_signal(
        self,
        signal: Signal,
        filename: str
    ) -> Path:

        path = self.data_path(filename)

        data = np.column_stack(

            (

                signal.time,

                signal.value

            )

        )

        np.savetxt(

            path,

            data,

            delimiter=",",

            header="time,value",

            comments=""

        )

        return path

    # =====================================================
    # Spectrum
    # =====================================================

    def save_spectrum(
        self,
        spectrum: Spectrum,
        filename: str
    ) -> Path:

        path = self.data_path(filename)

        data = np.column_stack(

            (

                spectrum.frequency,

                spectrum.magnitude,

                spectrum.phase

            )

        )

        np.savetxt(

            path,

            data,

            delimiter=",",

            header="frequency,magnitude,phase",

            comments=""

        )

        return path

    # =====================================================
    # CSV
    # =====================================================

    def save_csv(
        self,
        filename: str,
        header: List[str],
        rows: Iterable[Iterable[Any]]
    ) -> Path:
        """
        保存CSV文件
        """

        path = self.data_path(filename)

        with open(
            path,
            "w",
            newline="",
            encoding="utf-8-sig"
        ) as f:

            writer = csv.writer(f)

            if header:
                writer.writerow(header)

            writer.writerows(rows)

        return path

    # =====================================================
    # Dict -> CSV
    # =====================================================

    def save_dict(
        self,
        filename: str,
        data: Dict[str, Any]
    ) -> Path:
        """
        保存字典为CSV
        """

        rows = []

        for key, value in data.items():

            rows.append([key, value])

        return self.save_csv(

            filename,

            ["Key", "Value"],

            rows

        )

    # =====================================================
    # JSON
    # =====================================================

    def save_json(
        self,
        filename: str,
        data: Dict[str, Any]
    ) -> Path:
        """
        保存JSON
        """

        path = self.data_path(filename)

        with open(
            path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(

                data,

                f,

                indent=4,

                ensure_ascii=False

            )

        return path

    # =====================================================
    # 批量保存Signal
    # =====================================================

    def save_signals(
        self,
        signals: List[Signal],
        prefix: str = "signal"
    ) -> List[Path]:

        paths = []

        for index, signal in enumerate(signals, start=1):

            filename = f"{prefix}_{index:03d}.csv"

            paths.append(

                self.save_signal(

                    signal,

                    filename

                )

            )

        return paths

    # =====================================================
    # 批量保存Spectrum
    # =====================================================

    def save_spectra(
        self,
        spectra: List[Spectrum],
        prefix: str = "spectrum"
    ) -> List[Path]:

        paths = []

        for index, spectrum in enumerate(spectra, start=1):

            filename = f"{prefix}_{index:03d}.csv"

            paths.append(

                self.save_spectrum(

                    spectrum,

                    filename

                )

            )

        return paths

    # =====================================================
    # 实验结果
    # =====================================================

    def save_result(
        self,
        filename: str,
        result: Dict[str, Any]
    ) -> Path:

        if filename.lower().endswith(".json"):

            return self.save_json(

                filename,

                result

            )

        return self.save_dict(

            filename,

            result

        )


# ==========================================================
# 默认Exporter
# ==========================================================

_default_exporter = Exporter()


# ==========================================================
# 快捷接口
# ==========================================================

def save_png(
    filename: str,
    dpi: int = 300
) -> Path:

    return _default_exporter.save_png(
        filename,
        dpi
    )


def save_svg(
    filename: str
) -> Path:

    return _default_exporter.save_svg(
        filename
    )


def save_pdf(
    filename: str
) -> Path:

    return _default_exporter.save_pdf(
        filename
    )


def save_signal(
    signal: Signal,
    filename: str
) -> Path:

    return _default_exporter.save_signal(
        signal,
        filename
    )


def save_spectrum(
    spectrum: Spectrum,
    filename: str
) -> Path:

    return _default_exporter.save_spectrum(
        spectrum,
        filename
    )


def save_csv(
    filename: str,
    header: List[str],
    rows: Iterable[Iterable[Any]]
) -> Path:

    return _default_exporter.save_csv(
        filename,
        header,
        rows
    )


def save_json(
    filename: str,
    data: Dict[str, Any]
) -> Path:

    return _default_exporter.save_json(
        filename,
        data
    )


# ==========================================================
# End of File
# ==========================================================