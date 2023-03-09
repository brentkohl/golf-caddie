import unittest
from unittest import mock
from unittest import TestCase
from unittest.mock import patch
import sys

sys.path.append("..")
from src.golf_caddie import golf_cad as golf


class DictCreateTests(unittest.TestCase):
    @mock.patch("src.golf_caddie.input", create=True)
    def testCustomClubs(self, mocked_input):
        mocked_input.side_effect = [
            "Driver",
            "275",
            "3-wood",
            "243",
            "3",
            "212",
            "4",
            "203",
            "5",
            "194",
            "6",
            "183",
            "7",
            "172",
            "8",
            "160",
            "9",
            "148",
            "PW",
            "136",
            "52",
            "120",
            "56",
            "110",
            "60",
            "100",
            "putter",
            "green",
        ]
        result = golf.custom()
        self.assertDictEqual(
            result,
            {
                "Driver": "275",
                "3-wood": "243",
                "3": "212",
                "4": "203",
                "5": "194",
                "6": "183",
                "7": "172",
                "8": "160",
                "9": "148",
                "PW": "136",
                "52": "120",
                "56": "110",
                "60": "100",
                "putter": "green",
            },
        )


if __name__ == "__main__":
    unittest.main()
    print("Test Passed")
