phonebook = {'kran': '555-4444', 'white': '666-1111', 'pang': '333-2222'}

print(phonebook)

print(phonebook['white'])
print(phonebook.get('pang'))

key = 'Pluto'
if key in phonebook:
    print(phonebook['Pluto'])
else:
    print(key = 'not in phonebook')

phonebook['simson'] = '666-4449'
phonebook['Pluto'] = '999-4447'
phonebook['white'] = '555-7878'
print(phonebook)

del phonebook['simson']
print(phonebook)