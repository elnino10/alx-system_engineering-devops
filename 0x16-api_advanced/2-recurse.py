#!/usr/bin/python3
"""function queries the Reddit API and returns the number of subscribers"""

import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """
    recursive function that queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit. If no results are found
    for the given subreddit, the function should return None.
    """

    if not subreddit:
        return None

    params = {"after": after, "count": count, "limit": 50}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    res = requests.get(
        url, headers=headers, params=params, allow_redirects=False, timeout=10
    ).json()

    res_data = res.get("data")
    after = res_data.get("after")
    count += res_data.get("dist")
    # add titles from res_data.children to the hot_list
    for child in res_data.get("children"):
        hot_list.append(child.get("data").get("title"))

    # for more data to be fetched recursively call recurse()
    if after:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
