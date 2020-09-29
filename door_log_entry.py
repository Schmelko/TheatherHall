from datetime import time

class DoorLogEntry:
    '''One log entry.'''

    def __init__(self, line):
        raw = line.split()
        self.hour_and_minute = time(int(raw[0]),int(raw[1]))
        self.person_id = int(raw[2])
        self.direction = raw[3]