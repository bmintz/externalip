#!/usr/bin/env python3
# encoding: utf-8

import requests

def get_ip():
	return requests.get('https://ifconfig.co/ip').text

if __name__ == '__main__':	
	# Prints The IP & '\033[1m' = To Bold White Font
	print('\n')
	print('\033[1m' + get_ip())

