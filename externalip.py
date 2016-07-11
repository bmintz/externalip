# Version 1 ~ TehProject26

import requests

# Vists The 'url' Can Captures The Data
url = 'http://myexternalip.com/raw'
req = requests.get(url)
Cip = req.text

# Prints The IP & '\033[1m' = To Bold White Font
print("\n")
print('\033[1m' + Cip)
print("\n")

