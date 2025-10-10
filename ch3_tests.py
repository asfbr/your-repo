spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1

#while True:
   # print('Please type your name.')
    #name = input('>')
    #if name == 'your name':
     #   break
#print('Thank you!')

name= ''
while not name:
    print('Enter your name:')
    name = input('>')
print('How many guests will you have?')
numOfGuests = int(input('>'))
if numOfGuests:
    print('Be sure to have enough room for all your guests.')
print('Done')