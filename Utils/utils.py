import re

def is_valid_vehicle_number(vehicle_number):
	''' Regex to check the correct format for car registration number '''
	if not re.match('^[A-Z]{2}-[0-9]{2}-[A-Z]{2}-[0-9]{4}', vehicle_number):
		return False
	return True