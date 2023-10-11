#!/usr/bin/python3
"""A recursive function that queries the Reddit API"""
import requests
import sys
after = None
count_dic = []


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """ parses the title of all hot articles, and prints a sorted count of given
    keywords (case-insensitive, delimited by spaces. Javascript should count as
    javascript, but java should not).
    """
    global after
    global count_dic
    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)
