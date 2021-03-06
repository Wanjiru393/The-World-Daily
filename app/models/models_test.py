import unittest
from models import source

Source = source.Source


class SourceTest (unittest.TestCase):
    """
    Test class to test behaviour of the source class
    """

    def setUp(self):
        """
        Method to run before every Test
        """
        self.new_source = Source(
            "abc-news", "ABC News", "http://abcnews.go.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, source))


if __name__ == '__main__':
    unittest.main()
