import pprint

from src.api.post import Post

#check
def test_post_health_check():
    post = Post()
    post_response = post.get_post()
    assert post_response.status_code == 200


def test_post_health_check2():
    post = Post()
    post_response = post.get_post()
    assert post_response.status_code == 200


def test_post_health_check3():
    post = Post()
    post_response = post.get_post()
    assert post_response.status_code == 200
