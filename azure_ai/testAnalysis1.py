import sys
sys.path.append('Text-Analytics')
from credential import client
from document import documents
client=client()
response=client.analyze_sentiment(
    documents=documents,
    language='en-US',
    show_opinion_mining=True

)
for idx, doc in enumerate(response):
            print(f"Document {idx + 1}: Sentiment: {doc.sentiment}, Scores: {doc.confidence_scores}")