import unittest
import urllib.request

from gutencorp.get_cache import URL

class TestURL():
    urllib.request.urlopen(URL).getcode()

class TestGetCache(unittest.TestCase):
    raise NotImplementedError

