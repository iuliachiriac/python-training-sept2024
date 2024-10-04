import os
import unittest

from examples.files import grep


class TestGrep(unittest.TestCase):
    TEST_FILE = "testfile.txt"

    @classmethod
    def setUpClass(cls):
        lines = ["hello world\n", "hi there\n", "bye world!\n", "bye\n"]
        with open(cls.TEST_FILE, "w") as f:
            f.writelines(lines)

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.TEST_FILE)

    def test_lines_match_with_search_term(self):
        matching_lines = grep("world", self.TEST_FILE)

        self.assertIsInstance(matching_lines, list)
        self.assertEqual(len(matching_lines), 2)
        self.assertListEqual(matching_lines, ["hello world\n", "bye world!\n"])

    def test_lines_do_not_match_with_search_term(self):
        matching_lines = grep("nothing", self.TEST_FILE)

        self.assertIsInstance(matching_lines, list)
        self.assertEqual(len(matching_lines), 0)

    def test_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            grep("something", "nonexistent.txt")
