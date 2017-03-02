import requests
import time

alphabet = 'abcdefghijklmnopqrstuvwxyz'
maxLength = 3


def permutations(perm, position, string):
    if position == len(perm):
        username = ''.join(perm)
        url = 'https://github.com/signup_check/username'
        payload = {
            'value': username,
            'authenticity_token': 'TyaQYDldmiSSXXa71Tx/3ceA8sfD3kGOdi2t7jrwTBD8P/mVHaXUkT+/WokacRWBvViic1fl0PDfsZAovT34Lg=='
        }
        headers = {
            'Host': 'github.com',
            'Connection': 'keep-alive',
            'Content-Length': '141',
            'Origin': 'https://github.com',
            'x-requested-with': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'Referer': 'https://github.com/join?source=header-home',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.8',
            'Cookie': '_octo=GH1.1.1900469204.1488489436; logged_in=no; _ga=GA1.2.628263974.1488489442; _gat=1; tz=America%2FNew_York; _gh_sess=eyJzZXNzaW9uX2lkIjoiNGE5YWIyZjgwMGJjMWU5MmUzMWEyMzU3NzAwNTA0MmUiLCJfY3NyZl90b2tlbiI6IkZxQUdndlFVVGdKM0grWk80WHpkaUZrQmFIaFdWMTFCY2dwdjJRYUJDSzQ9IiwicmVmZXJyYWxfY29kZSI6Imh0dHBzOi8vZ2l0aHViLmNvbS8iLCJsYXN0X3dyaXRlIjoxNDg4NDg5NDQxOTQ0fQ%3D%3D--e232a1389ffd30ca25a0fb59ad03aa95b2de55ba'
        }
        while True:
            res = requests.post(url, data=payload, headers=headers)
            if res.status_code == 200:
                exists = False
                break
            elif res.status_code == 403 and res.text.strip() == 'Username is already taken':
                exists = True
                break
            elif res.status_code == 429:
                print("Too fast, pausing for 2 minutes...")
                time.sleep(120)

        if not exists:
            print(username + ' is AVAILABLE')
            with open('github.txt', 'a') as file:
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
