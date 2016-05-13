# Control-LED
[![Build Status](https://drone.io/github.com/wuttinunt/Control-LED/status.png)](https://drone.io/github.com/wuttinunt/Control-LED/latest)

Control LED with Raspberrypi and ThingSpeak

## Clone repository
```bash
git clone https://github.com/wuttinunt/Control-LED.git
cd Control-LED
```

## Run
Ensure you connect jumper wire between Raspberry Pi and LED if already let's Run it.

```bash
sudo python led.py
```

## Control
This is my ThingSpeak account you can register account free from www.thingspeak.com and setting somthing but it easy
go to websit https://api.thingspeak.com/update?api_key=GWHB4M9HGNS2Y5VM&field1=XXX
You can replace ```bash XXX ``` by digit.

```bash
Means of digit
10 = > LED 1 off
11 = > LED 1 on
20 = > LED 2 off
21 = > LED 2 on
30 = > LED 3 off
31 = > LED 4 on
777 = > Turn off all LED
999 = > Turn on all LED
```


