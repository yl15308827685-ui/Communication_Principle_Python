"""
Communication_Principle_Python

PyTest Global Configuration
"""

from pathlib import Path
import sys

import pytest


# ======================================================
# Project
# ======================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

SRC_DIR = PROJECT_ROOT / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))


# ======================================================
# SDK
# ======================================================

import communication as comm


# ======================================================
# Fixtures
# ======================================================

@pytest.fixture(scope="session")
def config():

    return comm.ExperimentConfig()


@pytest.fixture(scope="session")
def generator(config):

    return comm.SignalGenerator(config)


@pytest.fixture(scope="session")
def sine(generator):

    return generator.sine()


@pytest.fixture(scope="session")
def cosine(generator):

    return generator.cosine()


@pytest.fixture(scope="session")
def square(generator):

    return generator.square()


@pytest.fixture(scope="session")
def triangle(generator):

    return generator.triangle()


@pytest.fixture(scope="session")
def spectrum(sine):

    return comm.fft(sine)
