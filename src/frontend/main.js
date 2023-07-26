import React from 'react';
import UserInterface from './user_interface.js';

class Main extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      userInput: '',
      analysisResult: null,
      legalInfo: null,
      fraudScore: null,
      riskScore: null,
      responseRecommendation: null,
      userData: null
    };
    this.handleInputChange = this.handleInputChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleInputChange(event) {
    this.setState({userInput: event.target.value});
  }

  handleSubmit(event) {
    event.preventDefault();
    this.analyzeLetter();
  }

  async analyzeLetter() {
    const response = await fetch('/api/analyzeLetter', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({letter: this.state.userInput})
    });
    const data = await response.json();
    this.setState({
      analysisResult: data.analysisResult,
      legalInfo: data.legalInfo,
      fraudScore: data.fraudScore,
      riskScore: data.riskScore,
      responseRecommendation: data.responseRecommendation
    });
  }

  render() {
    return (
      <UserInterface 
        userInput={this.state.userInput}
        analysisResult={this.state.analysisResult}
        legalInfo={this.state.legalInfo}
        fraudScore={this.state.fraudScore}
        riskScore={this.state.riskScore}
        responseRecommendation={this.state.responseRecommendation}
        handleInputChange={this.handleInputChange}
        handleSubmit={this.handleSubmit}
      />
    );
  }
}

export default Main;