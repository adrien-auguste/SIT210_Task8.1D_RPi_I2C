from smbus import SMBus
from adafruit_seesaw.seesaw import Seesaw
import time
import board

# Setting up the soil moisture sensor - address is 0x36
i2c_bus = board.I2C()
mt_sensor= Seesaw(i2c_bus, addr=0x36) 

try:
	while True:
	

			
			temp = round(mt_sensor.get_temp(),2)
			time.sleep(3)
			if temp > 30:
				print('Room temperature is: '+ str(temp)+ '\nPlease turn on the A/C room is too hot')
			elif ((temp >26) and (temp <=30)):
				print('Room temperature is: '+ str(temp)+ '\nPlease turn on the A/C room is hot')
			elif temp < 15:
				print('Room temperature is: '+str(temp)+ '\nPlease turn in the Heater room is too cold')
			elif ((temp >15) and (temp <=20)):
				print('Room temperature is: '+str(temp)+ '\nPlease turn in the Heater room is cold')
			else:
				print('Room temperature is: '+str(temp)+ '\nThis is nice temperature')

			
except KeyboardInterrupt:
	
	print("Completed")

