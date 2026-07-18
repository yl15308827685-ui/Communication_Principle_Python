from communication import *
import communication


def test_import():

    generator = SignalGenerator()
    assert generator is not None

    analyzer = SpectrumAnalyzer()
    assert analyzer is not None

    signal_analyzer = SignalAnalyzer()
    assert signal_analyzer is not None

    exporter = SignalExporter()
    assert exporter is not None


def test_version():

    assert isinstance(
        communication.__version__,
        str
    )

    assert len(
        communication.__version__
    ) > 0