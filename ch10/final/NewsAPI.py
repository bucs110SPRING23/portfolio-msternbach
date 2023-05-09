import requests
import json

class NewsAPI:
    def __init__(self, api_key):
        '''
        Initializes the news for the city
        Args: The api_key
        '''
        self.api_key = api_key
    
    def __str__(self):
        '''
        Turns the API data into string
        Args: None
        Return: api data in string form
        '''
        api_key = self.api_key
        return api_key

    def get(self, city):
        '''
        Gets the data about the news for the city
        Args: City
        Return: returns the data found from the API
        '''
        url = f"https://newsapi.org/v2/top-headlines?q={city}&apiKey={self.api_key}"
        response = requests.get(url)
        data = json.loads(response.text)
        return data
    