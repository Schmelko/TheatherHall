from door_log_entry import DoorLogEntry

class DoorLog:

    def __init__(self, lines):
        self.entries = [DoorLogEntry(line) for line in lines]

    def __str__(self):
        return "{} entries in door_log".format(len(self.entries))