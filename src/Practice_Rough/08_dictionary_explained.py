
employee ={
    'name':'keran',
    'age':'31',
    'gender':'male',
    'number':'9811085395',
    'experience':'6years'
}

print(employee)

#printing keys
print(employee.keys())

#printing values
print(employee.values())

#printing the all the items
print(employee.items())

#in aproper format
for key,value in employee.items():
    print(f'{key}= {value}')

print(employee)
#pop
employee.pop('number')
print(employee)

#pop the last element
employee.popitem()
print(employee)

#updaing the dictionary
employee.update({'hobbies':'daycare_captain'})
print(employee)

#copy_dict
n_employee = employee.copy()
print(n_employee)

#clear dictionary
n_employee.clear()
print(n_employee)
