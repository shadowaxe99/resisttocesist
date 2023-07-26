```python
import numpy as np

def assessRisk(analysisResult, legalInfo, fraudScore):
    """
    Function to assess the potential legal risks associated with the claims made in the cease and desist letter.
    It uses the analysis result, legal information and fraud score to calculate a risk score.
    """
    # Initialize risk score
    riskScore = 0

    # Increase risk score based on the severity of the claims made in the letter
    for claim in analysisResult['claims']:
        if claim in legalInfo['severe_claims']:
            riskScore += 2
        elif claim in legalInfo['moderate_claims']:
            riskScore += 1

    # Increase risk score if the letter is likely to be fraudulent
    if fraudScore > 0.5:
        riskScore += 3

    # Normalize risk score to be between 0 and 1
    riskScore = np.clip(riskScore / 10, 0, 1)

    return riskScore
```