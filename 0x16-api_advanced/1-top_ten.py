#!/usr/bin/python3
"""function queries the Reddit API and returns the number of subscribers"""

import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=9"
    user_agent = "Lolly"
    req_res = requests.get(url, user_agent, timeout=10).json()

    try:
        for child in req_res.get("data").get("children"):
            print(child.get("data").get("title"))
    except Exception:
        print(None)


if __name__ == "__main__":
    from sys import argv

    top_ten(argv[1])
