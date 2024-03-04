# Create the dictionaries for the room numbers, instructors, and meeting times
room_numbers = {
    'CSC101': '3004',
    'CSC102': '4501',
    'CSC103': '6755',
    'NET110': '1244',
    'COM241': '1411',
}

instructors = {
    'CSC101': 'Haynes',
    'CSC102': 'Alvarado',
    'CSC103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee',
}

meeting_times = {
    'CSC101': '8:00 a.m.',
    'CSC102': '9:00 a.m.',
    'CSC103': '10:00 a.m.',
    'NET110': '11:00 a.m.',
    'COM241': '1:00 p.m.',
}

while True:
    # Get the user input for the course number
    course_number = input("Enter the course number (e.g., CSC101): ").upper()

    # Check if the course number is in the dictionaries
    if course_number in room_numbers:
        room_number = room_numbers[course_number]
        instructor = instructors[course_number]
        meeting_time = meeting_times[course_number]

        print(f"Course: {course_number}")
        print(f"Room Number: {room_number}")
        print(f"Instructor: {instructor}")
        print(f"Meeting Time: {meeting_time}")
        break  # Exit the loop if a valid course number is in the dictionaries
    else:
        print("Course is not found. Please try again.")