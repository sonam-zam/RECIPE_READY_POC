from logging import Logger

import boto3


class BaseRepository(object):

    def __init__(self):
        self.logger = Logger(name="repositories")
        self.dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
