```python
from transformers import pipeline

class SentimentDetection:
    def __init__(self):
        self.nlp_model = pipeline('sentiment-analysis')

    def detect_sentiment(self, userInput):
        result = self.nlp_model(userInput)
        return result[0]

def main(userInput):
    sentiment_detector = SentimentDetection()
    analysisResult = sentiment_detector.detect_sentiment(userInput)
    return analysisResult

if __name__ == "__main__":
    userInput = input("Enter the cease and desist letter: ")
    print(main(userInput))
```