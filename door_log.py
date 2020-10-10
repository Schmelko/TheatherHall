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

    def person_ids_at_end_of_period(self):
        person_ids = self.find_unique_person_ids()
        entries_by_person_ids = {person_id:self.find_entries_by_person_id(person_id) for person_id in person_ids}
        last_entries_by_person_ids = {person_id:entries[-1] for (person_id,entries) in entries_by_person_ids.items()}
        last_directions_by_person_ids = {person_id:entry.direction for (person_id, entry) in last_entries_by_person_ids.items()}
        result = tuple(person_id for (person_id,direction) in last_directions_by_person_ids.items() if direction == 'be')
        return result

    def current_head_counts(self):
        current_head_count = 0
        head_counts_with_time = []
        for entry in self.entries:
            if entry.direction == 'be':
                current_head_count += 1
            else:
                current_head_count -= 1
            head_counts_with_time.append((entry.hour_and_minute, current_head_count))

        max_head_count = max(tuple(head_count_with_time[1] for head_count_with_time in head_counts_with_time))
        
        for head_count_with_time in head_counts_with_time:
            if head_count_with_time[1] == max_head_count:
                return head_count_with_time[0]

    def find_stayings_by_person_id_with_while(self, person_id):
        entries_by_id = list(self.find_entries_by_person_id(person_id))
        crossings = []
        while len(entries_by_id) > 1:
            crossings.append((entries_by_id[0], entries_by_id[1]))
            entries_by_id = entries_by_id[2:]
        if (len(entries_by_id) > 0):
            crossings.append((entries_by_id[0],))
        return crossings

    def find_stayings_by_person_id_with_for(self, person_id):
        entries_by_id = list(self.find_entries_by_person_id(person_id))
        crossings = []
        last_index = len(entries_by_id) if len(entries_by_id) % 2 == 0 else len(entries_by_id) - 1
        for index in range(0, last_index, 2):
            crossings.append((entries_by_id[index], entries_by_id[index + 1]))
        if (len(entries_by_id) % 2 == 1):
            crossings.append((entries_by_id[-1],))
        return crossings
