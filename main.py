from door_log import DoorLog

with open('ajto.txt') as f:
    lines = f.readlines()
    door_log = DoorLog(lines)

print(door_log)
