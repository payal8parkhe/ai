 
## Azure AI Cognitive Services

This repository contains hands-on examples for implementing Azure AI Cognitive Services, specifically focusing on Sentiment Analysis, Language Detection, and Key Phrase Extraction. The examples are implemented in Python and utilize the Azure AI Text Analytics SDK.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [File Descriptions](#file-descriptions)
- [Usage](#usage)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- An active Azure subscription. If you do not have one, you can create a [free account](https://azure.microsoft.com/free/).
- Python 3.8 or later installed on your system.
- Azure AI Text Analytics SDK installed. You can install it using pip:

```bash
pip install azure-ai-textanalytics
```

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/payal8parkhe/ai.git
```

2. Navigate to the project directory:

```bash
cd ai
```

3. Set up your Azure credentials 'language_key' and 'language_endpoint' in the each file. You will need to provide your API key and endpoint URL.

## File Descriptions

- **credential.py**: Contains the Azure API key and endpoint configuration. This file should be kept secure and not shared publicly.
  
- **sentimentAnalysis.py**: Implements sentiment analysis using Azure's Text Analytics service. It analyzes the sentiment of provided text and outputs the results.

- **languageDetection.py**: Detects the language of the provided text using Azure's language detection capabilities.

- **keyPhraseExtraction.py**: Extracts key phrases from the provided text, helping to summarize content and identify main topics.

## Usage

To use the scripts, follow these steps:

1. Ensure you have set your Azure credentials in `credential.py`.
2. Run the desired script using Python. For example, to run the sentiment analysis script, use:

```bash
python sentimentAnalysis.py
```

3. Follow the prompts or check the output in the console for results.
