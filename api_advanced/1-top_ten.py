#!/usr/bin/python3
"""Print top 10 hot post titles for a subreddit"""

import requests


def top_ten(subreddit):
    """Main function"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)

        if response.status_code != 200:
            print(None)
            return

        posts = response.json().get("data", {}).get("children", [])

        if not posts:
            print(None)
            return

        for post in posts:
            print(post.get("data").get("title"))

    except Exception:
        print(None)
