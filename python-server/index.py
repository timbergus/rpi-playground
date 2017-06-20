#import RPi.GPIO as GPIO
import picamera

camera=picamera.PiCamera()

from flask import Flask, render_template

app = Flask(__name__)

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(16, GPIO.OUT)


@app.route('/')
def index():
    #camera.capture('image.jpg')
    return render_template('index.html', image='image.jpg')


#@app.route('/cakes')
#def cakes():
#    return 'Yummy cakes!'


#@app.route('/hello/<name>')
#def hello(name):
#    return render_template('page.html', name=name)


#@app.route('/led/<state>')
#def led(state):
#    if state == 'on':
        # GPIO.output(16, True)
#        return 'Led ON!'
#    else:
        # GPIO.output(16, False)
#        return 'Led OFF!'




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
