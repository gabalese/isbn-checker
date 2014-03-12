import unittest
from checkisbn import is_valid as check_isbn


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.test_isbn_list = {
            "correct": [
                "9788866324430",
                "9788-866-3248-81",
                "8876411542"
            ],
            "wrong": [
                "9788866324433",
                "9758866324430",
                "1-9788866324430"
            ],
            "with_spaces": [
                "978886 6324430",
                "9788 866 3248 81",
                "887 64 11  5 42"
            ],
            "non_numeric": [
                "ksjdfhg",
                "98797656__2òijsg",
                "978886632123O"
            ]
        }

    def test_correctisbns(self):
        for isbn in self.test_isbn_list["correct"]:
            self.assertTrue(check_isbn(isbn))

    def test_correctisbn_withspaces(self):
        for isbn in self.test_isbn_list["with_spaces"]:
            self.assertTrue(check_isbn(isbn))

    def test_incorrect_isbn(self):
        for isbn in self.test_isbn_list["wrong"]:
            self.assertFalse(check_isbn(isbn))

    def test_incorrect_nonnumeric_isbn(self):
        for isbn in self.test_isbn_list["non_numeric"]:
            self.assertFalse(check_isbn(isbn))


if __name__ == '__main__':
    unittest.main()
