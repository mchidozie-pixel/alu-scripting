#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 
10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the top 10 hot posts for a given subreddit.
    If the subreddit is invalid, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/your_username)"
    }
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        # If the status code is 200, the subreddit exists and is accessible
        if response.status_code == 200:
            data = response.json().get("data", {})
            children = data.get("children", [])
            for post in children:
                print(post.get("data", {}).get("title"))
        else:
            print(None)
    except Exception:
        print(None)
