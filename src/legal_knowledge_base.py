```python
import json

class LegalKnowledgeBase:
    def __init__(self):
        self.legal_info = self.load_legal_info()

    def load_legal_info(self):
        with open('src/database/legal_information.py', 'r') as file:
            legal_info = json.load(file)
        return legal_info

    def fetch_legal_info(self, userInput):
        legalInfo = {}
        for claim in userInput['claims']:
            if claim in self.legal_info:
                legalInfo[claim] = self.legal_info[claim]
        return legalInfo
```