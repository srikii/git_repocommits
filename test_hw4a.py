"""test program to run unit tests on hw4a program that counts number of repositories and commits in each repository
    author: srikanth"""

import urllib.request
import urllib.parse
import urllib.error
import json
import requests
import unittest
from hw4a import git_repocommits

class TestRepocommits(unittest.TestCase):

    def testRepocommits_srikii(self): 
        n="richkempinski"
        self.assertEqual(git_repocommits(n),(['hellogitworld', 'helloworld', 'Mocks', 'Project1', 'threads-of-life'], [30, 6, 9, 2, 1]))

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
