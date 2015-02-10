import requests
import json
name = raw_input('Enter your Github account name:')

url = 'https://api.github.com/users/'+name+'/repos'

req=requests.get(url).json()

for value in req:
	print value['name']
