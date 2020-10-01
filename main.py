from door_log import DoorLog
from datetime import time

with open('ajto.txt') as f:
    lines = f.readlines()
    door_log = DoorLog(lines)

print(door_log)

print(door_log.find_first_entry_by_person_id_with_direction_in())

print(door_log.find_last_entry_by_person_id_with_direction_out())

print(door_log.find_no_of_crossings_by_person_ids())
