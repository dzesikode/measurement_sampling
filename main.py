from src.measurement_types import MeasType, Measurement
from datetime import datetime
from src.sample_measurements import sampleMeasurements


if __name__ == "__main__":
    exampleMeasurements = [
        Measurement(datetime(2017, 1, 3, 10, 4, 45), MeasType.TEMP, 35.79),
        Measurement(datetime(2017, 1, 3, 10, 1, 18), MeasType.SPO2, 98.78),
        Measurement(datetime(2017, 1, 3, 10, 9, 7), MeasType.TEMP, 35.01),
        Measurement(datetime(2017, 1, 3, 10, 3, 34), MeasType.SPO2, 96.49),
        Measurement(datetime(2017, 1, 3, 10, 2, 1), MeasType.TEMP, 35.82),
        Measurement(datetime(2017, 1, 3, 10, 5, 0), MeasType.SPO2, 97.17),
        Measurement(datetime(2017, 1, 3, 10, 5, 1), MeasType.SPO2, 95.08),
    ]
    startTime = datetime(2017, 1, 3, 10, 0, 0)
    output = sampleMeasurements(startTime, exampleMeasurements)

    for type, intervals in output.items():
        for interval in intervals:
            for intervalKey, measurement in interval.items():
                print(intervalKey, type, measurement.value)
