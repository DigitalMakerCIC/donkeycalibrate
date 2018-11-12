from flask import Flask, render_template
from flask import request
from calibratefunctions import *

import time
import Adafruit_PCA9685
# Initialise the PCA9685 using the default address (0x40).
PCA9685_pwm = Adafruit_PCA9685.PCA9685()


# Set frequency to 100hz, good for l298n h-bridge.
PCA9685_pwm.set_pwm_freq(60)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600 # Max pulse length out of 4096

app = Flask(__name__)

@app.route("/")
def web_interface():
  return render_template('main.html')

@app.route("/set_servo1")
def set_servo1():
  speed = request.args.get("speed")
  print ("Received " + str(speed))
  PCA9685_pwm.set_pwm(0, 0, int(speed))
  return ("Received " + str(speed))

@app.route("/set_servo2")
def set_servo2():
  speed = request.args.get("speed")
  print ("Received " + str(speed))
  PCA9685_pwm.set_pwm(1, 0, int(speed))
  return "Received " + str(speed)

if __name__ == "__main__":
  app.run(host='d2.local', port=8181, debug=True)
