#!/usr/bin/python3
"""fuunction  for the number_of_subscribers"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """ returns the number of  subscribers for a given subreddit
    """
    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    return (0)
	
