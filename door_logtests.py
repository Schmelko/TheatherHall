import unittest
from door_log import DoorLog
from door_log_entry import DoorLogEntry
from datetime import time


class TestSolution(unittest.TestCase):

    def setUp(self):
        with open('ajto.txt') as f:
            lines = f.readlines()
        
        self.door_log = DoorLog(lines)

    def test_task1(self):
        expected = 516
        result = len(self.door_log.entries)
        self.assertEqual(expected, result)

    def test_task2(self):
        self.assertEqual(self.door_log.find_first_entry_by_person_id_with_direction_in(), (2))

    def test_task2b(self):
        self.assertEqual(self.door_log.find_last_entry_by_person_id_with_direction_out(),)


if __name__ == '__main__':
    unittest.main()