#activity_06
import json
json_data = '{"name" : "June", "contact" : {"email" : "june@example.com" , "city" : "Paris"}}'

data = json.loads(json_data)
print(f"Email : {data['contact']['email']} , city : {data['contact']['city']}")