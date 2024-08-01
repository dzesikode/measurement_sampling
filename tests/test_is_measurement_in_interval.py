import pytest
from datetime import datetime, timedelta
from src.sample_measurements import isMeasurementInInterval


@pytest.fixture
def baseTime():
    return datetime(2024, 7, 31, 12, 0, 0)  # July 31, 2024, 12:00:00


def testMeasurementInsideInterval(baseTime):

    intervalStart = baseTime
    intervalEnd = baseTime + timedelta(hours=1)
    measurementTime = baseTime + timedelta(minutes=30)
    assert isMeasurementInInterval(measurementTime, intervalStart, intervalEnd)


def testMeasurementAtIntervalEnd(baseTime):
    intervalStart = baseTime
    intervalEnd = baseTime + timedelta(hours=1)
    measurementTime = intervalEnd
    assert isMeasurementInInterval(measurementTime, intervalStart, intervalEnd)


def testMeasurementAtIntervalStart(baseTime):
    intervalStart = baseTime
    intervalEnd = baseTime + timedelta(hours=1)
    measurementTime = intervalStart
    assert not isMeasurementInInterval(measurementTime, intervalStart, intervalEnd)


def testMeasurementBeforeInterval(baseTime):
    intervalStart = baseTime
    intervalEnd = baseTime + timedelta(hours=1)
    measurementTime = baseTime - timedelta(minutes=1)
    assert not isMeasurementInInterval(measurementTime, intervalStart, intervalEnd)


def testMeasurementAfterInterval(baseTime):
    intervalStart = baseTime
    intervalEnd = baseTime + timedelta(hours=1)
    measurementTime = baseTime + timedelta(hours=2)
    assert not isMeasurementInInterval(measurementTime, intervalStart, intervalEnd)


def testZeroLengthInterval(baseTime):
    intervalStart = baseTime
    intervalEnd = baseTime
    measurementTime = baseTime
    assert not isMeasurementInInterval(measurementTime, intervalStart, intervalEnd)
