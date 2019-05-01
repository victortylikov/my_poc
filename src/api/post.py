import requests

from configs import get_argument_url
from conftest import CMD_ARGS


class Post:

    def get_post(self):
        print("AAA1 ", CMD_ARGS["--url"], CMD_ARGS["--browser"])
        post_url = 'https://jsonplaceholder.typicode.com/posts'
        return requests.get(url=post_url)
