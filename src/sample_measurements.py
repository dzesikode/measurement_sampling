from collections import OrderedDict, defaultdict
from datetime import datetime, timedelta

from src.measurement_types import MeasType, Measurement

ResultType = defaultdict[MeasType, list[dict[datetime, Measurement]]]


def groupMeasurementsByType(measurements: list[Measurement]) -> defaultdict[MeasType, list[Measurement]]:
    """
    Group the given list of measurements by measurement type.

    Args:
        measurements (list): The list of measurements to group.

    Returns:
        defaultdict: The measurements grouped by type.
    """
    measurementsGroupedByType = defaultdict(list)
    for measurement in measurements:
        measurementsGroupedByType[measurement.measurementType].append(measurement)
    return measurementsGroupedByType


def isMeasurementInInterval(measurementTime: datetime, intervalStart: datetime, intervalEnd: datetime) -> bool:
    """
    Check if the given measurement is within the provided interval.

    Args:
        measurementTime (datetime): The time of the measurement to check.
        intervalStart (datetime): The lower bound of the interval.
        intervalEnd (datetime): The upper bound of the interval.

    Returns:
        bool: Whether the given time is within the interval or not.
    """
    return measurementTime > intervalStart and measurementTime <= intervalEnd


def sampleMeasurements(measurementStartTime: datetime, unsampledMeasurements: list[Measurement]) -> defaultdict[MeasType, list[dict[datetime, Measurement]]]:
    """
    Sample the given measurements with five-minute intervals

    Args:
        measurementStartTime (datetime): The time to start the interval count.
        unsampledMeasurements (list): The list of measurements to sample.

    Returns:
        defaultdict: The sampled measurements grouped by type with the intervals and measurements within those intervals.
    """
    measurementsGroupedByType = groupMeasurementsByType(unsampledMeasurements)
    result: ResultType = defaultdict(list)
    for measurementType, samples in measurementsGroupedByType.items():
        sortedMeasurements: list[Measurement] = sorted(samples, key=lambda m: m.measurementTime)
        intervalStart = measurementStartTime
        intervalEnd = intervalStart + timedelta(minutes=5)
        intervals = OrderedDict()
        for measurement in sortedMeasurements:
            while True:
                if measurement.measurementTime < intervalStart:
                    break
                elif isMeasurementInInterval(measurement.measurementTime, intervalStart, intervalEnd):
                    intervals[intervalEnd] = measurement
                    break
                else:
                    intervalStart = intervalEnd
                    intervalEnd = intervalStart + timedelta(minutes=5)
        if intervals:
            result[measurementType].extend([{interval: measurement} for interval, measurement in intervals.items()])

    return result
