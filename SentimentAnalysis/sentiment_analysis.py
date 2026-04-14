import requests # Import the requests library to handle HTTP requests
import json

def sentiment_analyzer(text_to_analyse): # Define a function named sentiment_analyzer that takes a string
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict' # URL of the sentiment analysis service myobj
    
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } } # Create a dictionary with the text to be analyzed
    
    # Custom header specifying the model ID for the sentiment analysis service header
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"} # Set the headers required for the API request

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json = myobj, headers=header) # Send a POST request to the API with the text and headers

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting sentiment label and score from the response
    label = formatted_response['documentSentiment']['label']
    score = formatted_response['documentSentiment']['score']

    # Returning a dictionary containing sentiment analysis results
    return {'label': label, 'score': score}
