import os

import praw


def get_reddit(client, secret, username, password):
    reddit = praw.Reddit(
        client_id=client,
        client_secret=secret,
        username=username,
        password=password,
        user_agent='Script <Ridley> by /u/{}'.format(username),
    )
    return redit


def main():
    username = os.environ['REDDIT_USER']
    password = os.environ['REDDIT_PASS']
    client = os.environ['REDDIT_CLIENT']
    secret = os.environ['REDDIT_SECRET']

    redit = get_reddit(client, secret, username, password)
    print(redit.user)

if __name__ == '__main__':
    main()
