#!/usr/bin/python3

"""Function to check top posts in a sub reddit recursively"""
import requests as req


def recurse(subreddit, hot_list=[], after="", count=0):
    """Function to check top posts in a sub reddit recursively"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {"User-Agent": "Reddit Fetch Agent 1.0"}
    param = {
        "after": after,
        "count": count,
        "limit": 100,
    }
    res = req.get(url, headers=header, params=param, allow_redirects=False)
    if res.status_code == 400:
        return None
    reply = res.json().get("data")
    after = reply.get("after")
    count = reply.get("dist")
    for idx in reply.get("children"):
        hot_list.append(idx.get("data").get("title"))
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
