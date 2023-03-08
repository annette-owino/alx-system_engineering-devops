#!/usr/bin/python3
"""
<<<<<<< HEAD
Using reddit's API
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """returning top ten post titles recursively"""
    global after
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    results = requests.get(url, params=parameters, headers=user_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = results.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
=======
Function that requires the Reddit API and prints
the top ten hot posts of a subreddit
"""
import requests
import sys


def add_title(hot_list, hot_posts):
    """ Adds item into a list """
    if len(hot_posts) == 0:
        return
    hot_list.append(hot_posts[0]['data']['title'])
    hot_posts.pop(0)
    add_title(hot_list, hot_posts)


    def recurse(subreddit, hot_list=[], after=None):
        """ Queries to Reddit API """
        u_agent = 'Mozilla/5.0'
        headers = {
            'User-Agent': u_agent
        }

        params = {
            'after': after
        }

        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        res = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

        if res.status_code != 200:
            return None

        dic = res.json()
        hot_posts = dic['data']['children']
        add_title(hot_list, hot_posts)
        after = dic['data']['after']
        if not after:
            return hot_list
        return recurse(subreddit, hot_list=hot_list, after=after)
>>>>>>> 2d1c284690028753bd399b27afb16f922db869bd
