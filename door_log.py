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
    
    def find_unique_person_ids(self):
        result = set(entry.person_id for entry in self.entries)
        return result
    
    def find_no_of_crossings_by_person_ids(self):
        result = {person_id:len(self.find_entries_by_person_id(person_id)) for person_id in self.find_unique_person_ids()}
        return result
    
    def find_entries_by_person_id(self, person_id):
        result = tuple(entry for entry in self.entries if entry.person_id == person_id)
        return result
    