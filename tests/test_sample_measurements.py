from collections import defaultdict
from datetime import datetime

from src.measurement_types import MeasType, Measurement
from src.sample_measurements import sampleMeasurements


def testSampleMeasurementsNormalCase():
    startTime = datetime(2017, 1, 3, 10, 0, 0)
    measurements = [
        Measurement(datetime(2017, 1, 3, 10, 4, 45), MeasType.TEMP, 35.79),
        Measurement(datetime(2017, 1, 3, 10, 1, 18), MeasType.SPO2, 98.78),
        Measurement(datetime(2017, 1, 3, 10, 9, 7), MeasType.TEMP, 35.01),
        Measurement(datetime(2017, 1, 3, 10, 3, 34), MeasType.SPO2, 96.49),
        Measurement(datetime(2017, 1, 3, 10, 2, 1), MeasType.TEMP, 35.82),
        Measurement(datetime(2017, 1, 3, 10, 5, 0), MeasType.SPO2, 97.17),
        Measurement(datetime(2017, 1, 3, 10, 5, 1), MeasType.SPO2, 95.08),
    ]
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
    assert output == expected


def testSampleMeasurementsEmptyList():
    startTime = datetime(2017, 1, 3, 10, 0, 0)
    output = sampleMeasurements(startTime, [])
    assert output == defaultdict(list)


def testSampleMeasurementsSingleMeasurement():
    startTime = datetime(2017, 1, 3, 10, 0, 0)
    measurements = [Measurement(datetime(2017, 1, 3, 10, 2, 30), MeasType.TEMP, 36.5)]
    output = sampleMeasurements(startTime, measurements)
    expected = {MeasType.TEMP: [{datetime(2017, 1, 3, 10, 5): measurements[0]}]}
    assert output == expected


def testSampleMeasurementsAllMeasurementsBeforeStartTime():
    startTime = datetime(2017, 1, 3, 10, 0, 0)
    measurements = [
        Measurement(datetime(2017, 1, 3, 9, 55, 0), MeasType.TEMP, 36.5),
        Measurement(datetime(2017, 1, 3, 9, 58, 0), MeasType.SPO2, 98.0),
    ]
    output = sampleMeasurements(startTime, measurements)
    assert output == defaultdict(list)


def testSampleMeasurementsAllMeasurementsInSameInterval():
    startTime = datetime(2017, 1, 3, 10, 0, 0)
    measurements = [
        Measurement(datetime(2017, 1, 3, 10, 2, 0), MeasType.TEMP, 36.5),
        Measurement(datetime(2017, 1, 3, 10, 3, 0), MeasType.TEMP, 36.7),
        Measurement(datetime(2017, 1, 3, 10, 4, 0), MeasType.TEMP, 36.9),
    ]
    output = sampleMeasurements(startTime, measurements)
    expected = {MeasType.TEMP: [{datetime(2017, 1, 3, 10, 5): measurements[2]}]}
    assert output == expected


def testSampleMeasurementsMeasurementsSpanMultipleIntervals():
    startTime = datetime(2017, 1, 3, 10, 0, 0)
    measurements = [
        Measurement(datetime(2017, 1, 3, 10, 2, 0), MeasType.TEMP, 36.5),
        Measurement(datetime(2017, 1, 3, 10, 7, 0), MeasType.TEMP, 36.7),
        Measurement(datetime(2017, 1, 3, 10, 12, 0), MeasType.TEMP, 36.9),
    ]
    output = sampleMeasurements(startTime, measurements)
    expected = {
        MeasType.TEMP: [
            {datetime(2017, 1, 3, 10, 5): measurements[0]},
            {datetime(2017, 1, 3, 10, 10): measurements[1]},
            {datetime(2017, 1, 3, 10, 15): measurements[2]},
        ]
    }
    assert output == expected


def testSampleMeasurementsStartTimeNotOnExactInterval():
    startTime = datetime(2017, 1, 3, 10, 2, 30)
    measurements = [
        Measurement(datetime(2017, 1, 3, 10, 3, 0), MeasType.TEMP, 36.5),
        Measurement(datetime(2017, 1, 3, 10, 8, 0), MeasType.TEMP, 36.7),
    ]
    output = sampleMeasurements(startTime, measurements)
    expected = {
        MeasType.TEMP: [
            {datetime(2017, 1, 3, 10, 7, 30): measurements[0]},
            {datetime(2017, 1, 3, 10, 12, 30): measurements[1]},
        ]
    }
    assert output == expected
