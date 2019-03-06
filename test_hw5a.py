"""test program to run unit tests on hw4a program that counts number of repositories and commits in each repository
    author: srikanth"""

import urllib.request
import urllib.parse
import urllib.error
import json
import requests
import unittest
from unittest import mock
import unittest.mock
from unittest.mock import *
from hw4a import git_repocommits

class TestRepocommits(unittest.TestCase):
    @patch('requests.get')
    def testRepocommits_srikii(self, mockedReq): 
        n="richkempinski"
        mockedReq.return_value = MockResponse('[{"name":"hellogitworld"},{"name":"helloworld"},{"name":"Mocks"},{"name":"Project1"},{"name":"threads-of-life"}]')
        self.assertEqual(git_repocommits(n),(['hellogitworld', 'helloworld', 'Mocks', 'Project1', 'threads-of-life'], [30, 6, 9, 2, 1]))

class MockResponse:
    def __init__(self, blah):
        self.text=blah

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
