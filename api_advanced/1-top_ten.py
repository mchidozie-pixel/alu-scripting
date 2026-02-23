#!/usr/bin/python3
"""Print top 10 hot post titles for a subreddit"""

import requests


def top_ten(subreddit):
    """Fetch and print titles"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {
        "User-Agent": "python:alu.project:v1.0 (by /u/anonymous)"
    }

    params = {"limit": 10}

    try:
        res = requests.get(url,
                           headers=headers,
                           params=params,
                           allow_redirects=False,
                           timeout=10)

        if res.status_code != 200:
            print(None)
            return

        posts = res.json().get("data", {}).get("children", [])

        if not posts:
            print(None)
            return

        for post in posts:
            print(post.get("data").get("title"))

    except Exception:
        print(None)
