#activity_04:
#dictionary to json string

import json
data = {"city" : "Paris", "Temp" : 21}
json_string = json.dumps(data)
print(json_string)