from configparser import ConfigParser
import os

import praw


def read_config(ini_file):
    config = ConfigParser()
    config.read(ini_file)
    return config


def get_reddit(config):
    return praw.Reddit(
        client_id=config['client_id'],
        client_secret=config['client_secret'],
        username=config['username'],
        password=config['password'],
        user_agent='python:ridley:0.1 (by /u/{})'.format(config['username']),
    )


def main():
    config = read_config('local.ini')

    reddit = get_reddit(config['Auth'])

    user = config['Auth']['username']
    redditor = reddit.redditor(user)
    print('Link karma: {}'.format(redditor.link_karma))

    print(vars(reddit.user.me()))

    for sub in reddit.user.me().comments.top('week'):
        print(sub)
        print(vars(sub))


if __name__ == '__main__':
    main()
