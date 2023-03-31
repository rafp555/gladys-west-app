import io
import json


"""
	Student: Sindy Ken and Rafael Payan
	Module: gladysSatellite
	Description: This module cross-references the satellite data to return specific values.
"""

# Start code by Rafael Payan
# enable relative file paths
import pathlib
relativePath = pathlib.Path(__file__).parent 
# Stop code by Rafael Payan

def readSat(sat):
	"""
		reads satellite data from a json file
		Students do NOT need to change the readSat function.
	"""

	# relative data file path
	fileName = sat + "-satellite.json"
	filePath = str(relativePath) + "/data/" + fileName

	# open the file
	try:
		fileHandle = open(filePath)
	except IOError:
		print("ERROR: Unable to open the file " + filePath)
		raise IOError

	# print("filePath = ", filePath)

	# read the file
	data = json.load(fileHandle)

	return data


def gpsValue(x, y, sat):
	"""
		This function retrieves satellite locations from a JSON based on input coordinates.
	"""
# Start code Enhancement by Rafael Payan
# Consolidated Sindy Ken's original code from 4 if elseif conditions to one if
	# Read sattelite data and pull respective values.
	if (0<=x<=99) and (0<=y<=99):
		satDictionary = {}
		satData = readSat(sat)
		for row in satData:
			coordinates = row["x"] , row["y"]
			satLocation = row["value"]
			satDictionary[coordinates] = [satLocation]
		value = satDictionary[(int(x),int(y))]
		return value[0]
	else:
		return 0