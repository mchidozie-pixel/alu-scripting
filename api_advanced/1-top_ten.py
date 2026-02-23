#!/usr/bin/python3
"""Fetch and print top 10 hot posts"""
import requests


def top_ten(subreddit):
    """Print titles of first 10 hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {
        "User-Agent": "python:alu.reddit.api:v1.0 (by /u/anonymous)"
    }

    params = {"limit": 10}

    res = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if res.status_code != 200:
        print(None)
        return

    posts = res.json().get("data", {}).get("children", [])

    if not posts:
        print(None)
        return

    for post in posts:
        print(post.get("data").get("title"))

