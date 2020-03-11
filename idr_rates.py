import requests

jsion_data =requests.get('http://www.floatrates.com/daily/idr.json')

print(jsion_data.json())