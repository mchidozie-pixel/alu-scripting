#!/usr/bin/python3
"""Module to fetch top 10 hot posts from Reddit API"""
import requests


def top_ten(subreddit):
    """Print titles of the first 10 hot posts of a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-api-project"}
    params = {"limit": 10}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get("data", {}).get("children", [])

    if not posts:
        print(None)
        return

    for post in posts:
        print(post.get("data", {}).get("title"))

