import requests
import json

alphabet = 'abcdefghijklmnopqrstuvwxyz'
maxLength = 3


def permutations(perm, position, string):
    if position == len(perm):
        username = ''.join(perm)
        url = 'http://gitlab.com/users/' + username + '/exists'
        res = requests.get(url)
        exists = json.loads(res.text)['exists']

        if not exists:
            print(username + ' is AVAILABLE')
            with open('gitlab.txt', 'a') as file:
                file.write(username + '\n')
        else:
            print(username + ' is unavailable')

    else:
        for i in range(0, len(string)):
            perm[position] = string[i]
            permutations(perm, position + 1, string)


for length in range(1, maxLength + 1):
    perm = []
    for j in range(0, length):
        perm.append(0)
    permutations(perm, 0, alphabet)
