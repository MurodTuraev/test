# 1597735413:AAEA20RoZ_JJsQ3b4q8XvKuegECeH-i6exk
import requests
import json
from pprint import pprint
token = '1597735413:AAEA20RoZ_JJsQ3b4q8XvKuegECeH-i6exk'
url = f'https://api.telegram.org/bot{token}/getMe'

r = requests.get(url).json()
pprint(r)
