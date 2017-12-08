#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response, json, request, jsonify
import RPi.GPIO as gpio
import time
import json
from motor import Motors
from servo import Servo
from SensorReader import Sensor
import requests



# import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    #from camera import Camera
    x = 0

# Raspberry Pi camera module (requires picamera package)
from camera_pi import Camera

app = Flask(__name__)
ser = Servo()
m = Motors()
s = Sensor()

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/updateMotion', methods = ['POST'])
def updateMotion():
    motion_model = request.get_json()
    
    if motion_model["left"]:
        print "left"
        m.left()
    elif motion_model["right"]:
        print "right"
        m.right()
    elif motion_model["forward"]:
        print "forward"
        m.forward()
    elif motion_model["reverse"]:
        print "reverse"
        m.reverse()
    elif motion_model["stop"]:
        print("Stop")
        m.stop()
    return "ok"

@app.route('/getData', methods = ['GET'])
def getData():
    hum, temp = s.read()
    data_model = {"temperature": str(temp), "humidity": str(hum)}
    print(hum,temp)
    return jsonify(data_model)

@app.route('/rotateServo', methods = ['POST'])
def rotateServo():
    servo_model = request.get_json()
    turn_value = servo_model["angle"]
    ser.turn(turn_value)
    print turn_value
    return "ok"

if __name__ == '__main__':
    app.run(host='192.168.1.90', threaded=True)
