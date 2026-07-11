from communication import SignalGenerator

signal = SignalGenerator.sine(
    frequency=10,
    amplitude=1,
    duration=1
)

signal.plot()