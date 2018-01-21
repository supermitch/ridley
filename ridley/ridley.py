import os

import praw


CLIENT_ID = 'ox7oa9jyv2iEIg'
CLIENT_SECRET = 'HmEATEoGGUGm-4SJTZHCbYr0eYg'


def get_reddit(id, secret, username, password):
    reddit = praw.Reddit(
        client_id=id,
        client_secret=secret,
        username=username,
        password=password,
        user_agent='Script <Ridley> by /u/{}'.format(username),
    )
    return redit


def main():
    username = os.environ['REDDIT_USER']
    password = os.environ['REDDIT_PASS']

    redit = get_reddit(username, password)
    print(redit.user)

if __name__ == '__main__':
    main()
