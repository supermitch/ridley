import os

import praw


def get_reddit(client, secret, user, password):
    return praw.Reddit(
        client_id=client,
        client_secret=secret,
        username=user,
        password=password,
        user_agent='python:ridley:0.1 (by /u/{})'.format(user),
    )


def main():
    user = os.environ['USER']
    password = os.environ['PWD']
    client = os.environ['CLIENT']
    secret = os.environ['SECRET']

    reddit = get_reddit(client, secret, user, password)

    redditor = reddit.redditor(user)
    print(redditor.link_karma)  # Output: users's karma

    for sub in reddit.redditor(user).submissions:
        print(sub)


if __name__ == '__main__':
    main()
