import RPi.GPIO as GPIO     # Import Library to access GPIO PIN
import time                 # To access delay function

GPIO.setmode(GPIO.BOARD)    # Consider complete raspberry-pi board
GPIO.setwarnings(False)     # To avoid same PIN use warning

LED_PIN = 11                # Define PIN for LED
SWITCH_PIN = 12             # Define PIN for switch

GPIO.setup(LED_PIN, GPIO.OUT)   # Set pin function as output
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # Set pin function as input  

while True:
    # Check if switch is pressed or not 
    if GPIO.input(SWITCH_PIN) == GPIO.LOW:
        print("Switch Pressed and LED ON")
        GPIO.output(LED_PIN, GPIO.HIGH)  # LED ON                 
    else:
        print("Switch released and LED OFF")
        GPIO.output(LED_PIN, GPIO.LOW)   # LED OFF
