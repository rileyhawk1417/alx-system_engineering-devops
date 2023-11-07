#!/usr/bin/python3

"""Function to check number of subscribers in sub reddit"""
import requests as req


def number_of_subscribers(subreddit):
    """Function to check number of subscribers in sub reddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    custom_headers = {"User-Agent": "Reddit Fetch Agent 1.0"}
    res = req.get(url, headers=custom_headers)
    if res.status_code == 200:
        reply = res.json()
        return reply.get("data").get("subscribers")
    else:
        return 0
