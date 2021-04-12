import sys


name = input('Name: ')
sex = input('Sex: ')

# use exception handling to cover an integer conversion error
try:
    time = int(input('Time: '))
except ValueError:
    print('Zeit muss eine Zahl sein (idealerweise 0-23)', file=sys.stderr)
    sys.exit(1)

if sex == 'm':
    anrede = 'Mr.'
elif sex == 'f':
    anrede = 'Mrs.'
else:
    print('Falsches Geschlecht (m/f will ich haben):', sex, file=sys.stderr)
    sys.exit(1)
    
    print('Falsche Zeit (0-23 will ich haben):', file=sys.stderr)
    sys.exit(1)

# print(hallo, ',', anrede, name)
# print('{0}, {1} {2}'.format(hallo, anrede, name))
# print('{hlo}, {anr} {nm}'.format(anr=anrede, nm=name, hlo=hallo))
print(f'{hallo}, {anrede} {name}')
