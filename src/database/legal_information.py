```python
from pymongo import MongoClient

class LegalInformation:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['legal_database']
        self.collection = self.db['legal_information']

    def fetch_legal_info(self, claim):
        legal_info = self.collection.find_one({"claim": claim})
        return legal_info

    def insert_legal_info(self, legal_info):
        self.collection.insert_one(legal_info)

    def update_legal_info(self, claim, legal_info):
        self.collection.update_one({"claim": claim}, {"$set": legal_info})

    def delete_legal_info(self, claim):
        self.collection.delete_one({"claim": claim})
```