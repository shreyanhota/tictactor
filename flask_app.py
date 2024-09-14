from flask import Flask, render_template, Response
import pygame
import time
import runner_new as game

app = Flask(__name__)

@app.route('/')
def index():
    # Renders the HTML page
    return render_template('index.html')

def generate_frame():
    """
    Generate frames of the game to stream to the web.
    """
    while True:
        image = game.get_pygame_image()  # Get the current game frame
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n\r\n')
        time.sleep(0.1)  # Adjust frame rate

@app.route('/video_feed')
def video_feed():
    # Streaming game frames
    return Response(generate_frame(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
