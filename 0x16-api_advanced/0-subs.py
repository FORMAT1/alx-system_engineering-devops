#!/usr/bin/python3
"""fuunction  for the number_of_subscribers"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """returns the number of  subscribers for a given subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    """Set a custom User-Agent to avoid being blocked"""
    headers = {'User-Agent': 'xica369'}

    """Send an HTTP GET request to the Reddit API"""
    response = requests.get(url, headers=headers)
    
   """ Check if the request was successful"""
    if response.status_code == 200:
        try:
            data = response.json()
            """Extract the number of subscribers from the response"""
            subscribers = data['data']['subscribers']
            return subscribers
        except (KeyError, ValueError):
            """Invalid JSON response"""
            return 0
    else:
        """Invalid subreddit or other error"""
        return 0
