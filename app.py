
import openai
import requests
import json

# Set your OpenAI API key
# openai.api_key = 'API-KEY'

# Function to send a prompt and get a response from the ChatGPT model
def chat(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',  # Specify the ChatGPT model
        prompt=prompt,
        max_tokens=50,  # Adjust the response length as needed
        n=1,
        stop=None,
        temperature=0.7  # Control the randomness of the response
    )
    return response.choices[0].text.strip()

def GetBitCoinPrices():
    url = "https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd/history"
    querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"7d"}

    headers = {
        "X-RapidAPI-Key": "b699e05ccbmsh6834f6ee8604814p134359jsne7ea5baa3dc2",
        "X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    JSONResult = json.loads(response.text)
    history = JSONResult["data"]["history"]
    prices = []
    for change in history:
        prices.append(change["price"])
    pricesList = ','.join(prices)
    return pricesList

bitcoinPrices = GetBitCoinPrices()

chatGPTPrompt = f"""You are an expert crypto trader with more than 10 years of experience,
I will provide you with a list of bitcoin prices for the last 7 days,
can you provide me with a technical analysis
of Bitcoin based on these prices. here is what I want:
Price Overview,
Moving Average Convergence Divergence (MACD),
Advice and Suggestion,
Do I buy or sell?
Please be as detailed as you can, and explain in a way any beginner can understand. and make
Here is the price list: {bitcoinPrices}"""


analysied_data = chat(chatGPTPrompt)
print(analysied_data)
