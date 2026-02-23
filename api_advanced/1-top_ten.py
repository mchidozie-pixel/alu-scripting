#!/usr/bin/python3
"""
Module for querying the Reddit API to get the top 10 hot posts.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 
    10 hot posts listed for a given subreddit.
    
    If the subreddit is invalid, prints None.
    """
    # The URL for the hot posts in JSON format
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # User-Agent header to prevent 429 (Too Many Requests) errors
    headers = {
        'User-Agent': 'python:api.advanced:v1.0.0 (by /u/wintermancer)'
    }

    # Parameters to limit the results to the first 10
    params = {'limit': 10}

    try:
        # allow_redirects=False is vital to detect invalid subreddits
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        if response.status_code == 200:
            # Extract the 'children' list from the data
            data = response.json().get('data', {})
            posts = data.get('children', [])
            
            for post in posts:
                print(post.get('data', {}).get('title'))
        else:
            # For 302, 404, or any other non-200 status
            print(None)
    except Exception:
        # Fallback for connection issues or JSON parsing errors
        print(None)
