def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

def assign_rooms(names):
    room_assignments = []
    for i, name in enumerate(names):
        room_number = i + 1  # Rooms are 1-indexed
        room_assignments.append(f"Hello, {name}! You'll be assigned to room {room_number}!")
    return room_assignments

def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)
    
    # Print badge messages
    for badge in badges:
        print(badge)
    
    # Print room assignments
    for room in rooms:
        print(room)

