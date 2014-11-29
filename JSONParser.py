import json
from pprint import pprint
from collections import Counter

#open fie
with open('exer4-courses.json') as json_data:
	#create data structure
	data = json.load(json_data)
	json_data.close()

#create list of students
students = []
for course in data:
	for student in courses['students']:
		students.append(student)

#count how many times they appear (how many courses they have)
output = Counter(students)

#dump to json file
f=open('output.json', 'w')
json.dump(output, f)

