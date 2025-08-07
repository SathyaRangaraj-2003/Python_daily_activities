#activity_05:
#json string to python

import json

json_input = '{"product" : "Book", "price": 9.99}'
data = json.loads(json_input)
print(data['product'] , data['price'])
