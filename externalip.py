#!/usr/bin/env python

from __future__ import print_function

import requests

ip = requests.get('https://ifconfig.co/ip').text

# Prints The IP in bold white font
print()
print('\033[1m' + ip)
print()

