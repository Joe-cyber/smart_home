import unittest
from unittest.mock import patch, PropertyMock

import mock.adafruit_dht as adafruit_dht
import mock.GPIO as GPIO
from SmartHome import SmartHome
from SmartHomeError import SmartHomeError


class SmartHomeTest(unittest.TestCase):
    """
    Your test cases go here
    """
    def setUp(self) -> None:
        self.sm = SmartHome()

    @patch.object(GPIO, "input")
    def test_check_room_occupancy_true(self, mock_input):
        mock_input.return_value = 0
        occ = self.sm.check_room_occupancy()
        self.assertTrue(occ)

    @patch.object(GPIO, "input")
    def test_check_room_occupancy_false(self, mock_input):
        mock_input.return_value = 1
        occ = self.sm.check_room_occupancy()
        self.assertFalse(occ)
