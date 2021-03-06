#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    ButtonThread
   Description :  子线程，监听按键操作
   Author :       Slientsky
   date：         2018-04-23
-------------------------------------------------
   Change Activity:
                   2018-04-23
-------------------------------------------------
"""

import threading
import os
import sys
import time
import RPi.GPIO as GPIO

class button():
	def __init__(self, pin, oled):
		self.oled = oled
		self.timesleep = 1
		self.pin = pin
		self.bt1_in_value = 0
		self.press_time = 1
		self.count_down = 10
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.pin,GPIO.IN)
		
		GPIO.add_event_detect(pin, GPIO.FALLING, callback= self.onPress,bouncetime=500)

	def onPress(self, channel):
		# print('pressed')
		self.press_time+=1
		if self.press_time >5:
			self.press_time=1
			self.oled.display = 0
		elif self.press_time==2:
			self.oled.display = 2
		elif self.press_time==3:
			# print('python will close in %s'%(self.count_down))
			self.oled.count = 10
			self.oled.display = 3
		elif self.press_time==4:
			# print('system will restart in %s'%(self.count_down))
			self.oled.count = 10
			self.oled.display = 4
		elif self.press_time==5:
			# print('system will halt in %s'%(self.count_down))
			self.oled.count = 10
			self.oled.display = 5
			
	def cleanup(self):
		'''释放资源，不然下次运行是可能会收到警告
		'''
		print('clean up')
		GPIO.cleanup()