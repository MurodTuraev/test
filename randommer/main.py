# 1d6f8b85f44b411b864257fee6dafed3
import requests
import json
from pprint import pprint
header = {'X-Api-Key': '1d6f8b85f44b411b864257fee6dafed3'}
url = 'https://randommer.io/api/Card'
r = requests.get(url, headers=header).json()
# for i in r:
#     pprint(i[0])
pprint(r)
