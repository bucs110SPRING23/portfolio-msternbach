import requests
import json

class LocationAPI:
    def __init__(self, api_key):
        '''
        Initializes the location for the city
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
        Gets the data about the location for the city
        Args: City
        Return: returns the data found from the API for latitude and longitude
        '''
        url = f"https://api.opencagedata.com/geocode/v1/json?q={city}&key={self.api_key}"
        response = requests.get(url)
        data = json.loads(response.text)
        return data['results'][0]['geometry']