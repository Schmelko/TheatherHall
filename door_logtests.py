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
        self.assertEqual(len(self.door_log.entries),516)



if __name__ == '__main__':
    unittest.main()