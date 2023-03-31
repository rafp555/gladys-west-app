import io
import gladysSatellite as satellite
import math
"""
	Student: John Foster
	Module: gladysCompute
	Description: This module computes the formulas for averaging coordinate positions and calculating distance between two coordinates.
"""


def gpsAverage(x, y):
	"""
		This function averages out the longitude, latitude, altitude, and time values of the input coordinates.
	"""
# Start changes by Rafael Payan for legibility
	summed = satellite.gpsValue(x, y, "longitude")\
			+satellite.gpsValue(x, y, "latitude")\
			+satellite.gpsValue(x, y, "altitude")\
			+satellite.gpsValue(x, y, "time")

	average = summed / 4

	return average
# Stop changes by Rafael Payan

def distance(current, destination):
	"""
		This function computes the distance between two coordinates.
	"""

	distance = distance = math.sqrt(current**2 + destination**2)

	return str(round(distance,2))
