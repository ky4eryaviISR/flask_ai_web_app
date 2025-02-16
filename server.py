"""
Main server provide access to emotion detection
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Provide emotion analysis on required text.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    res = emotion_detector(text_to_analyze)
    if res['dominant_emotion']:
        return (
            f"For the given statement, the system response is 'anger': {res['anger']}, "
            f"'disgust': {res['disgust']}, 'fear': {res['fear']}, "
            f"'joy': {res['joy']} and 'sadness': {res['sadness']}. "
            f"The dominant emotion is {res['dominant_emotion']}.")
    return "Invalid text! Please try again!."


@app.route("/")
def render_index_page():
    """ Render the index html file from static """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
