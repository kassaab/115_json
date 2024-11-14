#
import json

#
data1 = {
    'name': 'Abraham',
    'age': 30,
    'city': 'Seattle, WA',
    'interests': ['Traveling', 'Videogames', 'outdoors', 'Walking'],
    'is_student': True
}


with open('data1.json', 'w') as json_file:

    #Dump the Data Dictionary into the JSON file
    json.dump(data1,json_file, indent=4)


print("You have successfully written data1 json file")


with open('data1.json', 'r') as json_file:
    loaded_data = json.load(json_file)

# loaded_data = json.dumps(loaded_data, indent=1) #me

print("Successfully able to read data1.json")
print(loaded_data)


loaded_data['age'] = 24
loaded_data['interests'].append('Abraham1')
loaded_data['interests'].append('Abraham2')

with open('data1.json', 'w') as json_file:
    json.dump(loaded_data, json_file, indent=4)

print("Data has beeen re-written to data1.json")
