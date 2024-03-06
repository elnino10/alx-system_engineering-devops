#!/usr/bin/python3
"""function queries the Reddit API and returns the number of subscribers"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    recursive function that queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit. If no results are found
    for the given subreddit, the function should return None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=9"
    user_agent = "alx:0x16-api_advanced:v1.0 (by /u/Joe-Egboka)"
    requests.get(url, user_agent, timeout=10).json()
