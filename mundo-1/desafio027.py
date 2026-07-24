name = str(input('Enter your full name: ')).strip()
newname = name.split()

print('Your firt name is: {}'.format(newname[0]))
print('Your last name is: {}'.format(newname[len(newname)-1]))
print(len(newname))
