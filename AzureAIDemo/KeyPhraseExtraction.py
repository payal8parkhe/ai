
language_key = 'EVErnyTVZwTGkVSp8ElK05Mr4abGgZ8GhDZpPHbd80yRKWNtVU0DJQQJ99BAACGhslBXJ3w3AAAaACOGQTpW'
language_endpoint = 'https://mylanguageresource123.cognitiveservices.azure.com/'

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Authenticate the client using your key and endpoint 
def authenticate_client():
    ta_credential = AzureKeyCredential(language_key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=language_endpoint, 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

def key_phrase_extraction_example(client):

    try:
        documents = ["Dr. Smith has a very modern medical office, and she has great staff."]

        response = client.extract_key_phrases(documents = documents)[0]

        if not response.is_error:
            print("\tKey Phrases:")
            for phrase in response.key_phrases:
                print("\t\t", phrase)
        else:
            print(response.id, response.error)

    except Exception as err:
        print("Encountered exception. {}".format(err))
        
key_phrase_extraction_example(client)