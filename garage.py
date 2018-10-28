# Import required Python libraries
import RPi.GPIO as GPIO
import time

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

card =""
    
    



print("Scan Card to activate garage")

while True:
    card = input()
    
    try:
        print("Read Card: ", card)
        GPIO.output(7,True)
        time.sleep(1)
        GPIO.output(7,False)
        time.sleep(1)
        
    except OSError as e:
            print ("Execution failed:" )
            range(10000)       # some payload code
            time.sleep(0.2)    # sane sleep time of 0.1 seconds
        
        
        
        
        
GPIO.cleanup()
