import requests
import json
url = 'http://127.0.0.1:5000/predict'
headers = {"Content-Type": "application/json"}
from data_input1 import data_in
data = json.dumps(data_in)
r_survey = requests.post(url, data)
print(url)
print(r_survey)
# print(send_request.json())
# r = requests.post(url,data)
# print(r.json())