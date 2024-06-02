course_rooms = { # Create course/room dictionary
    'CSC101' : 3004,
    'CSC102' : 4501,
    'CSC103' : 6755,
    'NET110' : 1244,
    'COM241' : 1411
}
course_profs = { # Create course/instructor dictionary
    'CSC101' : 'Haynes',
    'CSC102' : 'Alvarado',
    'CSC103' : 'Rich',
    'NET110' : 'Burke',
    'COM241' : 'Lee'
}
course_times = { # Create course/meeting time dictionary
    'CSC101' : '8:00 a.m.',
    'CSC102' : '9:00 a.m.',
    'CSC103' : '10:00 a.m.',
    'NET110' : '11:00 a.m.',
    'COM241' : '1:00 p.m.'
}

course = input('Course Name: ') # Gets user input for course

print(f'\n{course}') # Prints course header

# All if/elif statements check if the course is listed in each dictionary, then prints value, otherwise prints N/A
if course in course_rooms:
    print(f'Room: {course_rooms[course]}')
elif course not in course_rooms:
    print('Room: N/A')

if course in course_rooms:
    print(f'Instructor: {course_profs[course]}')
elif course not in course_rooms:
    print('Instructor: N/A')

if course in course_rooms:
    print(f'Meeting Time: {course_times[course]}')
elif course not in course_rooms:
    print('Meeting Time: N/A')
