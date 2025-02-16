from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        params = [
            {'text': 'I am glad this happened', 'value': 'joy'},
            {'text': 'I am really mad about this', 'value': 'anger'},
            {'text': 'I feel disgusted just hearing about this', 'value': 'disgust'},
            {'text': 'I am so sad about this', 'value': 'sadness'},
            {'text': 'I am really afraid that this will happen', 'value': 'fear'}
        ]
        for test_case in params:
            print(test_case)
            res = emotion_detector(test_case['text'])
            self.assertEqual(res['dominant_emotion'], test_case['value'])


unittest.main()