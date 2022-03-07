import requests, uuid, json

from config import TRANSLATION_ENDPOINT, TRANSLATION_SUBSCRIPTION_KEY

# Add your subscription key and endpoint
subscription_key = TRANSLATION_SUBSCRIPTION_KEY
endpoint = TRANSLATION_ENDPOINT

# Add your location, also known as region. The default is global.
# This is required if using a Cognitive Services resource.
location = "eastus"

path = '/translate'
constructed_url = endpoint + path


constructed_url = endpoint + path

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

def translate_text(text, language_to, language_from=None):
    
    body = [{
        'text': text
    }]
    
    params = {
    'api-version': '3.0',
    'from': language_from, 
    'to': language_to, 
    }

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    return response[0]['translations'][0]['text']