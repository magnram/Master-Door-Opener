import RPi.GPIO as GPIO
import pigpio
from time import sleep
from flask import Flask

pwm = pigpio.pi()
servo = 20
frequence = 50
pwm.set_mode(servo, pigpio.OUTPUT)
pwm.set_PWM_frequency(servo, frequence)

app = Flask(__name__)
@app.route("/")
def index():
    pwm.set_mode(servo, pigpio.OUTPUT)
    pwm.set_PWM_frequency(servo, frequence)
    pwm.set_servo_pulsewidth(servo, 750)
    sleep(1)
    pwm.set_servo_pulsewidth(servo, 0)
    sleep(2)
    pwm.set_servo_pulsewidth(servo, 2250)
    sleep(1)
    pwm.set_PWM_dutycycle(servo, 0)
    pwm.set_PWM_frequency( servo, 0 )
    return ("", 204)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090)
