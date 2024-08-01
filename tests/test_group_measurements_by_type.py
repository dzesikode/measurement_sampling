from datetime import datetime
from src.sample_measurements import groupMeasurementsByType
from src.measurement_types import MeasType, Measurement


def testGroupMeasurementByTypeEmptyList():
    measurements = []
    grouped = groupMeasurementsByType(measurements)
    assert len(grouped) == 0


def testGroupMeasurementsByTypeSingleMeasurement():
    measurement = Measurement(
        measurementTime=datetime.now(), measurementType=MeasType.SPO2, value=98.0
    )
    grouped = groupMeasurementsByType([measurement])
    assert len(grouped) == 1
    assert grouped[MeasType.SPO2] == [measurement]


def testGroupMeasurementsByTypeMultipleTypes():
    measurements = [
        Measurement(
            measurementTime=datetime.now(), measurementType=MeasType.SPO2, value=98.0
        ),
        Measurement(
            measurementTime=datetime.now(), measurementType=MeasType.HR, value=70.0
        ),
        Measurement(
            measurementTime=datetime.now(), measurementType=MeasType.TEMP, value=36.5
        ),
    ]
    grouped = groupMeasurementsByType(measurements)
    assert len(grouped) == 3
    assert len(grouped[MeasType.SPO2]) == 1
    assert len(grouped[MeasType.HR]) == 1
    assert len(grouped[MeasType.TEMP]) == 1


def testGroupMeasurementsByTypeMultipleMeasurementsSameType():
    measurements = [
        Measurement(
            measurementTime=datetime.now(), measurementType=MeasType.SPO2, value=98.0
        ),
        Measurement(
            measurementTime=datetime.now(), measurementType=MeasType.SPO2, value=97.0
        ),
    ]
    grouped = groupMeasurementsByType(measurements)
    assert len(grouped) == 1
    assert len(grouped[MeasType.SPO2]) == 2
