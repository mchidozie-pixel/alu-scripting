#!/usr/bin/python3
"""
This module provides a function that interacts with the Reddit API.
It retrieves and prints the titles of the first 10 hot posts for
a specified subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts.

    Args:
        subreddit (str): The name of the subreddit to query.

    If the subreddit is invalid or an error occurs, the function prints None.
    """
    # Custom User-Agent to avoid generic bot blocking (Reddit API requirement)
    headers = {
        'User-Agent': 'python:api.advanced:v1.0.0 (by /u/wintermancer)'
    }
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'limit': 10}

    try:
        # allow_redirects=False ensures we don't follow 302s to search results
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        if response.status_code == 200:
            posts = response.json().get('data', {}).get('children', [])
            if not posts:
                print(None)
                return
            for post in posts:
                print(post.get('data', {}).get('title'))
        else:
            print(None)
    except Exception:
        print(None)
