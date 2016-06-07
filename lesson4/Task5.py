from urllib2 import urlopen
from lxml.html import parse
import requests
from requests.auth import HTTPBasicAuth
import json

with open("clients.txt") as json_file:
    json_data = json.load(json_file)

ENDPOINT = 'https://python-for-qa.herokuapp.com/login'

for i in json_data:
    USER = i['name']
    PASSWORD = i['password']
    response = requests.get(ENDPOINT, auth=HTTPBasicAuth(USER, PASSWORD))
    status = response.status_code
    if status == 401:
        print USER