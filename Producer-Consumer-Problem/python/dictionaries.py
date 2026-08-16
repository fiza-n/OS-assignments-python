student = {
    'name': 'Fiza',
    'age': 22,
    'course_list': ['History', 'Physics', 'English']
}
print(student.keys(), student.values() , sep="\n")

print(student.get('phone', 'Not found'))

# update
student.update({
    'name': 'iqra',
    'age': 22,
    'phone': '555-555-55'
})

# delete
del student['course_list'][0]

print(student.items())

print(student)

# if(student.get('Phone')):
#     print('Not found')
    
# loops in dict

for index,(keys, values) in enumerate(student.items() , start=1):
    if index ==2:
        print(index, keys, values)