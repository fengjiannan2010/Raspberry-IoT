# Rasyberry-IoT
### 项目基于python3创建，所以请注意使用pip3安装轮子
```sh
#已实现功能介绍
1、读取传感器数据
2、实时显示数据到oled屏幕
3、定时上传数据到onenet
4、通过按键切换显示页面
5、实现关闭应用，重启系统，关闭系统操作

#将实现的功能
1、从onenet上获取历史数据
2、创建web 服务并展示历史数据
3、通过Restful 请求控制硬件设备
```
## 所需硬件设备型号

硬件连接请参考对应硬件引脚图[简书文章](https://www.jianshu.com/u/06e291ec9827).
数据展示 [OneNet 应用](https://open.iot.10086.cn/appview/p/18739ef05c7a7c8bd6f631aa7e70b02a)

### 1. Raspberry pi (c)
### 2. ssd1306 128*64 OLED I2C
### 3. DHT22
### 4. 按钮模块
### 5. PMSA003
### 6. CH340 or CP2102 USB to TTL（UAERT）

## 安装应用运行所需依赖库
```sh
sudo apt-get install python3-dev python3-pip libfreetype6-dev libjpeg-dev build-essential
sudo apt-get install libopenjp2-7-dev
sudo apt install libsdl-dev libportmidi-dev libsdl-ttf2.0-dev libsdl-mixer1.2-dev libsdl-image1.2-dev
```

## 安装相关python轮子,安装Adafruit_Python_DHT时连同安装RPi.GPIO
```sh
git clone https://github.com/adafruit/Adafruit_Python_DHT
cd Adafruit_Python_DHT
sudo python3 setup.py install
sudo -H pip3 install psutil
sudo -H pip3 install --upgrade luma.oled
sudo -H pip3 install pyserial
sudo -H pip3 install pymodbus
```

## 需要上传数据到onenet平台时
## 新增配置文件onenet.conf,填写onenet上对应的设备号和apikey
```sh
{  
	"Raspberry0":  
	{     
		"deviceid":"********",
		"apikey":"********************"
	} 
} 
```

## 运行程序,如果使用参数onenet.conf --device=Raspberry0（参数定义请根据你的需求修改），可上传数据到onenet平台
```sh
cd Rasyberry-IoT
python3 main.py onenet.conf --device=Raspberry0
-----------------------------------------------
#不添加参数，只显示，不上传数据
python3 main.py
```


