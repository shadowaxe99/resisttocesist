```python
from transformers import pipeline

class TextAnalysis:
    def __init__(self):
        self.nlp_model = pipeline('sentiment-analysis')

    def analyze_text(self, userInput):
        analysisResult = self.nlp_model(userInput)
        return analysisResult

    def extract_key_claims(self, userInput):
        # This is a placeholder function. In a real-world application, this would involve complex NLP techniques
        # to extract key claims from the text. For simplicity, we'll assume that the key claims are the first few sentences.
        key_claims = userInput.split('.')[:3]
        return key_claims
```