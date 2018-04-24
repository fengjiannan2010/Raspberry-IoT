#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     onenetPostTest
   Description :
   Author :       Slientsky
   date：          2018-04-23
-------------------------------------------------
   Change Activity:
                   2018-04-23
-------------------------------------------------
"""
import datetime
import time
import requests
import json
import sys
import random
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
	reload(sys)
	sys.setdefaultencoding(defaultencoding)

class onenet():
	def __init__(self, deviceid='29577383', apikey='QzCP2X7dyYVCg=loObHOt6L6hQ8='):
		# 设备ID
		self.DEVICEID = deviceid
		# 数据流名称
		self.SENSORID = ''
		# 数值
		self.VALUE = 0
		# APIKEY
		self.APIKEY = apikey
		
		self.num = 0
		self.dict = {"datastreams": []}

	def set(self, sensorid, value):
		self.SENSORID = sensorid
		self.VALUE = value
		
		d = {"id": "TEMP", "datapoints": [{"value": 50}]}
		d['id'] = self.SENSORID
		d['datapoints'][0]['value'] = self.VALUE
		self.dict['datastreams'].append(d)

	def post(self):
		url = 'http://api.heclouds.com/devices/%s/datapoints' % (self.DEVICEID)
		s = json.dumps(self.dict)
		headers = {
			"api-key": self.APIKEY,
			"Connection": "close",
		}
		try:
			r = requests.post(url, headers = headers, data = s)
		except requests.RequestException:
			return False
		finally:
			self.dict = {"datastreams": []}
		# print(r.text)
		return r


def main():
	DEVICEID = '29577383'
	APIKEY = 'QzCP2X7dyYVCg=loObHOt6L6hQ8='

	rPi = onenet(DEVICEID, APIKEY)
	num = 0

	while True:
		# VALUE = 100
		if num < 10:
			rPi.set("Test1", random.randint(1, 100))
			rPi.set("Test2", random.randint(1, 100))
			# print(rPi.dict)
			r = rPi.post()
			num +=1
			print(r.headers)
			print('1',20 * '*')
			print(r.text)
			print('2',20 * '*')
			time.sleep(5)
		else:break

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		pass