import RPi.GPIO as GPIO
import time



#GPIOの定義
LED1_RED int  = 16  
LED2_GREEN int  = 13  
PORT_SW1 int  = 7  


GPIO.setmode(GPIO.BCM)

GPIO.setup(LED1_RED, GPIO.OUT)  
GPIO.setup(LED2_GREEN, GPIO.OUT)  
GPIO.setup(PORT_SW1, GPIO.IN)

GPIO.output(LED1_RED, GPIO.HIGH)
GPIO.output(LED2_GREEN, GPIO.HIGH)

# 100回繰り返して終了
for i in range(100)
    if GPIO.input(PORT_SW1) == GPIO.LOW
        GPIO.output(LED1_RED, GPIO.LOW) # 点灯
        GPIO.output(LED2_GREEN, GPIO.LOW) # 点灯
        time.sleep(1)
    else    
        GPIO.output(LED2_GREEN, GPIO.LOW) # 点灯
        GPIO.output(LED1_RED, GPIO.HIGH) # 消灯
        time.sleep(0.5)
        GPIO.output(LED1_RED, GPIO.LOW) # 点灯
        GPIO.output(LED2_GREEN, GPIO.HIGH) # 消灯
        time.sleep(0.5)

#GPIO.cleanup()

GPIO.cleanup(LED1_RED)
GPIO.cleanup(LED2_GREEN)
GPIO.cleanup(PORT_SW1)
