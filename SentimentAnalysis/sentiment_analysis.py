import requests # Import the requests library to handle HTTP requests
import json

def sentiment_analyzer(text_to_analyse):
    # Define a function named sentiment_analyzer that takes a string
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict' # URL of the sentiment analysis service myobj
    
    # Constructing the request payload in the expected format
    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } } # Create a dictionary with the text to be analyzed
    
    # Custom header specifying the model ID for the sentiment analysis service header
    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"} # Set the headers required for the API request

    # Sending a POST request to the sentiment analysis API
    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json = myobj, headers=header) # Send a POST request to the API with the text and headers

    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        # Parsing the JSON response from the API
        # Parse the response from the API
        formatted_response = json.loads(response.text)
        # Extracting sentiment label and score from the response
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    # If the response status code is 500, set label and score to None
    elif response.status_code == 500:
        label = None
        score = None
    # For any other unexpected status codes, set label and score to None
    else:
        label = None
        score = None

    # Returning a dictionary containing sentiment analysis results
    # Return the label and score in a dictionary
    return {'label': label, 'score': score}
