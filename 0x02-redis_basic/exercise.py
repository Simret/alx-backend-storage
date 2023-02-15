#!/usr/bin/env python3
'''Cache class to flush the instance'''

import uuid
import redis
from typing import Any, Callable, Union


class Cache:
    '''An object for storing data in a Redis data storage'''

    def __init__(self) -> None:
        '''Initializes a Cache instance'''
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Stores a value in a Redis data storage'''
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key
