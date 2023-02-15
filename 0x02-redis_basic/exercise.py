#!/usr/bin/env python3
'''Cache class to flush the instance'''

import redis


class Cache:
    '''An object for storing data in a Redis data storage'''

    def __init__(self) -> None:
        '''Initializes a Cache instance'''
        self._redis = redis.Redis()
        self._redis.flushdb(True)
