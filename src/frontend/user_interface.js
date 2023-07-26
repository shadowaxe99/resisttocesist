```javascript
import React, { useState } from 'react';
import axios from 'axios';

const UserInterface = () => {
  const [userInput, setUserInput] = useState('');
  const [analysisResult, setAnalysisResult] = useState(null);
  const [responseRecommendation, setResponseRecommendation] = useState(null);

  const handleInputChange = (event) => {
    setUserInput(event.target.value);
  };

  const handleSubmit = async () => {
    const response = await axios.post('/api/analyzeLetter', { text: userInput });
    setAnalysisResult(response.data.analysisResult);
    setResponseRecommendation(response.data.responseRecommendation);
  };

  return (
    <div>
      <textarea id="inputLetter" onChange={handleInputChange} value={userInput} />
      <button id="submitBtn" onClick={handleSubmit}>Submit</button>
      {analysisResult && (
        <div id="resultDisplay">
          <h2>Analysis Result</h2>
          <p>{analysisResult}</p>
        </div>
      )}
      {responseRecommendation && (
        <div id="recommendationDisplay">
          <h2>Recommended Response</h2>
          <p>{responseRecommendation}</p>
        </div>
      )}
    </div>
  );
};

export default UserInterface;
```