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
        self.assertEqual(self.door_log.find_first_entry_by_person_id_with_direction_in(),(2))

    def test_task2b(self):
        self.assertEqual(self.door_log.find_last_entry_by_person_id_with_direction_out(),(6))

    def test_task3(self):
        expected = {
            1: 21, 2: 12, 3: 14, 4: 14, 5: 10, 6: 22, 7: 18, 9: 12, 10: 18, 11: 13, 12: 8, 14: 10, 15: 14,
            16: 16, 18: 10, 20: 10, 21: 16, 22: 9, 23: 22, 24: 15, 25: 32, 26: 10, 27: 14, 28: 10, 29: 13, 
            30: 11, 31: 16, 32: 8, 35: 21, 36: 26, 37: 17, 38: 18, 39: 12, 40: 12, 41:12
        }
        result = self.door_log.find_no_of_crossings_by_person_ids()

        self.assertEqual(expected, result)

    def test_task3b(self):
        expected = { 1: 21, 2: 12, 3: 14 }
        result = self.door_log.find_no_of_crossings_by_person_ids()

        self.assertEqual(expected[1], result[1])
        self.assertEqual(expected[2], result[2])
        self.assertEqual(expected[3], result[3])

if __name__ == '__main__':
    unittest.main()