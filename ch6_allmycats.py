cat_names = []
while True:
    print('Enter the name of cat ' + str(len(cat_names) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    cat_names = cat_names + [name]  # List concatenation
print('The cat names are:')
for name in cat_names:
    print('  ' + name)

print('Enter a pet name:')
name = input()
if name not in cat_names:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')



import random
random.shuffle(cat_names)
print('Here are the cat names in random order:')
for name in cat_names:
    print('  ' + name)

