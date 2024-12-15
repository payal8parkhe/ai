from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
API_KEY='ANVYIZpMEZLmpXJpLctyDFwSbOy2dcSumjuBOt6WzZWG7vaDwIQrJQQJ99ALACL93NaXJ3w3AAAaACOGJSL3'
ENDPOINT='https://ainew29.cognitiveservices.azure.com/'

def client():
    try:
        client=TextAnalyticsClient(
         endpoint=ENDPOINT,
         credential=AzureKeyCredential(API_KEY)

        )
        return client
    except Exception as e:
        print(e)
        return   