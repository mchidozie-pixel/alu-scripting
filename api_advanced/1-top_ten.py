#!/usr/bin/python3
"""Fetch top 10 hot posts from Reddit"""
import requests


def top_ten(subreddit):
    """Print titles of first 10 hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get("data", {}).get("children", [])

    if not data:
        print(None)
        return

    for post in data:
        print(post.get("data").get("title"))

