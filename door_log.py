from door_log_entry import DoorLogEntry
from datetime import time

class DoorLog:

    def __init__(self, lines):
        self.entries = [DoorLogEntry(line) for line in lines]

    def __str__(self):
        return "{} entries in door_log".format(len(self.entries))

    def find_first_entry_by_person_id_with_direction_in(self):
        filtered_entries = tuple(entry for entry in self.entries if entry.direction == 'be')
        first_entry = filtered_entries[0]
        return first_entry.person_id
    
    def find_last_entry_by_person_id_with_direction_out(self):
        filtered_entries = tuple(entry for entry in self.entries if entry.direction == 'ki')
        last_entry = filtered_entries[-1]
        return last_entry.person_id
    