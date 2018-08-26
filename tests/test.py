"""
Unit testing of the automatic batch processing application

http://www.codingtricks.biz/ci-cd-python-project-with-gitlab/
"""
import unittest
from src.twitter_bot import unfollow_back_who_not_folow_me

class AppTests(unittest.TestCase):
  def test_app(self):
    """Simple Tests"""

def suite():
  _suite = unittest.TestSuite()
  _suite.addTest(AppTests('test_app'))
  #_suite.addTest(AppTests('test_errors'))
  return _suite
