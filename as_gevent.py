import requests
from gevent import Greenlet

def get_request(url: str):
    return requests.get(url)

if __name__ == "__main__":
    g = Greenlet(get_request, "http://www.gevent.org")
    g.start()