from src.measurement_types import MeasType, Measurement
from datetime import datetime
from src.sample_measurements import sampleMeasurements


if __name__ == "__main__":
    measurements = [
        Measurement(datetime(2017, 1, 3, 10, 4, 45), MeasType.TEMP, 35.79),
        Measurement(datetime(2017, 1, 3, 10, 1, 18), MeasType.SPO2, 98.78),
        Measurement(datetime(2017, 1, 3, 10, 9, 7), MeasType.TEMP, 35.01),
        Measurement(datetime(2017, 1, 3, 10, 3, 34), MeasType.SPO2, 96.49),
        Measurement(datetime(2017, 1, 3, 10, 2, 1), MeasType.TEMP, 35.82),
        Measurement(datetime(2017, 1, 3, 10, 5, 0), MeasType.SPO2, 97.17),
        Measurement(datetime(2017, 1, 3, 10, 5, 1), MeasType.SPO2, 95.08),
    ]
    startTime = datetime(2017, 1, 3, 10, 0, 0)
    output = sampleMeasurements(startTime, measurements)

    expected = {
        MeasType.TEMP: [
            {datetime(2017, 1, 3, 10, 5): measurements[0]},
            {datetime(2017, 1, 3, 10, 10): measurements[2]},
        ],
        MeasType.SPO2: [
            {datetime(2017, 1, 3, 10, 5): measurements[-2]},
            {datetime(2017, 1, 3, 10, 10): measurements[-1]},
        ],
    }
    for type, intervals in output.items():
        for interval in intervals:
            for interval_key, measurement in interval.items():
                print(interval_key, type, measurement.value)