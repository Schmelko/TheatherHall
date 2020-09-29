
class DoorLogEntry:
    '''One log entry.'''

    def __init__(self, line):
        raw = line.split()
        self.timehour = raw[0]
        self.timeminute = raw[1]
        self.person_id = int(raw[2])
        self.direction = raw[3]