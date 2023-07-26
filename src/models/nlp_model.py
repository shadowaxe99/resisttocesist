```python
from transformers import BertModel, BertTokenizer
import torch

class NLPModel:
    def __init__(self, model_name='bert-base-uncased'):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = BertModel.from_pretrained(model_name).to(self.device)
        self.tokenizer = BertTokenizer.from_pretrained(model_name)

    def encode(self, text):
        encoded = self.tokenizer.encode_plus(
            text,
            max_length=512,
            truncation=True,
            padding='max_length',
            add_special_tokens=True,
            return_tensors='pt'
        )
        return encoded.to(self.device)

    def predict(self, text):
        self.model.eval()
        with torch.no_grad():
            encoded_text = self.encode(text)
            output = self.model(**encoded_text)
        return output.last_hidden_state.mean(dim=1).cpu().numpy()

nlp_model = NLPModel()
```