#!/usr/bin/python3
"""function queries the Reddit API and returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """returns number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    req_res = requests.get(
        url, headers=headers, allow_redirects=False, timeout=10
    ).json()

    try:
        return req_res.get("data").get("subscribers")
    except Exception:
        return 0


if __name__ == "__main__":
    from sys import argv

    number_of_subscribers(argv[1])
