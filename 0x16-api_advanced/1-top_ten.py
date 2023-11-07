#!/usr/bin/python3

"""Function to check top 10 posts in a sub reddit"""
import requests as req


def top_ten(subreddit):
    """Function to check top 10 posts in a sub reddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    custom_headers = {"User-Agent": "Reddit Fetch Agent 1.0"}
    res = req.get(url, headers=custom_headers, allow_redirects=False)
    if res.status_code == 200:
        reply = res.json().get("data").get("children")
        for idx in range(10):
            print(reply[idx].get("data").get("title"))
    else:
        print("None")
