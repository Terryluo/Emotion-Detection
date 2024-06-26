"""
server.py

This module contains the Flask web application for emotion detection.
It includes routes for rendering the index page and handling emotion detection requests.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/')
def index():
    """Render the index.html page."""
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detection():
    """
    Handle the GET request to the /emotionDetector endpoint.
    Analyze the provided text and return the emotion analysis results.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response.get('dominant_emotion') is None:
        return "Invalid text! Please try again."

    return (f"For the given statement, the system response is 'anger': {response.get('anger')}, "
            f"'disgust': {response.get('disgust')}, 'fear': {response.get('fear')}, "
            f"'joy': {response.get('joy')} and 'sadness': {response.get('sadness')}. "
            f"The dominant emotion is <strong>{response.get('dominant_emotion')}</strong>.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
