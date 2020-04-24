import requests 
from data_input import data_in
import json
url = 'http://127.0.0.1:5000/predict'

# test data

data = json.dumps(data_in)
data
r_survey = requests.post(url, data)
print(url)
print(r_survey)
# send_request = requests.post(url, data)
# print(send_request)
# print(send_request.json())