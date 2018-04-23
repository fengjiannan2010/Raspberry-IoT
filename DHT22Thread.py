#!/usr/bin/env python3
import threading
import os
import sys
import time

#轮子
import Adafruit_DHT

  
class tdht22(threading.Thread):
	def __init__(self, pin):
		threading.Thread.__init__(self)
		self.H = 0
		self.T = 0
		self.timesleep = 1
		#温湿度传感器DHT22
		self.sensor = Adafruit_DHT.DHT22
		self.pin = pin
	
	def run(self):
		while True:
			time.sleep(self.timesleep)
			thm = self.getTH()

	def getTH(self):
		humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)#24 是 GPIO 的引脚编号
		# print(humidity, end='')
		# print("   ", end='')
		# print(temperature)
		
		if humidity == None:
			return False
		if temperature == None:
			return False

		self.H = round(humidity,2)
		self.T = round(temperature,2)
		return True

	#传感器温度数据校验，将偏差值较大数据丢弃
	def checkT():
		return ""
	#传感器湿度数据校验，将偏差值较大数据丢弃
	def checkH():
		return ""

# def main():
	# thread = tdht22(24)
	# thread.start()
	
# if __name__ == "__main__":
	# try:
		# main()
	# except KeyboardInterrupt:
		# pass
		
