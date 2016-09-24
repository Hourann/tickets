import re
import requests
from pprint import pprint


url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8955'
r = requests.get(url, verify=False)
tmp = re.findall(r'([A-Z]+)\|([a-z]+)', r.text)
stations = {k:v for v,k in tmp}
pprint(stations, indent=4)