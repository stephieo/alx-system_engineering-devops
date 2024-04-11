#!/usr/bin/python3
""" script to query Reddit API and
return the number of users in given subreddit
"""
from client_secrets import USERNAME, PASSWORD, CLIENT_ID, CLIENT_SECRET
import json
import requests
import requests.auth


def number_of_subscribers(subreddit):
    """ return the  number of total subscribers
        in a given subreddit
    """
    # Authenticating Reddit app
    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    post_data = {
        'grant_type': 'password',
        'username': USERNAME,
        'password': PASSWORD
    }
    headers = {
        'User-Agent': 'Stephanie'
    }

    # Getting token Access Id
    TOKEN_ACCESS_ENDPOINT = 'https://www.reddit.com/api/v1/access_token'
    response = requests.post(TOKEN_ACCESS_ENDPOINT, data=post_data,
                             headers=headers, auth=client_auth)
    if response.status_code == 200:
        token_id = response.json()['access_token']
        headers['Authorization'] = f"bearer {token_id}"

    # Query
    OAUTH_ENDPOINT = "https://oauth.reddit.com"
    response = requests.get(OAUTH_ENDPOINT + f"/r/{subreddit}/about",
                            headers=headers, allow_redirects=False)

    if response.status_code != 200:
        # print("ERRORR!", response.status_code)
        return 0

    subscriber_count = response.json().get('data').get('subscribers')
    return subscriber_count
