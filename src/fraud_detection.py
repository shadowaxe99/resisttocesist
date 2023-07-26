```python
import re
from sklearn.ensemble import RandomForestClassifier

class FraudDetection:
    def __init__(self):
        self.model = RandomForestClassifier()

    def preprocess(self, letter):
        # Preprocessing steps like removing special characters, lowercasing etc.
        processed_letter = re.sub('[^a-zA-Z]', ' ', letter)
        processed_letter = processed_letter.lower()
        return processed_letter

    def extract_features(self, letter):
        # Feature extraction from the letter
        # This is a placeholder and should be replaced with actual feature extraction code
        features = []
        return features

    def train_model(self, training_data, labels):
        # Training the model with training data and labels
        self.model.fit(training_data, labels)

    def predict_fraud(self, letter):
        # Predicting if the letter is fraudulent
        processed_letter = self.preprocess(letter)
        features = self.extract_features(processed_letter)
        fraud_score = self.model.predict_proba([features])[0][1]
        return fraud_score

def detectFraud(userInput):
    fraud_detector = FraudDetection()
    fraudScore = fraud_detector.predict_fraud(userInput)
    return fraudScore
```