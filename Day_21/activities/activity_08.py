#activity_08

#os module

import os

def report_location():
	location = os.getcwd()
	return f"Script is running from: {location}"
print(report_location())