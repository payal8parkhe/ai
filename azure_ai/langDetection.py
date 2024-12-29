from credential import client

text_analytics_client = client()
def detect_language(client, text):
    try:
        response = client.detect_language(documents=[{"id": "1", "text": text}])
        for doc in response:
            print(f"Detected Language: {doc.primary_language.name}")
            print(f"ISO Code: {doc.primary_language.iso6391_name}")
            print(f"Confidence Score: {doc.primary_language.confidence_score:.2f}")
    except Exception as err:
        print(f"Error: {err}")
        
if __name__ == "__main__":
    sample_text = input("Enter text to detect language: ")
    detect_language(text_analytics_client, sample_text)
